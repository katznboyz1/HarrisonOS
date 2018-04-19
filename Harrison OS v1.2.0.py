#THIS SCRIPT WAS WRITTEN BT HARRISON LINDGREN (harrison.lindgren@gmail.com) AND BELONGS TO HIM. UNAUTHORIZED DISTRIBUTION OF THIS SOFTWARE IS ILLEGAL.

#TO DO: Make an option to change the desktop color and taskbar color in the settings menu

import webbrowser
import tkinter
import turtle
import random
import time
import os
from tkinter import *

root = Tk()
root.title("Harrison OS V1.2.0 BETA")
root.maxsize(width = 1580, height = 800)
root.minsize(width = 1580, height = 800)
root.configure(bg = "lightgray")

notepad_document1 = "No current entry."
should_update = 1
dktp_bgnd = "gray"
max_run = 500
update = 0
stage = "home"
updates = 0
now = time.localtime(time.time())
ttl = 0

taskbar_color = "blue"

def c1():
    root.destroy()
    exit()

def c2():
    root.update()
    global updates
    updates = float(updates) + 1

def c3():
    global stage
    global updates
    updates = float(updates) + 1
    stage = "home"
    main()

def c4():
    global stage
    global updates
    updates = float(updates) + 1
    stage = "calculator"
    main()

def c5():
    global stage
    global updates
    updates = float(updates) + 1
    stage = "settings_tfr"
    main()

def c6():
    global stage
    stage = "Security and privacy"

def c7():
    global stage
    stage = "Colors and layout"

def c8():
    global stage
    stage = "System preferences"

def c9():
    global stage
    stage = "Date and time"
    
def c10():
    global stage
    stage = "System info/software status"

def c11():
    global dktp_bgnd
    dktp_bgnd = "orange"

def c12():
    global dktp_bgnd
    dktp_bgnd = "gray"

def c13():
    global dktp_bgnd
    dktp_bgnd = "purple"

def c14():
    global dktp_bgnd
    dktp_bgnd = "red"

def c15():
    global dktp_bgnd
    dktp_bgnd = "black"

def c16():
    global dktp_bgnd
    dktp_bgnd = "blue"

def c17():
    global stage
    stage = "System policy and copyright info"

def c18():
    global should_update
    if (should_update == 1):
        should_update = 0

        root = Tk()
        root.title("Harrison OS Error")
        root.maxsize(width = 310, height = 25)
        root.minsize(width = 310, height = 25)
        root.configure(bg = "red")
        item1 = Button(root, text = "FATAL ERROR - THE PROGRAM HAS STOPPED WORKING", bg = "red", command = c1)
        item1.place(x = 0, y = 0)
        
    elif (should_update == 0):
        should_update = 1

def c19():
    global dktp_bgnd
    dktp_bgnd = "white"

def c20():
    global stage
    global dktp_bgnd
    global notepad_document1

    def retrieve_input():
        global notepad_document1
        notepad_document1 = wordbox.get()

    def c23():
        root.destroy()
    
    root = Tk()
    root.title("Harrison OS Notepad Extension")
    root.minsize(width = 400, height = 200)
    root.minsize(width = 400, height = 200)
    root.configure(bg = dktp_bgnd)
    notice1 = Label(root, text = "Write your document below:", bg = dktp_bgnd)
    notice1.place(x = 0, y = 0)
    wordbox = Entry(root, width = 200)
    wordbox.place(x = 0, y = 20)
    savebutton = Button(root, text = "Save", bg = "black", fg = "white",command=lambda: retrieve_input())
    savebutton.place(x = 0, y = 40)
    item1 = Button(root, text = "    X    ", bg = "gray", activebackground = "red", command = c23)
    item1.place(x = 0, y = 70)
#    stage = "Notepad"

def c21():
    global stage
    stage = "System policy and copyright info"

def c22():
    global stage
    stage = "Variable checks"

def c24():
    global now
    print (now)

def main():
    global max_run
    global update
    global stage
    global taskbar_color
    global now
    global dktp_bgnd
    global updates
    global should_update
    global ttl
    global notepad_document1

    start = time.time()

    now = time.localtime(time.time())
    
    item1 = Button(root, text = "    X    ", bg = "gray", activebackground = "red", command = c1)
    item2 = Button(root, text = "   [ ]   ", bg = "gray", command = None)
    item3 = Button(root, text = "    R    ", bg = "gray", command = c2)
    item4 = Label(root, text = (" ", updates, " Total system updates."))
    item1.place(x = 0, y = 0)
    item2.place(x = 50, y = 0)
    item3.place(x = 100, y = 0)
    item4.place(x = 150, y = 0)

#--------------------------------------------------------------------------------------------------------------------------------------APP DEFINITIONS BELOW

    if (stage == "home"):
        item5 = Canvas(root, width = 1575, height = 720, bg = dktp_bgnd)
        item5.place(x = 0, y = 30)
        
    elif (stage == "settings_tfr"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        stage = "settings_mim"
        
    elif (stage == "settings_mim"):
        item6 = Label(root, text = "Settings main menu:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Button(root, text = "Security and privacy", bg = "black", fg = "white", command = c6)
        item7.place(x = 10, y = 70)
        item8 = Button(root, text = "Colors and layout", bg = "black", fg = "white", command = c7)
        item8.place(x = 10, y = 100)
        item9 = Button(root, text = "System preferences", bg = "black", fg = "white", command = c8)
        item9.place(x = 10, y = 130)
        item10 = Button(root, text = "Date and time", bg = "black", fg = "white", command = c9)
        item10.place(x = 10, y = 160)
        item11 = Button(root, text = "System info/software status", bg = "black", fg = "white", command = c10)
        item11.place(x = 10, y = 190)
        
    elif (stage == "Security and privacy"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "Security and privacy menu:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Button(root, text = "System policy and copyright info", bg = "black", fg = "white", command = c17)
        item7.place(x = 10, y = 70)
        
    elif (stage == "Colors and layout"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "Colors and layout menu:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Label(root, text = ("Desktop background = ", dktp_bgnd), bg = "lightgray")
        item7.place(x = 10, y = 70)
        item8 = Button(root, text = "Change desktop background to orange", bg = "orange", fg = "white", command = c11)
        item8.place(x = 200, y = 70)
        item9 = Button(root, text = "Change desktop background to gray", bg = "gray", fg = "white", command = c12)
        item9.place(x = 200, y = 100)
        item10 = Button(root, text = "Change desktop background to purple", bg = "purple", fg = "white", command = c13)
        item10.place(x = 200, y = 130)
        item11 = Button(root, text = "Change desktop background to red", bg = "red", fg = "white", command = c14)
        item11.place(x = 200, y = 160)
        item12 = Button(root, text = "Change desktop background to black", bg = "black", fg = "white", command = c15)
        item12.place(x = 200, y = 190)
        item13 = Button(root, text = "Change desktop background to blue", bg = "blue", fg = "white", command = c16)
        item13.place(x = 200, y = 220)
        item14 = Button(root, text = "Change desktop background to white", bg = "white", fg = "black", command = c19)
        item14.place(x = 200, y = 250)
        
    elif (stage == "System preferences"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "System preferences menu:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Checkbutton(root, text = "Disable refresh (CAUTION - THIS WILL COMPLETELY PAUSE THE PROGRAM // THIS ACTION CAN NOT BE UNDONE)", bg = "lightgray", command = c18)
        item7.place(x = 10, y = 70)
        
    elif (stage == "Date and time"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "Date and time menu:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Label(root, text = ("Current time is ", now), bg = "lightgray")
        item7.place(x = 10, y = 80)
        item8 = Label(root, text = "Time is represented in [YEAR-YEAR-YEAR-YEAR, MONTH-MONTH, DAY-DAY, HOUR-HOUR, MINUTE-MINUTE, SECOND-SECOND, DAY OF YEAR(0-365)]", bg = "lightgray")
        item8.place(x = 10, y = 110)

    elif (stage == "System info/software status"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "System information menu:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Label(root, text = ("Last runtime to complete one full mainloop() operation took ", ttl, " seconds."), bg = "lightgray")
        item7.place(x = 10, y = 70)
        item8 = Label(root, text = ("Total screen refreshes: ", updates, " Maximum amount of refreshes known is 0998.00 before stack overflow."), bg = "lightgray")
        item8.place(x = 10, y = 90)
        item9 = Button(root, text = "System policy and copyright info", bg = "black", fg = "white", command = c21)
        item9.place(x = 10, y = 110)
        item10 = Button(root, text = "View all variables and their definitions", bg = "black", fg = "white", command = c22)
        item10.place(x = 10, y = 140)

    elif (stage == "System policy and copyright info"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "System policy and copyright info menu:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Label(root, text = "User(s) of this computer:", bg = "lightgray")
        item7.place(x = 10, y = 70)
        item8 = Entry(root)
        item8.place(x = 160, y = 70)
        item9 = Label(root, text = "Current Harrison OS Version: V1.2.0", bg = "lightgray")
        item9.place(x = 10, y = 90)
        item10 = Label(root, text = "Harrison OS sotware is copyrighted, registered, and trademarked by Harrison Lindgren(harrison.lindgren@gmail.com) / Katznboyz", bg = "lightgray")
        item10.place(x = 10, y = 110)
        item11 = Label(root, text = "Current build version: V2", bg = "lightgray")
        item11.place(x = 10, y = 130)
        item12 = Label(root, text = "Current tidal version: V1", bg = "lightgray")
        item12.place(x = 10, y = 150)
        item13 = Label(root, text = "Software release date (MM-DD-YYYY): 12/26/2017", bg = "lightgray")
        item13.place(x = 10, y = 170)

    elif (stage == "Notepad"):
        stage = "home"

    elif (stage == "Variable checks"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "Variable list:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        item7 = Label(root, text = "Screen definition: 1580*800", bg = "lightgray")
        item7.place(x = 10, y = 70)
        item8 = Label(root, text = ("Stage: ", stage), bg = "lightgray")
        item8.place(x = 10, y = 90)
        item9 = Label(root, text = ("max_run: ", max_run), bg = "lightgray")
        item9.place(x = 10, y = 110)
        item10 = Label(root, text = ("update: ", update), bg = "lightgray")
        item10.place(x = 10, y = 130)
        item11 = Label(root, text = ("taskbar_color: ", taskbar_color), bg = "lightgray")
        item11.place(x = 10, y = 150)
        item12 = Label(root, text = ("now: ", now), bg = "lightgray")
        item12.place(x = 10, y = 170)
        item13 = Label(root, text = ("dktp_bgnd: ", dktp_bgnd), bg = "lightgray")
        item13.place(x = 10, y = 190)
        item14 = Label(root, text = ("updates: ", updates), bg = "lightgray")
        item14.place(x = 10, y = 210)
        item15 = Label(root, text = ("should_update: ", should_update), bg = "lightgray")
        item15.place(x = 10, y = 230)
        item16 = Label(root, text = ("ttl: ", ttl), bg = "lightgray")
        item16.place(x = 10, y = 250)
        item17 = Label(root, text = ("notepad_document1: ", notepad_document1), bg = "lightgray")
        item17.place(x = 10, y = 270)

    elif (stage == "calculator"):
        item5 = Canvas(root, width = 1575, height = 720, bg = "lightgray")
        item5.place(x = 0, y = 30)
        item6 = Label(root, text = "Calculator:", bg = "lightgray")
        item6.place(x = 10, y = 50)
        
        
#--------------------------------------------------------------------------------------------------------------------------------------APP DEFINITIONS ABOVE

    tb1 = Button(root, text = "Harrison OS", bg = "black", fg = "white", width = 12, command = c3) #home button
    tb2 = Button(root, text = "Calculator", bg = "black", fg = "white", width = 12, command = c4) #calculator app button
    tb3 = Button(root, text = "Settings", bg = "black", fg = "white", width = 12, command = c5) #settings app button
    tb4 = Button(root, text = "Notepad", bg = "black", fg = "white", width = 12, command = c20) #notepad app button
    tb10 = Button(root, text = now, width = 20, bg = taskbar_color, fg = "orange") #clock widget

    tb1.place(x = 0, y = 775)
    tb2.place(x = 100, y = 775)
    tb3.place(x = 200, y = 775)
    tb4.place(x = 300, y = 775)
    tb10.place(x = 1430, y = 775)

    if (should_update == 1):
        updates = float(updates) + 1
        root.after(1000, main)

    if (updates > 500):
        exit()
        root.destroy()

    end = time.time()

    ttl = float(end) -  float(start)
    root.mainloop()
    
    
main()
