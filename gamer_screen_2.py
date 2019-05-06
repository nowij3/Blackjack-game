import tkinter
from tkinter import Image

window=tkinter.Tk()
window.title("BlackJack Game")
window.geometry("640x400+100+100")
window.resizable(True, True)


a1=tkinter.Button(window, text="Deal")
a2=tkinter.Button(window, text="Hit")
a3=tkinter.Button(window, text="Stand")
a4=tkinter.Button(window, text="New Hand")
a5=tkinter.Button(window, text="1000", command=lambda:chip_pressed('1000'))
a6=tkinter.Button(window, text="500", command=lambda:chip_pressed('500'))
a7=tkinter.Button(window, text="200", command=lambda:chip_pressed('200'))
a8=tkinter.Label(window, text="Balance :")
a9=tkinter.Button(window, text="New Game")
p1=tkinter.Label(window, text="Dealer", bg="white")
p2=tkinter.Label(window, text="Player1", bg="white")
p3=tkinter.Label(window, text="Player2", bg="white")

a1.place(x=150, y=300, width=90, height=50)
a2.place(x=300, y=300, width=90, height=50)
a3.place(x=450, y=300, width=90, height=50)
a4.place(x=20, y=50, width=80, height=30)
a5.place(x=20, y=90, width=50, height=50)
a6.place(x=20, y=150, width=50, height=50)
a7.place(x=20, y=210, width=50, height=50)
a8.place(x=20, y=320, width=50, height=30)
a9.place(x=20, y=10, width=80, height=30)
p1.place(x=300, y=25, width=70, height=30)
p2.place(x=120, y=150, width=70, height=30)
p3.place(x=500, y=150, width=70, height=30)

def chip_pressed(value):

    if not num_entry.get() == '':
        v = int(value)
        v += int(num_entry.get())
        # value += int(num_entry.get())
        num_entry.delete(0,'end')
        num_entry.insert("end", str(v))
    else:
        num_entry.insert("end", value)
    print(value,"pressed")
    # print(int(num_entry.get()))


entry_value=tkinter.StringVar(window, value='')

num_entry=tkinter.Entry(window, textvariable=entry_value, width=10)
num_entry.grid(row=0, columnspan=1)
num_entry.place(x=20, y=290)


window.mainloop()
