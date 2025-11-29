import wrongAnswer as wa
import correctAnswer as ca
import openwindow as ow
import wordRandInt as wri

def deleteAction(win):
    if hasattr(win, 'text_box'):
        try:
            win.text_box.delete("1.0", "end")
        except Exception:
            print("Failed to clear text box")

def wrongAnswerGiven(win):
    if not hasattr(win, "text_box"):
        print("No text_box on this window.")
        return
    
    raw = win.text_box.get("1.0", "end")
    userword = raw.strip()
    print("USERWORD:", repr(userword))

    correct = getattr(win, "current_word", None)
    print("CURRENT_WORD:", repr(correct))

    if correct is None:
        print("No current word set. Press Generate first.")
        return


    if userword.lower() == correct.lower():
        print("MATCHED! Correct answer.")
        ca.correctAnswerRendered(win)   
        ca.resetWindow(win)
    elif userword.lower() == "":
        wa.noAnswer(win)
    else:
        print("NOT MATCHED.")
        wa.renderWrongAnswer(win)

def destroyWindowContents(parent):
    win = parent
    for widget in win.winfo_children():
        widget.destroy()
    wri.resetWordInt()
    ow.generate_word(parent) 
    submitButtonPressedCount = 0
    wa.resultLabelInt = 0
    print("SubmitButtonCOunt = ", submitButtonPressedCount)
    print(wa.resultLabelInt)

          