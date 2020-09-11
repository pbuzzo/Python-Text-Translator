# Python-Text-Translator
A Python program that converts audio of the English languange from an MP3 file into translated text, and then converts the text to Spanish.

Prerequisites:

1. Account made at: https://www.ibm.com/cloud/watson-studio
2. Create New Project using Speech-To-Text and Language Translation API's (free of charge for free tier)


Environment Set-Up:

1. `git clone git@github.com:pbuzzo/Python-Text-Translator.git spanish-translator`
2. `cd spanish-translator`
3. `pipenv shell`
4. `pipenv install`
5. `touch .env`
6. In `.env`, instantiate newly obtained credentials under appropriate values (LT_KEY, LT_URL, S2T_KEY, S2T_URL)
- For example: `LT_URL=<url goes here>`



Usage:

- `python3 translator.py <path of mp3 file> <name of results file>`


Example: `python3 translator.py /Users/test/sample-projects/text-translator/PolynomialRegressionandPipelines.mp3 results_text.txt`
