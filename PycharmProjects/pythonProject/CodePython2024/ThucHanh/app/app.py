from pathlib import Path
from tkinter import Tk
from ui_components import MainFrame

ASSETS_PATH = Path(r"C:\Users\hello1love\PycharmProjects\pythonProject\CodePython2024\ThucHanh\ASSETS_PATH")

class MyApplication(Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill="both", expand=True)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = MyApplication()
    app.run()
