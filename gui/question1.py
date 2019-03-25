

import logic.question1 as one
import logic.tools as tools
import random
import timeit

import tkinter as tk
from tkinter import ttk

def sort(a_before, a_after, b_before, b_after, info):

    a = tools.randomArray(length = random.randint(256, 512))
    b = tools.randomArray(length = random.randint(256, 512))

    a_before.delete(1.0, tk.END)
    a_before.insert(tk.END, a.__str__())
    b_before.delete(1.0, tk.END)
    b_before.insert(tk.END, b.__str__())

    print(a)

    a_after.delete(1.0, tk.END)
    a_after.insert(tk.END, a.__str__())

    b_after.delete(1.0, tk.END)
    b_after.insert(tk.END, b.__str__()) 

    output = "Length of first array : " + len(a).__str__() + "\nLength of second array : " + len(b).__str__()
    info.delete(1.0, tk.END)
    info.insert(tk.END, output)



def makeGUI(window):

    root = ttk.Frame(window)
    tk.Label(root, text="First array before sorting:").pack()
    a_before = tk.Text(root,height=8)
    a_before.pack(fill=tk.X)
    tk.Label(root, text="Secong array before sorting:").pack()
    b_before = tk.Text(root,height=8)
    b_before.pack(fill=tk.X)

    a_after = tk.Text(root,height=8)
    b_after = tk.Text(root,height=8)
    info = tk.Text(root, height = 12)
    
    button = tk.Button(root, text="Generate and sort arrays",
                       command=lambda: sort(a_before, a_after, b_before, b_after, info))
    button.pack()
    
    tk.Label(root, text="First array after sorting:").pack()
    a_after.pack(fill=tk.X)
    tk.Label(root, text="Second array after sorting:").pack()
    b_after.pack(fill=tk.X)
    tk.Label(root, text="OUTPUT INFORMATION").pack()
    info.pack(fill=tk.X)



    return root