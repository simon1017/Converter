from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.properties import ObjectProperty
import os
import converter

class PDFToWavConverter(BoxLayout):
    pdf_path_input = ObjectProperty(None)
    wav_name_input = ObjectProperty(None)
    page_start_input = ObjectProperty(None)
    page_end_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

    def select_pdf_path(self):
        self.popup = Popup(title='Select PDF File', content=FileChooserIconView(), size_hint=(0.9, 0.9))
        self.popup.content.bind(on_submit=self.on_pdf_select)
        self.popup.open()

    def on_pdf_select(self, instance, path, touch):
        self.pdf_path_input.text = path[0]
        self.popup.dismiss()

    def convert_pdf_to_wav(self):
        pdf_path = self.pdf_path_input.text.strip()
        wav_name = self.wav_name_input.text.strip()
        page_start = int(self.page_start_input.text.strip())
        page_end = int(self.page_end_input.text.strip())

        if not pdf_path:
            self.show_popup("Error", "PDF file path is required.")
            return

        if not os.path.exists(pdf_path):
            self.show_popup("Error", "PDF file not found.")
            return

        if not wav_name:
            self.show_popup("Error", "Destination folder is required.")
            return

        converter.Converter(pdf_path, page_start, page_end, wav_name).convert()

        self.show_popup("Success", f"Conversion completed. WAV file saved as {wav_name}")

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

class PDFToWavApp(App):
    def build(self):
        return PDFToWavConverter()

if __name__ == "__main__":
    PDFToWavApp().run()
