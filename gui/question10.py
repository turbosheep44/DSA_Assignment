import logic.question10 as ten
import logic.tools as tools

import random
import timeit

import tkinter as tk
from tkinter import ttk

def getArray(largest, smallest, length):
    return tools.randomArray(smallest, largest, length)

def findPairs(array, outputField):
    
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, array.__str__())
    outputField.insert(tk.END, "\n\nThe largest number is:")

    largest = ten.findLargest(array)
    outputField.insert(tk.END, "\n\t" + str(largest))


def makeGUI(window):

    root = ttk.Frame(window)
    
    tk.Label(
        root, text="Enter a list of numbers, with each element separated by a comma:").pack()
    arrayInput = tk.Text(root, height=5)
    arrayInput.pack(expand=1, fill=tk.X)

    button = tk.Button(root, text="Find largest",
                       command=lambda: findPairs([float(x.strip(' ')) for x in arrayInput.get(1.0, tk.END).strip('\n').strip(' ').split(",")],  outputField))
    button.pack(pady=10)

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

    button = tk.Button(root, text="Generate array and find largest",
                       command=lambda: findPairs(getArray(int(maxNumber.get()), int(minNumber.get()), int(length.get())),  outputField))
    button.pack(pady=10)

    tk.Label(root, text="output:").pack()
    outputField.pack(expand=1, fill=tk.X, pady=10)

    return root
