import tkinter as tk
import enterButton as eb
from tkinter import messagebox as mb

root = tk.Tk()
root.withdraw()  

correctAnswerCount = 0

def correctAnswerRendered(parent):
    win = parent
    global correctAnswerCount
    print("correct answer function called")
    eb.deleteAction(parent)
    correctAnswerCount += 1
    mb.showinfo("Correct Answer", f"Damn it, you won. But lets see how much you can guess right! Total Correct Answers: {correctAnswerCount}")

def resetWindow(parent):
    eb.destroyWindowContents(parent)
    print("Window reset called, correct answer count preserved:", correctAnswerCount)