import gtts, PyPDF2

def gTTS(message, filename):
    tts = gtts.gTTS(text=message, lang='en')
    tts.save(filename)

@staticmethod
def clean_text(text):
    text = text.strip().replace('\n', ' ')
    return text

def read_pdf(pdf_path, page_start, page_end, use_translate):
        pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
        filtered_text = []
        full_text = ""

        for page_num in range(page_start - 1, page_end):
            page = pdf_reader.pages[page_num].extract_text()

            #if use_translate:
            #    translated_text_parts = []
            #    chunk_size = 1200
            #    for i in range(0, len(page), chunk_size):
            #        chunk = page[i:i+chunk_size]
            #        translation = my_translator.translate_text(chunk, self.src, self.dest)
            #        translated_text_parts.append(translation)
            #    translated_page = "".join(translated_text_parts)
            #    filtered_text.append(self.clean_text(translated_page))
            #else:
            filtered_text.append(clean_text(page))

        full_text = ''.join(filtered_text)
        return full_text


if __name__ == "__main__":
    filename = "hello.mp3"
    gTTS(read_pdf("test.pdf", 40, 45, False), filename)