import tkinter as tk
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

if __name__ == "__main__":
    root = tk.Tk()
    app = GenshinImpactAchievementsApp(root)
    root.mainloop()
