

import logic.question8 as eight

import tkinter as tk
from tkinter import ttk

def findSqrt(inputField, outputField):
    i = float(inputField.get())
    output = eight.main(i)
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, "Target:\t")
    outputField.insert(tk.END, str(i))
    outputField.insert(tk.END, "\n\nSquare Root:\t")
    outputField.insert(tk.END, str(output[eight.SOLUTION]))
    outputField.insert(tk.END, "\n\nIterations:\t")
    outputField.insert(tk.END, str(output[eight.ITERATIONS]))
    outputField.insert(tk.END, "\n\nSolution square:\t")
    square = output[eight.SOLUTION] ** 2
    outputField.insert(tk.END, str(square))

    outputField.insert(
        tk.END, "\n\nDifference between solution square and target:\t")
    outputField.insert(tk.END, str(square - i))

    if output[eight.PATTERN_EXISTS]:
        outputField.insert(
            tk.END, "\n\nStopped early because a pattern was found...\n\t")
        outputField.insert(tk.END, str(output[eight.PATTERN]))


def makeGUI(window):

    root = ttk.Frame(window)
    label = tk.Label(root, text="Enter a number to find the it's square root:")
    label.pack()
    inputField = tk.Entry(root)
    inputField.pack()
    outputField = tk.Text(root, height=15, width=100)
    button = tk.Button(root, text="Find square root",
                       command=lambda: findSqrt(inputField, outputField))
    button.pack()
    outputField.pack()

    return root
