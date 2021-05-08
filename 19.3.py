from tkinter import *

def fopen():
    fname = entry.get()
    f = open(fname)
    text.delete(1.0, END)
    text.insert(1.0, f.read)

def fsave():
    fname = entry.get()
    f = open(fname, 'x')
    f.write(text.get(1.0, END))
    text.delete(1.0, END)

root = Tk()

f1=Frame()
f1.pack
entry = Entry(f1, width=20)
entry.pack(side=LEFT)
Button(f1, text="Преобразовать")Открыть"Преобразовать"), command=file_load)\
 .pack(side=LEFT)

Button(f1, text="Преобразовать")Сохранить"Преобразовать"), command=file_save)\
75
 .pack(side=LEFT)

f2 = Frame()
f2.pack()
text = Text(f2, width=50, height=20, wrap=NONE)
text.pack(side=LEFT)
scroll = Scrollbar(f2, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

scroll2 = Scrollbar(orient=HORIZONTAL, command=text.xview)
scroll2.pack(side=BOTTOM, fill=X)
text.config(xscrollcommand=scroll2.set)

root.mainloop()
