import tkinter as tk
from tkinter import font as Font
from tkinter import ttk
import wordRandInt as wri    
import wrongAnswer as wa
import enterButton as eb
import generatorLabelChanger as glc
import tkinter.messagebox as mb
import correctAnswer as ca
import random as rnd
import os
import sys



def open_window(master=None):
    win = tk.Toplevel(master) if master else tk.Toplevel()
    win.title("Annoying Wordful")
    win.geometry("800x400")
    win.config(bg="#1800ad")
    style = ttk.Style()
    adlam = Font.Font(family="Adlam Display", size=14)

    style.configure("Custom.TButton", background="#1800ad", foreground="black", font=adlam)

    glc.defaultLabel(win)  
    win.genbutton = ttk.Button(win, text="Generate Random Word", command=lambda: generate_word(win), style="Custom.TButton")
    win.genbutton.pack(pady=10)
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    icon_path = os.path.join(base_path, "icon.ico")
    win.iconbitmap(icon_path)

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    
    return os.path.join(os.path.abspath("."), relative_path)

def enterButtonAndTextbox(win):
    
    #canvas = tk.Canvas(win, width=513, height=30, bg="white")
    #canvas.pack()    
    
    adlam = Font.Font(family="Adlam Display", size=20)
    win.word_label = tk.Label(win, text="", font=adlam)
    win.word_label.pack(pady=10)

    win.text_box = tk.Text(win, height=1, width=30, borderwidth=3, relief="solid")
    #arial = Font.Font(family="Arial", size=25)
    win.text_box.configure(font=adlam)
    win.text_box.pack(padx=10, pady=10)
    win.text_box.bind("<Return>", lambda e: on_enter(e, win))


    win.enterButtonImage = tk.PhotoImage(file=resource_path("enterbutton.png"))

    style = ttk.Style()
    style.configure("Hover.TButton", background="#1800ad")
    win.enter_btn = ttk.Button(win, image=win.enterButtonImage, 
                              command=lambda: submit_answer(win), style="Hover.TButton")
    win.enter_btn.pack(pady=6)

    def hovering(e):
        style.configure("Hover.TButton", background="#c1ff72")
    def notHovering(e):
        style.configure("Hover.TButton", background="#1800ad") 
    
    win.enter_btn.bind("<Enter>", hovering)
    win.enter_btn.bind("<Leave>", notHovering)

    win.result_label = tk.Label(win, text="")
    win.result_label.pack(pady=8)

    win.wrong_attempts = 0

    global submitButtonPressedCount 
    submitButtonPressedCount = 0


    return win


def generate_word(parent):
    win = parent
    enterButtonAndTextbox(win)  
    try:
        word = wri.get_random_word()
    except Exception as e:
        print("Error getting random word:", e)
        word = None

    if not word:
        eb.destroyWindowContents(win)
        open_window(win)
        mb.showerror("Error", "No word generated. Please try again.")
        print("No word generated.")
        return

    glc.removeLabel(win)  
    win.current_word = str(word).strip()
    print("SET win.current_word ->", repr(win.current_word))

    word = win.current_word
    maskedWord = word[0] + " __ " * (len(word) -2) + word[-1]

    win.word_label.config(text=maskedWord, fg="#c1ff72", bg="#1800ad")
 
    
    if hasattr(win, "result_label"):
        win.result_label.config(text="", bg="#1800ad")  

    if hasattr(win, "genbutton"):
        win.genbutton.destroy()

    if hasattr(win, "text_box"):
        win.text_box.delete("1.0", tk.END)
        win.text_box.focus_set()

submitButtonPressedCount = 0

def submit_answer(win):
    eb.wrongAnswerGiven(win)   
    global submitButtonPressedCount
    submitButtonPressedCount = wa.resultLabelInt
    word = win.current_word
    maskedWordNoHint = word[0] + " __ " * (len(word) -2) + word[-1]

    if not hasattr(win, "hint_index"):
        win.hint_index = None

    if wa.resultLabelInt == 0:
        submitButtonPressedCount = 0
        win.hint_index = None

    if submitButtonPressedCount == 3:
        if not hasattr(win, "hint_index") or win.hint_index is None:
            win.hint_index = rnd.randint(1, len(word) - 2)
            maskedWord = buildMaskedWord(word, hint=win.hint_index)
        else:
            win.hint_index = None
        win.word_label.config(text=maskedWord)
        print(maskedWord)
    elif submitButtonPressedCount < 2:
        win.word_label.config(text=maskedWordNoHint)

    eb.deleteAction(win) 
    
def on_enter(event, win):
    submit_answer(win)
    return "break"  

def resetCorrectIntCount():
    ca.correctAnswerCount = 0

def buildMaskedWord(word, hint = None):
        letters = []
        for i, ch in enumerate(word):
            if i == 0 or i == len(word) - 1:
                letters.append(ch)
            elif hint is not None and i == hint:
                letters.append(ch)
            else:
                letters.append(" __ ")
        return "".join(letters)