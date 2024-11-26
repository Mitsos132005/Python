import tkinter
window = tkinter.Tk()
window.title("Welcome to EEB3")
window.geometry('350x200')
lbl = tkinter.Label(window, text="Hello")
lbl.pack()
txt = tkinter.Entry(window,width=10)
txt.pack()
def clicked():
    a = "Welcome to " + txt.get()
    lbl.configure(text= a)
btn = tkinter.Button(window, text="Click Me", command=clicked)
btn.pack()
window.mainloop()
