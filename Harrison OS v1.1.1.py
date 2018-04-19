#TK REFRESH IS NOT FUNCTIONAL // DO NOT USE THE "U" TKINTER WIDGET // USING THE WIDTGET WILL CRASH THE PROGRAM // TKINTER REQUIRES PROPER MAINLOOP FUNCTION // WILL BE IMPROVED IN (Harrison OS v1.2.0) AS AN UPDATE.

import webbrowser
import tkinter
import random
import turtle
import time
import os
from tkinter import *

w1 = 1600
h1 = 800

stage = 0
stage_ws = 0
updates = 0
rf1 = 0
screen1_bg = "gray"
app_bg = "black"
createnew1 = 0
setting_stage = 0

'''root = Tk()
root.title("Harrison OS v(1.1.0)")
root.minsize(width = w1, height = h1)
root.maxsize(width = w1, height = h1)'''

def c1():
    exit()

def c2():
    global stage_ws
    if (stage_ws == 0):
        stage_ws = 1
        w = 800
        h = 400
    elif (stage_ws == 1):
        stage_ws = 0
        w = 1600
        h = 800
    main()

def c3():
    root = Tk()
    root.title("Harrison OS Error")
    root.minsize(width = 150, height = 30)
    root.maxsize(width = 150, height = 30)
    item1 = Label(root, text = "Error - Operation failed", bg = "red").grid(row = 1, column = 0)

def c4():
    global rf1
    global updates
    if (rf1 == 0):
        rf1 = 1
    elif (rf1 == 1):
        rf1 = 0

    while (rf1 == 1):
        main()
        updates = (float(updates) + 1)

def c5():
    global stage
    stage = 1
    main()

def c6():
    global stage
    stage = 0
    main()

def c7():
    global setting_stage
    setting_stage = 1
    main()
    
def c8():
    global setting_stage
    setting_stage = 2
    main()
    
def c9():
    global setting_stage
    setting_stage = 3
    main()
    
def c10():
    global setting_stage
    setting_stage = 4
    main()

def c11():
    global app_bg
    app_bg = "black"
    main()

def c12():
    global app_bg
    app_bg = "white"
    main()

def c13():
    global app_bg
    app_bg = "blue"
    main()

def c14():
    global app_bg
    app_bg = "green"
    main()

def c15():
    global app_bg
    app_bg = "orange"
    main()

def c16():
    global app_bg
    app_bg = "red"
    main()

def c17():
    global app_bg
    app_bg = "purple"
    main()

def main():
    global stage
    global screen1_bg
    global app_bg
    global setting_stage
    
    root = Tk()
    root.title("Harrison OS v(1.1.0)")
    root.minsize(width = w1, height = h1)
    root.maxsize(width = w1, height = h1)
    b1 = Button(root, text = "    X    ", activebackground = "red", bg = "gray", command = c1).grid(row = 1, column = 1)
    b2 = Button(root, text = "   [ ]   ", bg = "gray", command = c2).grid(row = 1, column = 2)
    b3 = Button(root, text = "    U    ", bg = "gray", command = c4).grid(row = 1, column = 3)
    b4 = Button(root, text = "    H    ", bg = "gray", command = c6).grid(row = 1, column = 4)
    b5 = Label(root, text = "   ").grid(row = 1, column = 5)
    b6 = Label(root, text = ("Stage ", stage)).grid(row = 1, column = 6)

    if (stage == 0):
        screen1 = Canvas(height = (float(h1) - (float(h1) / 4)), width = (float(w1) - (float(w1) / 6.5)), bg = screen1_bg).grid(row = 3, column = 0)
        item1 = Label(root, text = " ").grid(row = 4, column = 0)
        item2 = Button(root, text = "Settings", bg = app_bg, fg = "white", command = c5).grid(row = 5, column = 0)
        
    if(stage == 1):
        spacer1 = Label(root, text = " ").grid(row = 1, column = 7)
        item1 = Button(root, text = "Colors", bg = app_bg, fg = "white", command = c7).grid(row = 3, column = 0)
        item2 = Button(root, text = "Variables", bg = app_bg, fg = "white", command = c8).grid(row = 3, column = 1)
        item3 = Button(root, text = "Runtime", bg = app_bg, fg = "white", command = c9).grid(row = 3, column = 2)
        item4 = Button(root, text = "System info", bg = app_bg, fg = "white", command = c10).grid(row = 3, column = 3)
        if (setting_stage == 1):
            spacer1 = Label(root, text = " ").grid(row = 4, column = 4)
            item5 = Label(root, text = ("Defualt button color is ", app_bg)).grid(row = 5, column = 0)
            item6 = Button(root, text = "Set default color to black", bg = "black", fg = "white", command = c11).grid(row = 6, column = 0)
            item7 = Button(root, text = "Set default color to white", bg = "black", fg = "white", command = c12).grid(row = 6, column = 1)
            item8 = Button(root, text = "Set default color to blue", bg = "black", fg = "white", command = c13).grid(row = 6, column = 2)
            item9 = Button(root, text = "Set default color to green", bg = "black", fg = "white", command = c14).grid(row = 6, column = 3)
            item10 = Button(root, text = "Set default color to orange", bg = "black", fg = "white", command = c15).grid(row = 6, column = 4)
            item11 = Button(root, text = "Set default color to red", bg = "black", fg = "white", command = c16).grid(row = 6, column = 5)
            item12 = Button(root, text = "Set default color to purple", bg = "black", fg = "white", command = c17).grid(row = 6, column = 6)
            
        if (setting_stage == 2):
            spacer1 = Label(root, text = " ").grid(row = 4, column = 4)
            
        if (setting_stage == 3):
            spacer1 = Label(root, text = " ").grid(row = 4, column = 4)
            
        if (setting_stage == 4):
            spacer1 = Label(root, text = " ").grid(row = 4, column = 4)
    root.mainloop()
        

main()

root = Tk()
root.title("Harrison OS Quitboard")
root.minsize(width = 200, height = 75)
root.maxsize(width = 200, height = 75)
item1 = Button(root, text = "Quit all?", command = c1, bg = "red", width = 200, height = 40).grid(row = 1, column = 0)
