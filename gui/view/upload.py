import tkinter as tk
from process.processor import run
from threading import Thread
from ..file_selector import FileSelector

class UploadView(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label = tk.Label(master, text="Undiscovered achievements", font=("Helvetica", 24, "bold"))
        self.label.place(relx=0.5, rely=0.2, anchor="center")

        self.file_selector = FileSelector(master)
        self.file_selector.place(relx=0.5, rely=0.4, anchor="center")

        self.process_button = tk.Button(master, text="Process Achievements", command=self.process_achievements)
        self.process_button.place(relx=0.5, rely=0.5, anchor="center")

    def process_achievements(self):
        if hasattr(self.file_selector, "selected_file") and self.file_selector.get_selected_file():
            self.process_button.config(state=tk.DISABLED)
            self.process_button.update()
            self.process_thread = Thread(target=self.process_achievements_thread)
            self.process_thread.start()
        else:
            self.show_error("Please select a video file.")

    def process_achievements_thread(self):
        # Get the selected file from the FileSelector instance
        video_path = self.file_selector.get_selected_file()
        if video_path:
            run(video_path)
            self.show_message("Achievements processing completed.")
            self.process_button.config(state=tk.NORMAL)

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)

    def show_message(self, message):
        tk.messagebox.showinfo("Message", message)