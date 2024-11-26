import tkinter
window= tkinter.Tk()
window.title("Login")
un = "Mitsos132005"
pw = "123"
def clicked():
    if txt1.get() == un:
        print("Correct Username")
    else:
        print("Wrong Username")
    if txt2.get() == pw:
        print("Correct Password")
    else:
        print("Wrong Passwrod")
lbl1 = tkinter.Label(window, text="Username")
lbl1.pack()
txt1 = tkinter.Entry(window,width=10)
txt1.pack()
lbl2 = tkinter.Label(window, text="Password")
lbl2.pack()
txt2 = tkinter.Entry(window,show = "*", width=10)
txt2.pack()
button1 = tkinter.Button(text="Login", command=clicked)
button1.pack()
window.mainloop()
