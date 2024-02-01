# pdf_to_csv_app.py

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pdf_to_csv import pdf_to_csv_function  # Assuming you have a function in pdf_to_csv_script


class PdfToCsvApp:
    def __init__(self, master):
        """
        Initialize the PdfToCsvApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        master.title("PDF to CSV App")
        self.master.geometry("520x280")

        # UI components for PDF to CSV app
        self.pdf_label = tk.Label(master, text="Select PDF File:")
        self.pdf_label.pack()

        self.pdf_button = tk.Button(master, text="Choose PDF", command=self.choose_pdf_file)
        self.pdf_button.pack()

        self.upload_label = tk.Label(master, text="")
        self.upload_label.pack()

        self.csv_label = tk.Label(master, text="Choose CSV Output Path:")
        self.csv_label.pack()

        self.csv_button = tk.Button(master, text="Choose CSV Path", command=self.choose_csv_path)
        self.csv_button.pack()

        self.convert_button = tk.Button(master, text="Convert PDF to CSV", command=self.convert_pdf_to_csv)
        self.convert_button.pack()

        # Store the selected PDF and CSV paths as instance variables
        self.pdf_path = None
        self.csv_path = None

    def choose_pdf_file(self):
        """
        Open a file dialog to choose a PDF file.

        Updates the upload label with the result.
        """
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            self.upload_label.config(text="PDF Successfully Uploaded!")

    def choose_csv_path(self):
        """
        Open a file dialog to choose the CSV output path.
        """
        self.csv_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    def convert_pdf_to_csv(self):
        """
        Convert the chosen PDF file to CSV.

        Calls the pdf_to_csv_function and shows a message box with the conversion result.
        """
        if self.pdf_path and self.csv_path:
            pdf_to_csv_function(self.pdf_path, self.csv_path)
            messagebox.showinfo("Conversion Result", "PDF to CSV conversion complete!")
        else:
            messagebox.showwarning("Error", "Please upload a PDF file and choose a CSV path.")


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")
    app = PdfToCsvApp(root)
    root.mainloop()
