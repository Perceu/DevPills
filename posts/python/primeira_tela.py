"""
Criando uma telinha com python
"""
from tkinter import Tk
from tkinter import ttk

root = Tk()
root.title = "Olá mundo!"
frm = ttk.Frame(root, padding=50)

frm.grid()

ttk.Label(frm, text="Bem vindo! ao python").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)

root.mainloop()