import webbrowser
import tkinter
import random
import turtle
import time
import os
from tkinter import *

h1 = 900
w1 = 1800

root = Tk()
root.title("Harrison OS v(1.0.0)")
root.minsize(width = w1, height = h1)
root.maxsize(width = w1, height = h1)

def c1():
    exit()

def nc():
    root = Tk()
    root.title("Error")
    root.minsize(width = 200, height = 75)
    root.maxsize(width = 200, height = 75)
    p1 = Label(root, text = "There is no such command!", fg = "red").grid(row = 1, column = 0)
    p2 = Button(root, text = "   Ok   ", command = None).grid(row = 2, column = 0)

def runos():
    fsp01 = Label(root, text = " ").grid(row = 1, column = 0)
    item1 = Button(root, bg = "gray", activebackground = "red", text = "   X   ", command = c1).grid(row = 1, column = 3)
    item2 = Button(root, bg = "gray", text = "  [ ]  ", command = nc).grid(row = 1, column = 2)
    item3 = Button(root, bg = "gray", text = "   -   ", command = nc).grid(row = 1, column = 1)
    fsp02 = Label(root, text = " ").grid(row = 2, column = 0)
    item4 = Canvas(root, bg = "gray", width = 1400, height = 600).grid(row = 3, column = 0)
    root.mainloop()
    
runos()
