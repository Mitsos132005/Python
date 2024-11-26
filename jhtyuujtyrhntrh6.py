import tkinter
window= tkinter.Tk()
window.geometry("300x300")
ent1 = tkinter.Entry (window)
ent1.pack()
def getSquareRoot ():
    x1 = ent1.get()
    label1 = tkinter.Label(window, text= int(x1)**0.5)
    label1.pack()
button1 = tkinter.Button(text='Get the Square Root', command=getSquareRoot)
button1.pack()
window.mainloop ()
