# pdf_to_audio_app.py

import PyPDF2
from gtts import gTTS
from tkinter import filedialog
import tkinter as tk


# Updated PdfToAudioApp class in pdf_to_audio_app.py
class PdfToAudioApp:
    def __init__(self, master):
        """
        Initialize the PdfToAudioApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        self.master.title("PDF to Audio Converter")
        self.master.geometry("520x280")  # Set the initial size of the window

        # Create GUI components
        self.choose_file_button = tk.Button(master, text="Choose PDF File", command=self.choose_pdf_file)
        self.choose_file_button.pack(pady=20)

        self.upload_status_label = tk.Label(master, text="")
        self.upload_status_label.pack()

        self.convert_button = tk.Button(master, text="Convert to Audio", command=self.convert_to_audio)
        self.convert_button.pack(pady=20)

        self.save_button = tk.Button(master, text="Save Audio", command=self.save_audio)
        self.save_button.pack(pady=20)

    def choose_pdf_file(self):
        """
        Open a file dialog to choose a PDF file.

        Updates the upload status label with the result.
        """
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        if self.pdf_path:
            self.upload_status_label.config(text="PDF successfully uploaded.")
        else:
            self.upload_status_label.config(text="No PDF selected.")

    def convert_to_audio(self):
        """
        Convert the chosen PDF file to audio.

        Extracts text from the PDF, converts it to audio using gTTS, and saves it as an MP3 file.
        """
        if not hasattr(self, 'pdf_path') or not self.pdf_path:
            print("No PDF file selected. Please choose a PDF file first.")
            return

        # Extract text from the PDF
        text = ""
        with open(self.pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        # Create gTTS object
        tts = gTTS(text=text, lang='en', slow=False)

        # Set the output audio file name
        output_filename = "output_audio.mp3"
        self.output_audio_path = output_filename

        # Save the audio file
        tts.save(self.output_audio_path)

        print("Conversion complete.")

    def save_audio(self):
        """
        Save the converted audio file.

        Opens a file dialog to choose the output path for the audio file.
        """
        if hasattr(self, 'output_audio_path'):
            import shutil
            save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio files", "*.mp3")])
            if save_path:
                shutil.copyfile(self.output_audio_path, save_path)
                print(f"Audio saved to {save_path}")
            else:
                print("Save operation canceled.")
        else:
            print("No audio to save. Please convert to audio first.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")
    app = PdfToAudioApp(root)
    root.mainloop()
