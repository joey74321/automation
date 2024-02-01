# pdf_to_audio.py

from PyPDF2 import PdfReader
from gtts import gTTS
import pygame
from tkinter import filedialog
import tkinter as tk


def pdf_to_audio_function():
    # Open file dialog to choose a PDF file
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    root.destroy()

    if not pdf_path:
        print("No file selected. Exiting.")
        return

    # Extract text from the PDF
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    # Create gTTS object
    tts = gTTS(text=text, lang='en', slow=False)

    # Save the audio file
    output_audio_path = "output_audio.mp3"
    tts.save(output_audio_path)

    # Play the audio file using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(output_audio_path)
    pygame.mixer.music.play()


if __name__ == "__main__":
    pdf_to_audio_function()
