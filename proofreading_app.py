# proofreading_app.py

import tkinter as tk
from tkinter import messagebox
from proofreading_script import proofreading_function


class ProofreadingApp:
    def __init__(self, master):
        """
        Initialize the ProofreadingApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        self.master.title("Proofreading App")
        self.master.geometry("520x280")

        self.label = tk.Label(master, text="Enter a sentence or paragraph for proofreading:")
        self.label.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.proofread_button = tk.Button(master, text="Proofread", command=self.proofread)
        self.proofread_button.pack()

    def proofread(self):
        """
        Perform proofreading on the entered sentence or paragraph.

        Calls the proofreading_function and displays the proofreading result using a messagebox.
        """
        user_input = self.entry.get()
        if not user_input:
            messagebox.showinfo("Error", "Please enter a sentence or paragraph.")
            return

        proofreading_result = proofreading_function(user_input)
        result_text = "Potential errors: {}".format(proofreading_result)
        messagebox.showinfo("Proofreading Result", result_text)


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")
    app = ProofreadingApp(root)
    root.mainloop()
