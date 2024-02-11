import pyttsx3
import PyPDF2
import os

def text_filter(text):
    # split text into lines
    lines = text.split('\n')
    # remove last line
    new_text = ""
    for line in range(0, len(lines)-1):
        new_text += lines[line]
    return new_text

def clean_text(text):
    #text = text_filter(text)
    text = text.strip().replace('\n', ' ')
    return text

def get_os_path(file_name):
    return os.path.join(os.getcwd(), file_name)

def pdf_to_wav(pdf_path, page_start, page_end, wav_name):
    # init
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    speaker = pyttsx3.init()

    # chose voice
    voice_model = "com.apple.speech.synthesis.voice.daniel.premium"
    speaker.setProperty('voice', voice_model)

    # chose speed
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate - 30)
    text = []
    new_text = []

    for page_num in range(page_start - 1, page_end):  # Adjusted the range to include the specified pages
        print(f"cleaning text page {page_num + 1}...")
        text.append(pdf_reader.pages[page_num].extract_text())
        new_text.append(clean_text(text[-1]))

        print("//---------------//")
        print(new_text[-1])
        print("//---------------//")

    # get path and save wav file
    #full_path = get_os_path(wav_name)
    #print(full_path)
    save_path = os.path.join(os.getcwd(), "audio_files")
    print(save_path)
    full_text = ""
    for page in new_text:
        full_text += str(page)
    speaker.save_to_file(full_text, os.path.join(save_path, wav_name))
    speaker.runAndWait()
    speaker.stop()
    print(f"saved as {wav_name}")

#wav_name = "test_full.wav"
#pdf_path = 'test.pdf'
#page_start = 1
#page_end = 2

#pdf_to_wav(pdf_path, page_start, page_end, wav_name)
