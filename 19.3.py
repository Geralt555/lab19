#!/usr/bin/env python3
# -*- config: utf-8 -*-

# напишите программу, состоящую из однострочного и многострочного
# текстовых полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
# открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
# должно загружаться в поле типа Text .

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

f1 = Frame()
f1.pack()
entry = Entry(f1, width=20)
entry.pack(side=LEFT)


def file_load():
    pass


Button(f1, text="Открыть", command=file_load) \
    .pack(side=LEFT)


def file_save():
    pass


Button(f1, text="Сохранить", command=file_save) \
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
