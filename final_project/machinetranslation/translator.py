"""Translator"""
from deep_translator import MyMemoryTranslator
 
# translate english to french
def english_to_french(english_text):
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text

# translate french to english
def french_to_english(french_text):
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text