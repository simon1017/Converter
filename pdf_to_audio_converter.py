import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox, scrolledtext
import os, platform
import converter, textFilter
import translator as tl

class TextEditorWindow:
    def __init__(self, root, text):
        self.root = root
        self.root.title("Text Editor")

        self.text_editor = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_editor.pack(expand=True, fill='both', padx=5, pady=5)
        self.text_editor.insert(tk.END, text)

        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack()

        self.save_button = ctk.CTkButton(button_frame, text="Save", command=self.save_and_close)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.close_button = ctk.CTkButton(button_frame, text="Cancel", command=self.close_window)
        self.close_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.edited_text = None

    def save_and_close(self):
        self.edited_text = self.text_editor.get("1.0", tk.END)
        self.root.destroy()

    def close_window(self):
        self.root.destroy()


class PDFToAudioConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to audio converter")
        self.os_version = platform.system()

        # Initialize converter
        self.converter = converter.Converter()

        # Initialize translator
        self.translator = tl.MyTranslator()

        # Initialize textfilter
        self.textfilter = textFilter.TextFilter()

        # Create input widgets
        self.create_input_widgets()

    def create_input_widgets(self):
        # PDF path
        self.pdf_path_label = ctk.CTkLabel(self.root, text="PDF path:")
        self.pdf_path_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.pdf_path_input = ctk.CTkEntry(self.root)
        self.pdf_path_input.grid(row=0, column=1, padx=5, pady=5)
        self.pdf_path_button = ctk.CTkButton(self.root, text="Select PDF", command=self.select_pdf_path)
        self.pdf_path_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        # save folder path
        self.save_folder_label = ctk.CTkLabel(self.root, text="Save path:")
        self.save_folder_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.save_folder_input = ctk.CTkEntry(self.root)
        self.save_folder_input.grid(row=1, column=1, padx=5, pady=5)
        self.save_folder_button = ctk.CTkButton(self.root, text="Select folder", command=self.select_save_folder)
        self.save_folder_button.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

        # mp3 filename
        self.audio_name_label = ctk.CTkLabel(self.root, text="filename:")
        self.audio_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.audio_name_input = ctk.CTkEntry(self.root)
        self.audio_name_input.grid(row=2, column=1, padx=5, pady=5)
        self.audio_name_label2 = ctk.CTkLabel(self.root, text=".mp3")
        self.audio_name_label2.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)

        # Start page
        self.page_start_label = ctk.CTkLabel(self.root, text="Start page:")
        self.page_start_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.page_start_input = ctk.CTkEntry(self.root)
        self.page_start_input.insert(0, "0")
        self.page_start_input.grid(row=3, column=1, padx=5, pady=5)

        # End page
        self.page_end_label = ctk.CTkLabel(self.root, text="End page:")
        self.page_end_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.page_end_input = ctk.CTkEntry(self.root)
        self.page_end_input.insert(0, "0")
        self.page_end_input.grid(row=4, column=1, padx=5, pady=5)

        # translate from language
        self.translate_from_Label = ctk.CTkLabel(self.root, text="PDF language: ")
        self.translate_from_Label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        langs = self.translator.get_langs()
        #print(f"type is: {type(langs)}")
        self.from_lang = tk.StringVar(self.root)
        self.from_lang.set(langs[21])
        self.translate_from_menu = ctk.CTkOptionMenu(master=self.root, variable=self.from_lang, values=langs)
        self.translate_from_menu.grid(row=7, column=1, padx=5, pady=5)

        # translation checkbox
        self.use_translation_bool = tk.BooleanVar(value=False)
        self.use_translation_checkbox = ctk.CTkCheckBox(self.root, variable=self.use_translation_bool, onvalue=True, offvalue=False, text="use translation")
        self.use_translation_checkbox.grid(row=8, column=0, padx=5, pady=5)

        # translate to language
        self.translate_to_Label = ctk.CTkLabel(self.root, text="Translate to: ")
        self.translate_to_Label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

        self.to_lang = tk.StringVar(self.root)
        self.to_lang.set(langs[91])
        self.translate_to_menu = ctk.CTkOptionMenu(master=self.root, variable=self.to_lang, values=langs)
        self.translate_to_menu.grid(row=9, column=1, padx=5, pady=5)

        # Convert button
        self.convert_button = ctk.CTkButton(self.root, text="Convert", command=self.open_text_editor)
        self.convert_button.grid(row=10, column=1, padx=5, pady=15)

    def select_pdf_path(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        self.pdf_path_input.insert(0, pdf_path)

    def select_save_folder(self):
        save_path = filedialog.askdirectory()
        self.save_folder_input.insert(0, save_path)
        self.converter.set_save_folder(save_path)

    def on_slider_move(self, slider_value):
        self.speech_rate_value.set(slider_value)
        print(f"slider value: {self.speech_rate_value.get()}")
        self.converter.set_speech_rate(self.speech_rate_value.get())


    def open_text_editor(self):
        # Get input values
        pdf_path = self.pdf_path_input.get().strip()
        save_folder = self.save_folder_input.get().strip()
        audio_name = self.audio_name_input.get().strip()
        page_start = int(self.page_start_input.get().strip())
        page_end = int(self.page_end_input.get().strip())

        # Set converter parameters
        self.converter.set_pdf_path(pdf_path)
        self.converter.set_save_folder(save_folder)
        self.converter.set_audio_name(audio_name)
        self.converter.set_page_start(page_start)
        self.converter.set_page_end(page_end)
        
        if not pdf_path:
            messagebox.showerror("Error", "PDF path is required.")
            return
        
        if not audio_name:
            messagebox.showerror("Error", "Audio filename is required.")
            return
        
        if not save_folder:
            messagebox.showerror("Error", "Save folder is required.")
            return
        
        if not pdf_path or not audio_name:
            messagebox.showerror("Error", "PDF path and Audio filename are required.")
            return

        if not os.path.exists(pdf_path):
            messagebox.showerror("Error", "PDF file not found.")
            return
        
        if page_start <= 0 or page_end <= 0:
            messagebox.showerror("Error", "pages has to be greater than 0.")
            return

        if page_start > page_end:
            messagebox.showerror("Error", "Start page greater than End page")
            return
        
        if self.use_translation_bool.get():
            src = self.translator.get_codes(lang=self.from_lang.get())
            dest = self.translator.get_codes(lang=self.to_lang.get())
            self.converter.set_src(src)
            self.converter.set_dest(dest)
        
        text = self.converter.read_pdf(self.use_translation_bool.get())
        root_editor = tk.Tk()
        root_editor.configure(background='black')
        text_editor_window = TextEditorWindow(root_editor, text)
        root_editor.wait_window(text_editor_window.root)
        edited_text = text_editor_window.edited_text
        self.convert_pdf_to_audio(edited_text)

    def convert_pdf_to_audio(self, edited_text):
        if edited_text is not None:
            self.converter.convert(edited_text,self.audio_name_input.get(), self.use_translation_bool.get())
            messagebox.showinfo("Success", f"Conversion completed. audio file saved.")

def main():
    root = tk.Tk()
    root.configure(background='black')
    app = PDFToAudioConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
