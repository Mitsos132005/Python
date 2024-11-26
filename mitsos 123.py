import tkinter
window = tkinter.Tk()
window.title("Commands")
def callback():
    lbl.configure(text="Button Clicked!")
lbl = tkinter.Label(window, text="Nothing  Happened Yet")
lbl.pack()
btn = tkinter.Button(window, text="CLICK ME", command=callback)
btn.pack()
window.mainloop()
