import tkinter
import random
window = tkinter.Tk()
lbl1 = tkinter.Label(text="Guess a Number Between 0 and 10")
lbl1.pack()
ent1 = tkinter.Entry(window, width = 10)
ent1.pack()
number = random.randint(0,10)
lbl2 = tkinter.Label(window)
lbl2.pack()
def BruteForce():
    y = int(ent1.get())
    if y == number:
        lbl2.configure(text="You are Correct")
    if y < number:
        lbl2.configure(text="Too Low")
    if y > number:
        lbl2.configure(text="Too High")
btn1 = tkinter.Button(window, text ="Start", command = BruteForce)
btn1.pack()
window.mainloop()

