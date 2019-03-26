

import tkinter as tk
from tkinter import ttk

from logic.question7 import Node


def addToTree(input, outputField, rootNode):
    print(rootNode.value)
    if rootNode.value is None:
        rootNode.value = float(input)
    else:
        rootNode.addNode(float(input))
    
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, rootNode.getDisplayString())


def reset(outputField, rootNode):
    rootNode.value = None
    rootNode.left = None
    rootNode.right = None
    outputField.delete(1.0, tk.END)


def makeGUI(window):
    rootNode = Node()
    root = ttk.Frame(window)
    label = tk.Label(root, text="Enter a number to add it to the tree:")
    label.pack()
    inputField = tk.Entry(root)
    inputField.pack()
    outputField = tk.Text(root, height=30, width=100)
    button = tk.Button(root, text="Add node", command=lambda: addToTree(inputField.get(), outputField, rootNode))
    button2 = tk.Button(root, text="Reset", command=lambda: reset(outputField, rootNode))
    button.pack()
    button2.pack()
    outputField.pack()

    return root
