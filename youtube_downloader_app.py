# youtube_downloader_app.py

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from youtube_downloader import download_video


class YouTubeDownloaderApp:
    def __init__(self, master):
        """
        Initialize the YouTubeDownloaderApp class.

        Parameters:
        - master: The Tkinter root/master window.
        """
        self.master = master
        self.master.title("YouTube Video Downloader")
        self.master.geometry("520x280")

        # Create GUI components
        self.url_label = tk.Label(master, text="Enter YouTube Video URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(master, width=40)
        self.url_entry.pack()

        self.output_path_label = tk.Label(master, text="Choose Output Path:")
        self.output_path_label.pack()

        self.output_path_button = tk.Button(master, text="Choose Path", command=self.choose_output_path)
        self.output_path_button.pack()

        self.output_path_var = tk.StringVar()
        self.output_path_entry = tk.Entry(master, textvariable=self.output_path_var, state="readonly", width=40)
        self.output_path_entry.pack()

        self.download_button = tk.Button(master, text="Download Video", command=self.download_video)
        self.download_button.pack(pady=20)

    def choose_output_path(self):
        """
        Open a file dialog to choose the output path.

        Sets the selected output path in the corresponding entry.
        """
        output_path = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
        self.output_path_var.set(output_path)

    def download_video(self):
        """
        Download the YouTube video using the provided URL and save it to the specified output path.

        Shows a message box with the download result.
        """
        url = self.url_entry.get()
        output_path = self.output_path_var.get()

        if url and output_path:
            result = download_video(url, output_path)
            tk.messagebox.showinfo("Download Result", result)
        else:
            tk.messagebox.showwarning("Input Error", "Please enter a valid YouTube URL and choose an output path.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("520x280")
    root.resizable(False, False)
    root.title("YouTube Video Downloader")
    app = YouTubeDownloaderApp(root)
    root.mainloop()
