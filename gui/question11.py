import logic.question11 as eleven
import traceback

import math
import sys

import tkinter as tk
from tkinter import ttk


def findPairs(value, iterations,cosine, outputField):
    
    outputField.delete(1.0, tk.END)

    try:
        if cosine:
            outputField.insert(tk.END, "cos(" + str(value) + ") = " + str(eleven.cosine(value, iterations)))
            outputField.insert(tk.END, "\nusing math.cos\ncos(" + str(value) + ") = " + str(math.cos(value)))
        else:
            outputField.insert(tk.END, "sine(" + str(value) + ") = " + str(eleven.sine(value, iterations)))
            outputField.insert(tk.END, "\nusing math.sin\nsin(" + str(value) + ") = " + str(math.sin(value)))
    except Exception as e:
            outputField.insert(tk.END, "Unexpected error: " + type(e).__name__)
        



def makeGUI(window):

    root = ttk.Frame(window)
    
    tk.Label(root, text="Parameters for series expansion:").pack(pady=10)
    inputFields = tk.Frame(root, height = 50)
    inputFields.pack(fill= tk.X, pady=10)
    tk.Label(inputFields, text="argument in radians: ").pack(side=tk.LEFT)
    argument = tk.Entry(inputFields)
    argument.pack(side=tk.LEFT)
    tk.Label(inputFields, text="summations to perform: ").pack(side=tk.LEFT)
    iterations = tk.Entry(inputFields)
    iterations.pack(side=tk.LEFT)

    outputField = tk.Text(root)

    tk.Label(root, text="Suggested > 100 iterations, however too many iterations produces an overflow error betcase the factorial becomes too large").pack(pady=10)

    buttonCosine = tk.Button(root, text="cosine",
                       command=lambda: findPairs(float(argument.get()) ,int(iterations.get()), True,  outputField))
    buttonCosine.pack(pady=10)
    buttonSine = tk.Button(root, text="sine",
                       command=lambda: findPairs(float(argument.get()) ,int(iterations.get()), False,  outputField))
    buttonSine.pack(pady=10)

    tk.Label(root, text="output:").pack()
    outputField.pack(expand=1, fill=tk.X, pady=10)

    return root
