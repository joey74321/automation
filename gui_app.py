# gui_app.py
import tkinter as tk
from tkinter import ttk

# Importing individual application classes
from image_to_pdf_app import ImageToPdfApp
from pdf_to_audio_app import PdfToAudioApp
from photo_compressor_app import PhotoCompressorApp
from plagiarism_checker_app import PlagiarismCheckerApp
from text_to_speech_app import TextToSpeechApp  # Importing the TextToSpeechApp class
from proofreading_app import ProofreadingApp
from pdf_to_csv_app import PdfToCsvApp
from youtube_downloader_app import YouTubeDownloaderApp

class GUIApp:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        master.title("Automation App")
        root.geometry("520x280")  # Adjust the width and height as needed

        # Create UI components
        self.label = ttk.Label(master, text="Please choose one of the following:")
        self.label.pack()

        # Dropdown menu with available options
        self.options = ["Proofreading", "PDF to CSV", "Photo Compressor", "YouTube Downloader",
                        "Text to Speech", "Image to PDF", "Plagiarism Checker", "PDF to Audio"]

        # Combobox for selecting options
        self.option_combobox = ttk.Combobox(master, values=self.options)
        self.option_combobox.pack()

        # Button to execute the selected option
        self.execute_button = ttk.Button(master, text="Execute", command=self.execute_option)
        self.execute_button.pack()

    def execute_option(self):
        # Execute the selected option based on the combobox value
        selected_option = self.option_combobox.get()
        if selected_option == "Text to Speech":
            self.open_text_to_speech_app()
        elif selected_option == "Proofreading":
            self.open_proofreading_app()
        elif selected_option == "PDF to CSV":
            self.open_pdf_to_csv_app()
        elif selected_option == "Photo Compressor":
            self.open_photo_compressor_app()
        elif selected_option == "YouTube Downloader":
            self.open_youtube_downloading_app()
        elif selected_option == "Image to PDF":
            self.open_image_to_pdf_app()
        elif selected_option == "Plagiarism Checker":
            self.open_plagiarism_checker_app()
        elif selected_option == "PDF to Audio":
            self.open_pdf_to_audio_app()
        else:
            # Handle other options or add similar if statements for other functionalities
            print(f"Executing {selected_option} option.")

    def open_text_to_speech_app(self):
        # Open the TextToSpeechApp when Text to Speech option is selected
        text_to_speech_window = tk.Toplevel(self.master)
        text_to_speech_app = TextToSpeechApp(text_to_speech_window)

    def open_proofreading_app(self):
        # Open the ProofreadingApp when Proofreading option is selected
        proofreading_window = tk.Toplevel(self.master)
        proofreading_app = ProofreadingApp(proofreading_window)

    def open_image_to_pdf_app(self):
        # Open the ImageToPdfApp when Image to PDF option is selected
        image_to_pdf_window = tk.Toplevel(self.master)
        image_to_pdf_app = ImageToPdfApp(image_to_pdf_window)

    def open_pdf_to_audio_app(self):
        # Open the PdfToAudioApp when PDF to Audio option is selected
        pdf_to_audio_window = tk.Toplevel(self.master)
        pdf_to_audio_app = PdfToAudioApp(pdf_to_audio_window)

    def open_pdf_to_csv_app(self):
        # Open the PdfToCsvApp when PDF to CSV option is selected
        pdf_to_csv_window = tk.Toplevel(self.master)
        pdf_to_csv_app = PdfToCsvApp(pdf_to_csv_window)

    def open_photo_compressor_app(self):
        # Open the PhotoCompressorApp when Photo Compressor option is selected
        photo_compressor_window = tk.Toplevel(self.master)
        photo_compressor_app = PhotoCompressorApp(photo_compressor_window)

    def open_plagiarism_checker_app(self):
        # Open the PlagiarismCheckerApp when Plagiarism Checker option is selected
        plagiarism_checker_window = tk.Toplevel(self.master)
        plagiarism_checker_app = PlagiarismCheckerApp(plagiarism_checker_window)

    def open_youtube_downloading_app(self):
        # Open the YouTubeDownloaderApp when YouTube Downloader option is selected
        youtube_downloading_window = tk.Toplevel(self.master)
        youtube_downloading_app = YouTubeDownloaderApp(youtube_downloading_window)


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
