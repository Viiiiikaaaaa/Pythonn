import random
from tkinter import *
from tkinter import ttk
labels =[]
size = 10

def generate():
    global labels
    for i in range(size):
        labels.append(random.randrange(-100, 100))


btn_generate = Button(text = 'Сгенерировать массив', command=generate)

def sort():
    global labels
    for i in range(0, size - 1):
        for j in range(i, size - 1):
            if labels[j + 1] < labels[i]:
                temp = labels[i]
                labels[i] = labels[j + 1]
                labels[j + 1] = temp
    for i in labels:
        lbl = Label(text = str(i))
        lbl.pack()

btn_sort = Button(text = 'Сортировка', command = sort)

asd= Tk()
asd.geometry="300x250"

btn_generate.pack()
btn_sort.pack()

asd.mainloop()
