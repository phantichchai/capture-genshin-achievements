import tkinter as tk
from tkinter import ttk
from .view.upload import UploadView

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

if __name__ == "__main__":
    root = tk.Tk()
    app = GenshinImpactAchievementsApp(root)
    root.mainloop()
