import pyttsx3
import PyPDF2
import os, time
import translator, gtts

class Converter:
    def __init__(self):
        self.pdf_path = ""
        self.save_folder = ""
        self.page_start = 0
        self.page_end = 0
        self.audio_name = f"my_audio{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}.mp3"
        self.speaker = pyttsx3.init()
        self.my_translator = translator.MyTranslator()
        self.src = "en"
        self.dest = ""

        
    def get_src(self):
        return self.src
    
    def set_src(self, src):
        self.src = src
    
    def get_dest(self):
        return self.dest
    
    def set_dest(self, dest):
        self.dest = dest
        
    def set_pdf_path(self, pdf_path):
        self.pdf_path = pdf_path

    def get_pdf_path(self):
        return self.pdf_path

    def set_page_start(self, page_start):
        self.page_start = page_start

    def get_page_start(self):
        return self.page_start

    def set_save_folder(self, save_folder):
        self.save_folder = save_folder

    def get_save_folder(self):
        return self.save_folder

    def set_page_end(self, page_end):
        self.page_end = page_end

    def get_page_end(self):
        return self.page_end

    def set_audio_name(self, audio_name):
        self.audio_name = audio_name

    def get_audio_name(self):
        return self.audio_name

    def read_pdf(self, use_translate):
        pdf_reader = PyPDF2.PdfReader(open(self.pdf_path, 'rb'))
        filtered_text = []
        full_text = ""

        for page_num in range(self.page_start - 1, self.page_end):
            page = pdf_reader.pages[page_num].extract_text()

            if use_translate:
                translated_text_parts = []
                chunk_size = 1200
                for i in range(0, len(page), chunk_size):
                    chunk = page[i:i+chunk_size]
                    translation = self.my_translator.translate_text(chunk, self.src, self.dest)
                    translated_text_parts.append(translation)
                translated_page = "".join(translated_text_parts)
                filtered_text.append(self.clean_text(translated_page))
            else:
                filtered_text.append(self.clean_text(page))

        full_text = ''.join(filtered_text)
        return full_text

    
    def convert(self, text, filename, use_translate):
        # get save path
        save_path = self.get_save_folder()
        #print(save_path)
        if not filename.endswith(".mp3"):
            filename += ".mp3"
        file_path = os.path.join(save_path, filename)
        
        tts = gtts.gTTS(text=text, lang=self.get_dest() if use_translate else self.get_src())
        tts.save(file_path)


    @staticmethod
    def clean_text(text):
        text = text.strip().replace('\n', ' ')
        return text

if __name__ == "__main__":
    print("Wrong file, run app.py")
