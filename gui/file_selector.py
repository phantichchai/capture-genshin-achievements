import tkinter as tk
from tkinter import filedialog

class FileSelector(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.selected_file = None

        self.label = tk.Label(self, text="Select Video File:")
        self.label.pack(side="left")

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_video)
        self.browse_button.pack(side="right")

    def browse_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if video_path:
            self.selected_file = video_path
            self.label.config(text=f"Selected File: {video_path}")

    def get_selected_file(self):
        return self.selected_file
