


import logic.question1 as one
import logic.question2 as two
import logic.tools as tools

import random
import timeit

import tkinter as tk
from tkinter import ttk

def sort(a, b, merge):

    aArray = tools.randomArray(length = random.randint(256, 512))
    bArray = tools.randomArray(length = random.randint(256, 512))

    one.quicksort(aArray)
    one.shellsort(bArray)
    mergeArray = two.merge(aArray[:], bArray[:])

    a.delete(1.0, tk.END)
    a.insert(tk.END, aArray.__str__())
    b.delete(1.0, tk.END)
    b.insert(tk.END, bArray.__str__())

    merge.delete(1.0, tk.END)
    merge.insert(tk.END, mergeArray.__str__())
    



def makeGUI(window):

    root = ttk.Frame(window)
    tk.Label(root, text="First array (sorted with quicksort):").pack()
    a = tk.Text(root,height=8)
    a.pack(expand=1,fill=tk.X)
    tk.Label(root, text="Secong array (sorted with shellsort):").pack()
    b = tk.Text(root,height=8)
    b.pack(expand=1,fill=tk.X)

    merge = tk.Text(root,height=8)
    
    button = tk.Button(root, text="Generate and sort arrays",
                       command=lambda: sort(a, b, merge))
    button.pack()
    
    tk.Label(root, text="Merged arrays:").pack()
    merge.pack(expand=1, fill=tk.X)



    return root