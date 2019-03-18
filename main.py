
import tkinter as tk
from tkinter import ttk
import gui.question8 as q8

win = tk.Tk()
win.title("Python GUI")

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab1.pack()

tabControl.add(q8.makeGUI(win), text='Question 8')
tabControl.pack(expand=1, fill="both")
win.mainloop()
