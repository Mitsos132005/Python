import tkinter
window = tkinter.Tk()
window.title("First Canvas")
window.geometry("400x400")
canv = tkinter.Canvas(window, bg="white", height=200, width=200)
canv.pack()
canv.create_rectangle(50, 20, 150, 80, outline="black",fill="#ffd343", width=3)
canv.create_rectangle(65, 35, 135, 65, outline="black",fill="pink", width=3)
canv.create_line(0, 0, 50, 20, fill="black", width=3)
canv.create_line(0, 100, 50, 80, fill="black", width=3)
canv.create_line(150, 20, 200, 0, fill="black", width=3)
canv.create_line(150, 80, 200, 100, fill="black", width=3)
window.configure(background="aqua")
window.mainloop()
