import pyttsx3
import PyPDF2
import os

class Converter:
    def __init__(self, pdf_path, page_start, page_end, wav_name):
        self.pdf_path = pdf_path
        self.page_start = page_start
        self.page_end = page_end
        self.wav_name = wav_name

    def convert(self):
        pdf_reader = PyPDF2.PdfReader(open(self.pdf_path, 'rb'))
        speaker = pyttsx3.init()

        # Choose voice
        voice_model = "com.apple.speech.synthesis.voice.daniel.premium"
        speaker.setProperty('voice', voice_model)

        # Adjust speed
        rate = speaker.getProperty('rate')
        speaker.setProperty('rate', rate - 30)

        text = []
        new_text = []

        for page_num in range(self.page_start - 1, self.page_end):
            print(f"cleaning text page {page_num + 1}...")
            text.append(pdf_reader.pages[page_num].extract_text())
            new_text.append(self.clean_text(text[-1]))

            print("//---------------//")
            print(new_text[-1])
            print("//---------------//")

        save_path = os.path.join(os.getcwd(), "audio_files")
        print(save_path)
        full_text = ""
        for page in new_text:
            full_text += str(page)
        speaker.save_to_file(full_text, os.path.join(save_path, self.wav_name))
        speaker.runAndWait()
        speaker.stop()
        print(f"saved as {self.wav_name}")

    @staticmethod
    def clean_text(text):
        text = text.strip().replace('\n', ' ')
        return text

if __name__ == "__main__":
    print("Wrong file, run app.py")
