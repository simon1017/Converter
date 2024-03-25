import pyttsx3
import PyPDF2
import os
import time
import translator

class Converter:
    def __init__(self):
        self.pdf_path = ""
        self.save_folder = ""
        self.page_start = 0
        self.page_end = 0
        self.wav_name = f"my_wav{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}.wav"
        self.speaker = pyttsx3.init()
        self.my_translator = translator.MyTranslator()
        self.src = ""
        self.dest = ""

        # get voices, set def act, 
        self.voices = self.get_voices()
        self.active_voice = self.voices[0]
        self.set_active_voice(self.voices[14].name)
        
        # print available voices
        #print(len(self.voices))
        #for voice in self.voices:
        #    print(voice.name)

        # set def speech rate
        self.speech_rate = self.get_speech_rate()
        #print(f"speech rate: {self.speech_rate}")


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

    def set_wav_name(self, wav_name):
        self.wav_name = wav_name

    def get_wav_name(self):
        return self.wav_name

    def get_voices(self):
        return self.speaker.getProperty('voices')
    
    def set_active_voice(self, name):
        for voice in self.voices:
            if voice.name == name:
                self.active_voice = voice
                self.speaker.setProperty('voice', voice.id)

    def get_active_voice(self):
        return self.active_voice

    def set_speech_rate(self, speech_rate):
        self.speech_rate = speech_rate
        self.speaker.setProperty('rate', speech_rate)

    def get_speech_rate(self):
        return self.speaker.getProperty('rate')

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

    
    def convert(self, text):
        # setup
        # get voice
        voice_model = self.active_voice
        self.speaker.setProperty('voice', voice_model)

        # get save path
        save_path = self.save_folder
        #print(save_path)
        
        # save file
        self.speaker.save_to_file(text, os.path.join(save_path, self.get_wav_name()))
        self.speaker.runAndWait()
        self.speaker.stop()
        #print(f"saved as {self.wav_name}\nat\n{self.get_save_folder}")

    def voice_speak(self, name):
        self.set_active_voice(name)
        #print(f"name sent: {name}")
        #print(f"active voice: {self.active_voice.name}")
        phrase = f"Hi, my name is {self.active_voice.name}"
        self.speaker.say(phrase)
        self.speaker.runAndWait()


    @staticmethod
    def clean_text(text):
        text = text.strip().replace('\n', ' ')
        return text

if __name__ == "__main__":
    print("Wrong file, run app.py")
