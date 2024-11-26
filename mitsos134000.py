import tkinter
window = tkinter.Tk()
lbl1 = tkinter.Label(window, text="Red Text in Times Font", fg = "red", font = "Times")
lbl2 = tkinter.Label(window, text="Green Text in Helvetica Font", fg = "light green", bg = "dark green", font = "Helvetica 16 bold italic")
lbl3=tkinter.Label(window, text="Blue Text in Verdana bold", fg = "blue", bg = "yellow", font = "Verdana 10 bold")
lbl1.pack()
lbl2.pack()
lbl3.pack()
window.mainloop()
