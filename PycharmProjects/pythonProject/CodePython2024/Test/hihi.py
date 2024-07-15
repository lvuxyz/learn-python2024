import tkinter as tk
from tkinter import ttk

class Form1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Form 1")
        label.pack(pady=10, padx=10)
        button = ttk.Button(self, text="Go to Form 2",
                            command=lambda: controller.show_frame("Form2"))
        button.pack()

class Form2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Form 2")
        label.pack(pady=10, padx=10)
        button = ttk.Button(self, text="Go to Form 1",
                            command=lambda: controller.show_frame("Form1"))
        button.pack()

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tkinter Form Switching")
        self.geometry("300x200")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Form1, Form2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Form1")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
