import tkinter as tk
import time
from process.processor import run_video_processor, run_table_processor, run_text_processor, run_web_scraper, find_and_save_matching_data
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

        self.process_label = []
        rely_values = [0.55 + i * 0.05 for i in range(6)]
        for rely in rely_values:
            label = tk.Label(master, text="")
            label.place(relx=0.5, rely=rely, anchor="center")
            self.process_label.append(label)



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
            start_time = time.time()

            (video_processor, process_label) = run_video_processor(video_path)
            self.process_label[0].config(text=process_label)

            (text_processor, process_label) = run_text_processor(video_processor.temp_folder_path)
            self.process_label[1].config(text=process_label)

            process_label = run_web_scraper()
            self.process_label[2].config(text=process_label)

            (table_processor, process_label) = run_table_processor()
            self.process_label[3].config(text=process_label)

            text_data = text_processor.data
            process_label = find_and_save_matching_data(table_processor, text_data)
            self.process_label[4].config(text=process_label)

            total_duration = time.time() - start_time
            self.process_label[5].config(text=f"Total execution time: {total_duration:.2f} seconds")

            # Clean up temporal folder
            video_processor.cleanup()
            self.show_message("Achievements processing completed.")
            self.process_button.config(state=tk.NORMAL)

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)

    def show_message(self, message):
        tk.messagebox.showinfo("Message", message)