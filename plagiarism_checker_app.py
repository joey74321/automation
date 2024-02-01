# plagiarism_checker_app.py

import tkinter as tk
from tkinter import ttk
from plagiarism_checker import calculate_similarity


class PlagiarismCheckerApp:
    def __init__(self, master):
        """
        Initialize the PlagiarismCheckerApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        self.master.title("Plagiarism Checker App")
        self.master.geometry("520x280")

        self.label1 = ttk.Label(master, text="Enter text 1:")
        self.label1.pack()

        self.text_entry1 = tk.Text(master, height=5, width=40)
        self.text_entry1.pack()

        self.label2 = ttk.Label(master, text="Enter text 2:")
        self.label2.pack()

        self.text_entry2 = tk.Text(master, height=5, width=40)
        self.text_entry2.pack()

        self.output_button = ttk.Button(master, text="Check Plagiarism", command=self.check_plagiarism)
        self.output_button.pack()

    def check_plagiarism(self):
        """
        Check plagiarism between the entered text1 and text2.

        Calls the calculate_similarity function and displays the similarity ratio in a new label.
        """
        text1 = self.text_entry1.get("1.0", "end-1c")
        text2 = self.text_entry2.get("1.0", "end-1c")
        similarity_ratio = calculate_similarity(text1, text2)
        result_text = f"Similarity ratio: {similarity_ratio:.2f}"
        result_label = ttk.Label(self.master, text=result_text)
        result_label.pack()


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")
    app = PlagiarismCheckerApp(root)
    root.mainloop()
