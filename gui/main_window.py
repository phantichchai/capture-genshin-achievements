import tkinter as tk
from tkinter import filedialog
from threading import Thread
from process.processor import run
from gui.file_selector import FileSelector

class GenshinImpactAchievementsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Genshin Impact Achievements App")
        self.root.geometry("800x600")

        # Set the icon for the application
        icon_path = "resources/icon.ico"
        self.root.iconbitmap(icon_path)

        self.label = tk.Label(self.root, text="Undiscovered achievements", font=("Helvetica", 24, "bold"))
        self.label.place(relx=0.5, rely=0.2, anchor="center")

        self.file_selector = FileSelector(self.root)
        self.file_selector.place(relx=0.5, rely=0.4, anchor="center")

        self.process_button = tk.Button(self.root, text="Process Achievements", command=self.process_achievements)
        self.process_button.place(relx=0.5, rely=0.5, anchor="center")

    def browse_video(self):
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        self.video_path = video_path
        if self.video_path:
            self.label.config(text=f"Selected Video: {self.video_path}")

    def process_achievements(self):
        if hasattr(self, "video_path") and self.video_path:
            self.process_button.config(state=tk.DISABLED)
            self.process_button.update()
            self.process_thread = Thread(target=self.process_achievements_thread)
            self.process_thread.start()
        else:
            self.show_error("Please select a video file.")

    def process_achievements_thread(self):
        run(self.video_path)
        self.show_message("Achievements processing completed.")
        self.process_button.config(state=tk.NORMAL)

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)

    def show_message(self, message):
        tk.messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = GenshinImpactAchievementsApp(root)
    root.mainloop()
