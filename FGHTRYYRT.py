import tkinter
window1 = tkinter.Tk()
window1.title("Main Window")
window1.geometry("200x200")
def openNewWindow():
    window2 = tkinter.Tk()
    window2.title("New Window")
    window2.geometry("200x200")
    lbl1= tkinter.Label(window2, text ="This is a new window")
    lbl1.pack()
    lbl2 = tkinter.Label(window1,text ="This is the main window")
    lbl2.pack()
btn = tkinter.Button(window1, text ="Click to open a new window", command = openNewWindow)
btn.pack()
window1.mainloop()

