import tkinter
window = tkinter.Tk()
window.title("Backround Changer 2000")
def backgroundChangerPink():
    window.configure (bg = "pink")
btn = tkinter.Button(window, text="Make me Pink", command=backgroundChangerPink)
btn.pack()
def backgroundChangerYellow():
    window.configure (bg = "yellow") 
btn = tkinter.Button(window, text="Make me Yellow", command=backgroundChangerYellow)
btn.pack()
window.mainloop()
