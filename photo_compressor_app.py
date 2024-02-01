# photo_compressor_app.py

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from photo_compressor import photo_compressor


class PhotoCompressorApp:
    def __init__(self, master):
        """
        Initialize the PhotoCompressorApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        master.title("Photo Compressor App")
        self.master.geometry("520x280")

        self.label = ttk.Label(master, text="Choose a photo to compress:")
        self.label.pack()

        self.choose_button = ttk.Button(master, text="Choose Photo", command=self.choose_photo)
        self.choose_button.pack()

        self.compress_button = ttk.Button(master, text="Compress Photo", command=self.compress_photo, state=tk.DISABLED)
        self.compress_button.pack()

        self.message_label = ttk.Label(master, text="")
        self.message_label.pack()

        self.selected_photo_path = ""

    def choose_photo(self):
        """
        Open a simple dialog to enter the file path of the photo to be compressed.

        Enables the compress button and updates the message label with the selected photo path.
        """
        file_path = simpledialog.askstring("Choose a photo", "Enter the file path:")
        if file_path:
            self.selected_photo_path = file_path
            self.compress_button["state"] = tk.NORMAL  # Enable the compress button
            self.message_label["text"] = f"Photo selected: {file_path}"

    def compress_photo(self):
        """
        Open a file dialog to choose the output path for the compressed photo.

        Calls the photo_compressor function and updates the message label with the result.
        """
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if output_path:
            photo_compressor(self.selected_photo_path, output_path)
            self.message_label["text"] = f"Photo compressed successfully. Saved at: {output_path}"


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")  # Set your desired width and height
    app = PhotoCompressorApp(root)
    root.mainloop()
