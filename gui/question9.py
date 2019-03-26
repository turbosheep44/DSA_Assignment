import logic.question9 as nine
import logic.tools as tools

import random
import timeit

import tkinter as tk
from tkinter import ttk


def findPairs(largest, smallest, length, outputField):
    array = tools.randomArray(smallest, largest, length)
    
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, array.__str__())
    outputField.insert(tk.END, "\n\nThe duplicates are:")

    pairs = nine.getDuplicates(array)
    outputField.insert(tk.END, "\n\t" + pairs.__str__())


def makeGUI(window):

    root = ttk.Frame(window)
    
    tk.Label(root, text="Parameters for random array:").pack(pady=10)
    inputFields = tk.Frame(root, height = 50)
    inputFields.pack(fill= tk.X, pady=10)
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

    button = tk.Button(root, text="Generate array and find duplicates",
                       command=lambda: findPairs(int(maxNumber.get()), int(minNumber.get()) ,int(length.get()),  outputField))
    button.pack(pady=10)

    tk.Label(root, text="output:").pack()
    outputField.pack(expand=1, fill=tk.X, pady=10)

    return root
