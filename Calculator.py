from tkinter import *
from tkinter import ttk

def btn_click_add():
    n1 = int(entry_n1.get())
    n2 = int(entry_n2.get())
    lbl_result["text"] = str(n1+n2)

def btn_click_subtr():
    n1 = int(entry_n1.get())
    n2 = int(entry_n2.get())
    lbl_result["text"] = str(n1-n2)

def btn_click_mult():
    n1 = int(entry_n1.get())
    n2 = int(entry_n2.get())
    lbl_result["text"] = str(n1*n2)

root = Tk()
root.title("Название")
root.geometry("640x480")
lbl_name = Label(text="Калькулятор")
lbl_name.pack()
lbl_result = Label(text="Результат")
lbl_result.pack()

entry_n1 = ttk.Entry()
entry_n1.pack()
entry_n2 = ttk.Entry()
entry_n2.pack()

btn_change_label_add = Button(text = "+", command = btn_click_add)
btn_change_label_add.pack()

btn_change_label_subtr = Button(text="-", command = btn_click_subtr)
btn_change_label_subtr.pack()

btn_change_label_mult = Button(text="*", command = btn_click_mult)
btn_change_label_mult.pack()

root.mainloop()