import tkinter as tk
import openwindow as ow
from tkinter import ttk
from tkinter import font as Font
import os
import sys

root = tk.Tk()

def open_window():
    ow.open_window()
    closeMainWindow()

def closeMainWindow():
    root.destroy()


root.title("Annoying Wordful Launcher")
root.geometry("600x300")
root.config(bg="#1800ad")
style = ttk.Style()

adlam = Font.Font(family="Adlam Display", size=14)

style.configure("Custom.TButton", background="#1800ad", foreground="black", font=adlam)

open_btn = ttk.Button(root, text="Launch Game", command=open_window, style="Custom.TButton")
open_btn.pack(expand=True)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(base_path, "icon.ico")
#root.iconbitmap(icon_path)


if __name__ == "__main__":
    root.mainloop()