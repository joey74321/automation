# image_to_pdf_app.py

import tkinter as tk
from tkinter import filedialog
from image_to_pdf import ImageToPdf


class ImageToPdfApp:
    def __init__(self, master):
        """
        Initialize the ImageToPdfApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        self.master.title("Image to PDF Converter")
        self.master.geometry("520x280")

        # UI components
        self.choose_file_button = tk.Button(self.master, text="Choose Image", command=self.choose_image)
        self.choose_file_button.pack(pady=10)

        self.convert_button = tk.Button(self.master, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=10)

        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack(pady=10)

        self.input_images = []

    def choose_image(self):
        """
        Open a file dialog to choose image files.

        Updates the status label with the chosen file(s).
        """
        file_paths = filedialog.askopenfilenames(filetypes=[("Image file", (".png", ".jpg", ".jpeg", ".heic"))])
        if file_paths:
            self.status_label.config(text=f"Chosen file(s): {', '.join(file_paths)}")
        else:
            self.status_label.config(text="No file chosen.")

    def convert_to_pdf(self):
        """
        Convert chosen image(s) to a PDF file.

        Opens a file dialog to choose the output PDF file.
        Updates the status label during conversion and after completion.
        """
        self.status_label.config(text="Conversion in progress...")
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            image_to_pdf = ImageToPdf(self.input_images, output_path)
            image_to_pdf.convert_images_to_pdf()
        # Simulate a delay for demonstration purposes
        self.master.after(2000, self.simulate_conversion_complete)

    def simulate_conversion_complete(self):
        """
        Simulate the completion of the conversion process.

        Updates the status label after a simulated delay.
        """
        self.status_label.config(text="Conversion complete!")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")
    app = ImageToPdfApp(root)
    root.mainloop()
