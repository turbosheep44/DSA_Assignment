


import logic.question4 as four
import logic.tools as tools

import random
import timeit

import tkinter as tk
from tkinter import ttk


def findPairs(largest, smallest, length, outputField):
    array = tools.randomArray(smallest, largest, length)
    
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, array.__str__())
    outputField.insert(tk.END, "\n\nThe pairs are:")

    pairs = four.findPairs(array)
    for pair in pairs:
        outputField.insert(tk.END, "\n\t" + pair.__str__())


def makeGUI(window):

    root = ttk.Frame(window)
    
    inputFields = tk.Frame(root, height = 50)
    inputFields.pack(fill= tk.X)
    tk.Label(inputFields, text="maximum: ").pack(side=tk.LEFT)
    maxNumber = tk.Entry(inputFields)
    maxNumber.pack(side=tk.LEFT)
    tk.Label(inputFields, text="minimum: ").pack(side=tk.LEFT)
    minNumber = tk.Entry(inputFields)
    minNumber.pack(side=tk.LEFT)
    tk.Label(inputFields, text="length: ").pack(side=tk.LEFT)
    length = tk.Entry(inputFields)
    length.pack(side=tk.LEFT)

    outputField = tk.Text(root)

    button = tk.Button(root, text="Generate array and find pairs",
                       command=lambda: findPairs(int(maxNumber.get()), int(minNumber.get()) ,int(length.get()),  outputField))
    button.pack()

    tk.Label(root, text="output:").pack()
    outputField.pack(expand=1, fill=tk.X)

    return root
