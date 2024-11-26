import tkinter
window = tkinter.Tk()
window.title("Exitor 1000")
def hello():
    lbl = tkinter.Label(text="Hello")
    lbl.pack()
def close():
    window.destroy()
btn = tkinter.Button(window,text="Hello",command = hello)
btn.pack()
btn = tkinter.Button(window,text="Exit",command = close)
btn.pack()
window.mainloop()
