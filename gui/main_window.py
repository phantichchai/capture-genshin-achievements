import tkinter as tk
from tkinter import ttk
from .view.upload import UploadView
from .view.table import TableView

class GenshinImpactAchievementsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Genshin Impact Achievements App")
        self.root.geometry("800x600")

        # Set the icon for the application
        icon_path = "resources/icon.ico"
        self.root.iconbitmap(icon_path)

        self.notebook = ttk.Notebook(self.root)  # Create a notebook widget
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Upload Video")  # Add tab 1
        self.notebook.add(self.tab2, text="Completed")  # Add tab 2
        self.notebook.add(self.tab3, text="Uncompleted") # Add tab 3

        self.upload_view = UploadView(self.tab1)
        self.completed_view = TableView(self.tab2,
                                        json_file="completed_achievement_data.json",
                                        transfer_label="Set to Upcompleted")
        self.uncompleted_view = TableView(self.tab3,
                                          json_file="uncompleted_achievement_data.json",
                                          transfer_label="Set to Completed")
        
        self.completed_view.set_other(self.uncompleted_view)
        self.uncompleted_view.set_other(self.completed_view)

if __name__ == "__main__":
    root = tk.Tk()
    app = GenshinImpactAchievementsApp(root)
    root.mainloop()
