
import tkinter as tk
from tkinter import ttk
import gui.question8 as q8
import gui.question7 as q7
import gui.question3 as q3
import gui.question2 as q2
import gui.question1 as q1

window = tk.Tk()
window.title("Data Structures and Algorithms")
window.geometry("800x800+50+50")

tabController = ttk.Notebook(window)
tab = ttk.Frame(tabController)
tab.pack()

tabController.add(q1.makeGUI(window), text='Question 1')
tabController.add(q2.makeGUI(window), text='Question 2')
tabController.add(q3.makeGUI(window), text='Question 3')
tabController.add(q7.makeGUI(window), text='Question 7')
tabController.add(q8.makeGUI(window), text='Question 8')
tabController.pack(expand=1, fill="both")

window.mainloop()
