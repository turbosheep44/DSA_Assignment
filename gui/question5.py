

import logic.question5 as five

import tkinter as tk
from tkinter import ttk

def parseRPN(inputString, outputField):
    outputString = five.parseExpressionStringOutput(inputString)

    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, "expression: "+ inputString + "\n\n")
    outputField.insert(tk.END, outputString)
    
    return 0


def makeGUI(window):

    root = ttk.Frame(window)
    label = tk.Label(root, text="Enter an RPM expression to evaluate, each input value and operator should be separated by a space:")
    label.pack()
    inputField = tk.Entry(root)
    inputField.pack()
    outputField = tk.Text(root, height=25)
    button = tk.Button(root, text="Parse",
                       command=lambda: parseRPN(inputField.get(), outputField))
    button.pack()
    outputField.pack(fill=tk.X)

    return root
