
import logic.question6 as six

import tkinter as tk
from tkinter import ttk

def primeCheck(number, outputField):
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, str(number) + " is prime:\t" + six.primeCheck(number).__str__())

def sieve(number, outputField):
    outputField.delete(1.0, tk.END)
    outputField.insert(tk.END, "Primes up to and including:\t" + str(number) + "\n" + six.sieve(number).__str__())

def makeGUI(window):

    root = ttk.Frame(window)
    tk.Label(root, text="Enter a number to check if it is a prime:").pack()
    primeInput = tk.Entry(root)
    primeInput.pack()
    primeOutput = tk.Text(root, height=3, width=100)
    button = tk.Button(root, text="Prime Check",
                       command=lambda: primeCheck(int(primeInput.get()), primeOutput))
    button.pack()
    primeOutput.pack()

    tk.Label(root, text="Input a number to perform the sieve of eratosthenes").pack()
    sieveInput = tk.Entry(root)
    sieveInput.pack()
    sieveOutput = tk.Text(root, height=15, width=100)
    button = tk.Button(root, text="Sieve for primes",
                       command=lambda: sieve(int(sieveInput.get()), sieveOutput))
    button.pack()
    sieveOutput.pack()

    return root
