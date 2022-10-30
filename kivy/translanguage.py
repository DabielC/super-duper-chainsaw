from googletrans import Translator

translator = Translator()

translated_text = translator.translate('Mhong', dest='th')
print(translated_text.text)
