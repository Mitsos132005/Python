import tkinter
import random
window = tkinter.Tk()
def dice():
    rolled = random.randint(1,6)
    lbl2.configure(text=rolled)
lbl1 = tkinter.Label(text="Roll the Dice")
lbl1.pack()
btn = tkinter.Button(text="Roll",command=dice)
btn.pack()
lbl2 = tkinter.Label(window)
lbl2.pack()
window.mainloop()
