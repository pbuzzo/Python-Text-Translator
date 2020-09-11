#!/usr/bin/env python3

from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import argparse


# Language Translator Credentials
url_lt = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ba447b0f-2b17-4a60-bd2f-89d1f61917bd"
apikey_lt = "dKcmTx64bTccpzLXnX7caL3D0cudUclQiD-2DlppEjo4"
version_lt = "2018-05-01"


# Speech-to-Text Credentials
url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/cdedc6d9-7355-47d6-830e-47062e7f45d4"
iam_apikey_s2t = "xVS_njyCYNW-EXqpSduRxiXHnnX90encwOmYJ-F_zb0p"


# parse command line arguments
def create_parser():
    """
    Create parser to parse command line arguments supplied by user
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('mp3_file', type=str,
                        help='MP3 file to convert to translated text')
    parser.add_argument('text_file', type=str, default="results.txt",
                        help='Name of file that results will be written to')
    return parser


def speech_to_text(in_file):
    """
    Convert audio speech to text via IBM API
    """
    with open(in_file, mode="rb") as wav:
        authenticator_s2t = IAMAuthenticator(iam_apikey_s2t)
        s2t = SpeechToTextV1(authenticator=authenticator_s2t)
        s2t.set_service_url(url_s2t)
        response = s2t.recognize(audio=wav, content_type='audio/mp3')
        recognized_text = response.result['results'][0]["alternatives"][0]["transcript"]
        return recognized_text


def languange_translator(in_file):
    """
    Translate text from English to Spanish
    """
    recognized_text = speech_to_text(in_file)
    authenticator_lt = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator_lt)
    language_translator.set_service_url(url_lt)
    translated_response = language_translator.translate(text=recognized_text, model_id='en-es')
    translation = translated_response.get_result()
    final_trans = translation['translations'][0]['translation']
    return final_trans


def write_to_file(in_file, out_file):
    """
    Write newly-translated text to new .txt file
    """
    final_trans = languange_translator(in_file)
    with open(out_file, mode="w") as result_file:
        for line in final_trans:
            result_file.write(line)


def main():
    # Parse command-line arguments to be used
    parser = create_parser()
    args = parser.parse_args()

    write_to_file(args.mp3_file, args.text_file)


if __name__ == '__main__':
    main()
