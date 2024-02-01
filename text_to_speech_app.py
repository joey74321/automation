# text_to_speech_app.py

import tkinter as tk
from tkinter import ttk
from text_to_speech import text_to_speech


class TextToSpeechApp:
    def __init__(self, master):
        """
        Initialize the TextToSpeechApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        self.master.title("Text to Speech App")
        self.master.geometry("520x280")

        self.label = ttk.Label(master, text="Enter text:")
        self.label.pack()

        self.text_entry = ttk.Entry(master, width=40)
        self.text_entry.pack()

        self.language_label = ttk.Label(master, text="Select language:")
        self.language_label.pack()

        self.language_var = tk.StringVar()
        self.language_var.set("en")  # Default language is English

        self.language_combobox = ttk.Combobox(master, values=["en", "es", "fr", "de"])
        self.language_combobox.pack()

        self.output_button = ttk.Button(master, text="Convert to Speech", command=self.convert_to_speech)
        self.output_button.pack()

    def convert_to_speech(self):
        """
        Convert the entered text to speech using the selected language.

        Calls the text_to_speech function with the entered text and selected language.
        """
        text = self.text_entry.get()
        language = self.language_var.get()
        text_to_speech(text, language)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")
    app = TextToSpeechApp(root)
    root.mainloop()
