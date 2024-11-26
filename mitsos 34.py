import tkinter
window = tkinter.Tk()
window.title("Commands")
presses = 0
def addClick():
    global presses
    presses += 1
    lbl.configure(text=presses)
lbl = tkinter.Label(window, text=presses)
lbl.pack()
btn = tkinter.Button(window, text="Click Me", command=addClick)
btn.pack()
window.mainloop()
