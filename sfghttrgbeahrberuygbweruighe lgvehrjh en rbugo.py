import tkinter
window = tkinter.Tk()
lbl = tkinter.Label(window, text="Degrees Converter 6000")
lbl.pack()
txt = tkinter.Entry(window, width=10)
txt.pack()
def C():
    c = text= int(txt.get())*1.8+32
    print(c)
btn = tkinter.Button(window, text="Convert to Celsius", command=C)
btn.pack()
window.mainloop()
