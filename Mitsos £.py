import tkinter
window = tkinter.Tk()
window.title("Commands")
def callback():
    print("Button Clicked")
btn = tkinter.Button(window, text = "Click Me", command = callback)
btn.pack()
window.mainloop()
