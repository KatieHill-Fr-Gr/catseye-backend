import deepl
import os

_client = None 
'''
variable where deepl client is stored once created for the first time
it's called a "lazy-singleton" pattern, i.e. the stored client is reused for all subsequent calls
'''

def get_deepl_client():
    global _client
    if _client is None:
        key = os.environ['DEEPL_AUTH_KEY']


def translate_text(text: str, target_lang: str):
    client = get_deepl_client()
    result = client.translate_text(text, target_lang=target_lang)
    return result.text