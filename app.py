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
    #save_path_input = ObjectProperty(None)
    wav_name_input = ObjectProperty(None)
    page_start_input = ObjectProperty(None)
    page_end_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        # Label for PDF file path
        #pdf_label = Label(text='PDF File Path:')
        #self.add_widget(pdf_label)

        # Button to select PDF file
        #pdf_button = Button(text='Select PDF', on_press=self.select_pdf_path)
        #self.add_widget(pdf_button)

        # Text input for PDF file path
        #self.pdf_path_input = TextInput(hint_text='Enter PDF file path')
        #self.add_widget(self.pdf_path_input)

        # Label for WAV file name
        #wav_label = Label(text='WAV File Name:')
        #self.add_widget(wav_label)

        # Text input for WAV file name
        #self.wav_name_input = TextInput(hint_text='Enter WAV file name')
        #self.add_widget(self.wav_name_input)
        # Text input for start page
        #self.page_start_input = TextInput(hint_text='Enter start page')
        #self.add_widget(self.page_start_input)
        # Text input for end page
        #self.page_end_input = TextInput(hint_text='Enter end page')
        #self.add_widget(self.page_end_input)

        # Button to select destination folder
        #save_button = Button(text='Select Save Path', on_press=self.select_save_path)
        #self.add_widget(save_button)

        # Button to convert PDF to WAV
        #convert_button = Button(text='Convert PDF to WAV', on_press=self.convert_pdf_to_wav)
        #self.add_widget(convert_button)

    def select_pdf_path(self):
        self.popup = Popup(title='Select PDF File', content=FileChooserIconView(), size_hint=(0.9, 0.9))
        self.popup.content.bind(on_submit=self.on_pdf_select)
        self.popup.open()

    #def select_save_path(self):
        #root = tk.Tk()
        #root.withdraw()  # Hide the main tkinter window
        #save_path = filedialog.askdirectory()  # Open the directory picker dialog
        #self.save_path_input.text = save_path
        #print("Selected directory:", save_path)
    #def select_save_path(self):
    #    self.popup = Popup(title='Select Destination Folder', content=FileChooserIconView(path=os.getcwd(), dirselect=True), size_hint=(0.9, 0.9))
    #    self.popup.content.bind(on_submit=self.on_save_select)
    #    self.popup.open()

    def on_pdf_select(self, instance, path, touch):
        self.pdf_path_input.text = path[0]
        self.popup.dismiss()

    #def on_save_select(self, instance, path, touch):
    #    self.save_path_input.text = path[0]
    #    self.popup.dismiss()

    def convert_pdf_to_wav(self):
        pdf_path = self.pdf_path_input.text.strip()
        #save_path = self.save_path_input.text.strip()
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

        converter.pdf_to_wav(pdf_path, page_start, page_end, wav_name)

        self.show_popup("Success", f"Conversion completed. WAV file saved as {wav_name}")

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

class PDFToWavApp(App):
    def build(self):
        return PDFToWavConverter()

if __name__ == "__main__":
    PDFToWavApp().run()
