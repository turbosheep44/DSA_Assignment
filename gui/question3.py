


import logic.question3 as three
import logic.tools as tools

import random
import timeit

import tkinter as tk
from tkinter import ttk

def checkSorted(inputString, outputField):

    array = [ float(x.strip(' ')) for x in inputString.strip('\n').strip(' ').split(",") ]
    extremePoints = three.findExtremes(array)

    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, array.__str__())
    outputField.insert(tk.END, "\n")
    if len(extremePoints) == 0:
        outputField.insert(tk.END, "SORTED")
    else:
         for p in extremePoints:
                outputField.insert(tk.END, "extreme point at index :")
                outputField.insert(tk.END, p)
                outputField.insert(tk.END, "\n")
    



def makeGUI(window):

    root = ttk.Frame(window)
    tk.Label(root, text="Enter a list of numbers, with each element separated by a comma:").pack()
    inputField = tk.Text(root,height=5)
    inputField.pack(expand=1,fill=tk.X)

    outputField = tk.Text(root,height=3)
    
    button = tk.Button(root, text="Find extreme points",
                       command=lambda: checkSorted(inputField.get(1.0, tk.END), outputField))
    button.pack()
    
    tk.Label(root, text="output:").pack()
    outputField.pack(expand=1, fill=tk.X)



    return root