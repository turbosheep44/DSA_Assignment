

import logic.question12 as twelve

import tkinter as tk
from tkinter import ttk

def getSum(number, outputField):
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, str(twelve.sumFibonnaci(number)))


def makeGUI(window):

    root = ttk.Frame(window)
    label = tk.Label(root, text="Enter a number to find the sum of the fibonnaci numbers up to that number:")
    label.pack()
    inputField = tk.Entry(root)
    inputField.pack()
    outputField = tk.Text(root, height=15, width=100)
    button = tk.Button(root, text="Find the sum of the first \'n\' fibonnaci numbers", command=lambda: getSum(int(inputField.get()), outputField))
    button.pack()
    outputField.pack()

    return root
