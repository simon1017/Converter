from googletrans import Translator
from googletrans import LANGUAGES

class MyTranslator:
    def __init__(self):
        self.gtranslator = Translator()

    def get_langs(self):
        langs = []
        for lang_code, lang_name in LANGUAGES.items():
            #print(f"{lang_code}: {lang_name}")
            langs.append(lang_name)
        #print(f"type is: {type(LANGUAGES.values)}")
        return langs
    
    def get_codes(self, lang):
        for lang_code, lang_name in LANGUAGES.items():
            if lang_name == lang:
                return lang_code
        
    def translate_text(self, text, src, dest):
        #print(type(text))
        #print(type(src))
        #print(type(dest))
        translation = self.gtranslator.translate(str(text), src=str(src), dest=str(dest))
        #print(translation.text)
        return translation.text

if __name__ == "__main__":
    #MyTranslator().translate_text("Hello")
    #MyTranslator().translate_text("Hello", "en", "sv")
    pass