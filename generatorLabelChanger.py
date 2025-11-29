import tkinter as tk
from tkinter import font as Font
import wordRenderer as wr
import wordRandInt as wri

root = tk.Tk()
root.withdraw()  # Hide the root window
getword = ""

adlamDisplayFont = Font.Font(family="Adlam Display", size=30)
label = tk.Label(text="", font=adlamDisplayFont).pack(padx=10, pady=10)

def defaultLabel(parent):
    win = parent
    global label
    label = tk.Label(win, text="Generate Word to Start", font=adlamDisplayFont, bg="#1800ad", fg="#c1ff72")
    label.pack(padx=10, pady=10)

def removeLabel(parent):
    win = parent
    global label
    label.destroy()

def randomWordLabel(parent):
    win = parent
    wordLabel = wr.renderWord(wri.get_random_word())
    newLabel = tk.Label(win, text=wordLabel, font=adlamDisplayFont)
    newLabel.pack(padx=10, pady=10)
    

    