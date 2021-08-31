"""
 French/English Translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.api_exception import ApiException
from dotenv import load_dotenv

VERSION_API="2018-05-01"

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION_API,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Convert English Text to French"""

    #Assure that entry is a string
    englishText = str(englishText)

    if len(englishText) < 1:
        return ""

    try:
        translation = language_translator.translate(
            text=englishText,
            model_id='en-fr'
        ).get_result()

        # Take the first result among returned translations
        # If impossible, return empty string

        frenchText = translation["translations"][0]["translation"]
    except ApiException:
        frenchText = ""

    return frenchText

def frenchToEnglish(frenchText):
    """Convert French Text to English"""
    frenchText = str(frenchText)

    if len(frenchText) < 1:
        return ""

    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en'
    ).get_result()
    # Take the first result among returned translations
    # If impossible, return empty string
    try:
        englishText = translation["translations"][0]["translation"]
    except ApiException:
        englishText = ""

    return englishText
