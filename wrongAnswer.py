import tkinter as tk
from tkinter import font as Font
import wordRenderer as wr
import enterButton as eb
import wordRandInt as wri
import openwindow as ow
import random as rnd
from tkinter import messagebox as mb
import correctAnswer as ca

root = tk.Toplevel()
root.withdraw()  # Hide the root window

def renderWrongAnswer(parent):
    win = parent
    print("wrong answer renderer called")
    wrongAnswerAction(parent)

resultLabelInt = 0
adlam = Font.Font(family="Adlam Display", size=10)
def wrongAnswerAction(parent):
    win = parent
    global resultLabelInt
    if hasattr(win, 'result_label'):
        win.result_label.destroy()
    if wrongAnswerAction:
        win.result_label.destroy
    resultLabelInt = resultLabelInt + 1
    win.result_label = tk.Label(win, text="Wrong Answer! Attempts: " + str(resultLabelInt), bg="#1800ad", fg="#c1ff72", font=adlam)
    win.result_label.pack(pady=10)
    print("result in is", resultLabelInt)
    print("wrong answer action called")

    if resultLabelInt >= 5:
        resultLabelInt = 0
        annoyingPopup(parent)
        eb.destroyWindowContents(parent)


def annoyingPopup(parent):
    if ca.correctAnswerCount == 0:
        taunt = wrongAnswerTaunts[rnd.randint(1, 15)]
        mb.showinfo("Wrong Answer", taunt)
    if ca.correctAnswerCount > 0:
        mb.showinfo("Wrong Answer", "HAH, YOU COUDN'T KEEP YOUR STREAK LOSER!")
        ow.resetCorrectIntCount()
        #ca.correctAnswerCount = 0
        print("Correct Answer Count:", ca.correctAnswerCount)
    print("Annoying popup called")
    global getTauntInt
    getTauntInt = 0

wrongAnswerTaunts = {
    1:"Are you even trying?",
    2: "Wrong again! Go to school bruv.",
    3: "Is this your best effort bro?",
    4: "Keep going! If you dare...",
    5: "This is proof that you are not smart.",
    6: "Did you think that was correct loser?",
    7: "Wrong! Learn some english brother.",
    8: "Incorrect! Maybe try using your brain this time?",
    9: "nope nope nope. wrong.",
    10: "Are you even paying attention?",
    11: "Wrong! Retake kindergarten.",
    12: "Incorrect! Did you even try?",
    13: "Wrong again! LOL.",
    14: "Is this your best effort? Pathetic.",
    15: "You're trash.",
}

wrongAnswerTauntInt = rnd.randint(1, 15)
getTaunt = wrongAnswerTaunts.get(wrongAnswerTauntInt)

def noAnswer(parent):
    win = parent
    global resultLabelInt
