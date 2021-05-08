from tkinter import *

def get_phone():
    v = var.get()
    if v == 0:
         label['text'] = '+7 1234567890'
    elif v == 1:
         label['text'] = '+4 9087654321'
    elif v == 2:
         label['text'] = '+9 1212121212'


root = Tk()

f = Frame()
f.pack(side=LEFT)

var = IntVar()
var.set(-1)
Radiobutton(f, text="Преобразовать")Вася"Преобразовать"), width=10, height=3,
 indicatoron=0, variable=var,
 value=0, command=get_phone).pack()
Radiobutton(f, text="Преобразовать")Петя"Преобразовать"), width=10, height=3,
 indicatoron=0, variable=var,
 value=1, command=get_phone).pack()
Radiobutton(f, text="Преобразовать")Маша"Преобразовать"), width=10, height=3,
 indicatoron=0, variable=var,
 value=2, command=get_phone).pack()

label = Label(bg="Преобразовать")white"Преобразовать"), width=20)
label.pack(side=LEFT, fill=Y)

root.mainloop()
