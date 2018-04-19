#Create one game application
#Finish the web browser
#Add a settings menu to adjust recursion depth settings
#Add a function to clear the entire inbox

import socketserver
import winsound
import tkinter
import parser
import random
import time
import math
import sys
import os
from tkinter import *
from parser import *
from time import *
from sys import *
                                                            #########################################################################
root = Tk()                                                 #                                                                       #
root.title("Harrison OS V1.4.1")                            #   THIS BELONGS TO HARRISON LINDGREN [harrison.lindgren@gmail.com]     #
root.maxsize(width = 1580, height = 800)                    #   COPYING IS AGAINST THE TERMS OF CONDITIONS OF THIS SCRIPT           #
root.minsize(width = 1580, height = 800)                    #   THIS SCRIPT WAS CREATED 03/05/2018 [MM/DD/YYYY]                     #
                                                            #   THIS SCRIPT WAS CREATED 03/05/2018 [MM/DD/YYYY]                     #
stage = 'login'                                             #   ENVIRONMENTAL LANGUAGE IS PYTHON / CAN RUN ON PYTHON ENV            #
background_color = 'gray'                                   #   SCRIPT NATIVE TO IDLE PYTHON V 3.5.0                                #
taskbar_color = 'lightgray'                                 #                                                                       #
username = 'username'                                       #########################################################################
start_menu_visibility = False
notif_bar_visibility = False
c_time = '00:00'
notifs = 1
emails = ['ES01', 'ES02', 'ES03', 'ES04', 'ES05', 'ES06', 'ES07', 'ES08', 'ES09', 'ES10']
runs = 0
stack_overflow = 350
raised_error = None
version = 'HOS 1.4.1'
warning_1 = '''
WARNING:
THIS APPLICATION IS NEARING A STACK OVERFLOW
PLEASE EXIT THE APPLICATION
IF YOU DO NOT SUCCEED TO EXIT, YOUR COMPUTER MAY CRASH
THIS IS YOUR FINAL WARNING
FROM HERE ON, THIS MESSAGE WILL STAY PERMENANTLY ON YOUR SCREEN
IF YOU FAIL TO EXIT, THEN THE APPLICATION WILL SELF TERMINATE
'''
sysinfo = '''
#########################################################################
                                                                        
    THIS BELONGS TO HARRISON LINDGREN [harrison.lindgren@gmail.com]     
    COPYING IS AGAINST THE TERMS OF CONDITIONS OF THIS SCRIPT           
    THIS SCRIPT WAS CREATED 02/06/2018 [MM/DD/YYYY]                     
    ENVIRONMENTAL LANGUAGE IS PYTHON / CAN RUN ON PYTHON ENV            
    SCRIPT NATIVE TO IDLE PYTHON V 3.5.0                                
                                                                        
#########################################################################

Script tidal version: 1
Script build version: 4
Script update version: 0
[1.4.0]
'''

note1 = ''

rav1 = 0 #calculator
rav2 = 0 #calculator
rav3 = 1 #calculator
rav4 = 0 #calculator
rav5 = 500 #paino
rav6 = 0 #piano
rav7 = 0
rav8 = 0
rav9 = 0

email_01_context = ''
email_02_context = ''
email_03_context = ''
email_04_context = ''
email_05_context = ''
email_06_context = ''
email_07_context = ''
email_08_context = ''
email_09_context = ''
email_10_context = ''

def send_email(subject, message):
    global emails
    global email_01_context, email_02_context, email_03_context, email_04_context, email_05_context
    global email_01_context, email_02_context, email_03_context, email_04_context, email_05_context
    if (emails[0] == 'ES01'):
        emails = [(subject), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        email_01_context = message
    elif (emails[1] == 'ES02'):
        emails = [(emails[0]), (subject), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        email_02_context = message
    elif (emails[2] == 'ES03'):
        emails = [(emails[0]), (emails[1]), (subject), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        email_03_context = message
    elif (emails[3] == 'ES04'):
        emails = [(emails[0]), (emails[1]), (emails[2]), (subject), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        email_04_context = message
    elif (emails[4] == 'ES05'):
        emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (subject), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        email_05_context = message
    elif (emails[5] == 'ES06'):
        emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (subject), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        email_06_context = message
    elif (emails[6] == 'ES07'):
        emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (subject), (emails[7]), (emails[8]), (emails[9])]
        email_07_context = message
    elif (emails[7] == 'ES08'):
        emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (subject), (emails[8]), (emails[9])]
        email_08_context = message
    elif (emails[8] == 'ES09'):
        emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (subject), (emails[9])]
        email_09_context = message
    elif (emails[9] == 'ES10'):
        emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (subject)]
        email_10_context = message

if (version == 'HOS 1.4.1'):
    send_email('Whats in the new update?', '''
Tons of new features have been added in the recent 1.4.1 update!
Here are just a few of the things that have been added:

1.] New parser. This will make using searchbars much easier.

2.] New email feature. This feature will help you get all the latest updates
from your favirote websites or from the computer, regarding information.

3.] New clock, because time flies when you are having fun!

And many more things...
Stay tuned, for HOS 1.4.2
''')

def main():
    global rav1
    global rav2
    global rav3
    global rav4
    global rav5
    global rav6
    global rav7
    global rav8
    global rav9
    global runs
    global stage
    global note1
    global emails
    global c_time
    global notifs
    global sysinfo
    global version
    global username
    global warning_1
    global raised_error
    global taskbar_color
    global stack_overflow
    global background_color
    global notif_bar_visibility
    global start_menu_visibility
    global email_01_context, email_02_context, email_03_context, email_04_context, email_05_context
    global email_06_context, email_07_context, email_08_context, email_09_context, email_10_context

    sys.setrecursionlimit(stack_overflow)

    notifs = 0

    def delete_email(arg):
        global emails
        global email_01_context, email_02_context, email_03_context, email_04_context, email_05_context
        global email_06_context, email_07_context, email_08_context, email_09_context, email_10_context
        global stage
        if (arg == '1'):
            email_01_context = ''
            emails = [('ES01'), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        elif (arg == '2'):
            email_02_context = ''
            emails = [(emails[0]), ('ES02'), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        elif (arg == '3'):
            email_03_context = ''
            emails = [(emails[0]), (emails[1]), ('ES03'), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        elif (arg == '4'):
            email_04_context = ''
            emails = [(emails[0]), (emails[1]), (emails[2]), ('ES04'), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        elif (arg == '5'):
            email_05_context = ''
            emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), ('ES05'), (emails[5]), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        elif (arg == '6'):
            email_06_context = ''
            emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), ('ES06'), (emails[6]), (emails[7]), (emails[8]), (emails[9])]
        elif (arg == '7'):
            email_07_context = ''
            emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), ('ES07'), (emails[7]), (emails[8]), (emails[9])]
        elif (arg == '8'):
            email_08_context = ''
            emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), ('ES08'), (emails[8]), (emails[9])]
        elif (arg == '9'):
            email_09_context = ''
            emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), ('ES09'), (emails[9])]
        elif (arg == '10'):
            email_10_context = ''
            emails = [(emails[0]), (emails[1]), (emails[2]), (emails[3]), (emails[4]), (emails[5]), (emails[6]), (emails[7]), (emails[8]), ('ES10')]
        elif (arg.lower() == 'all'):
            emails = ['ES01', 'ES02', 'ES03', 'ES04', 'ES05', 'ES06', 'ES07', 'ES08', 'ES09', 'ES10']
            email_01_context = ''
            email_02_context = ''
            email_03_context = ''
            email_04_context = ''
            email_05_context = ''
            email_06_context = ''
            email_07_context = ''
            email_08_context = ''
            email_09_context = ''
            email_10_context = ''
        stage = 'email'
        main()

    def clock_refresh():
        global c_time
        raw_time = localtime()
        raw_time = str(raw_time)
        hour = 0
        minute = 0
        second = 0
        day = 0
        month = 0
        year = 0
        c_time = 0

        year = raw_time.split(',')[0]
        year = year.split('=')[1]

        month = raw_time.split(',')[1]
        month = month.split('=')[1]

        day = raw_time.split(',')[2]
        day = day.split('=')[1]

        hour = raw_time.split(',')[3]
        hour = hour.split('=')[1]

        minute = raw_time.split(',')[4]
        minute = minute.split('=')[1]

        second = raw_time.split(',')[5]
        second = second.split('=')[1]
        
        c_time = (str(month) + '/' + str(day) + '/' + str(year) + '   ' + str(hour) + ':' + str(minute) + ':' + str(second) + ' ')
    clock_refresh()

    if (emails[0] != 'ES01'):
        notifs = notifs + 1
    if (emails[1] != 'ES02'):
        notifs = notifs + 1
    if (emails[2] != 'ES03'):
        notifs = notifs + 1
    if (emails[3] != 'ES04'):
        notifs = notifs + 1
    if (emails[4] != 'ES05'):
        notifs = notifs + 1
    if (emails[5] != 'ES06'):
        notifs = notifs + 1
    if (emails[6] != 'ES07'):
        notifs = notifs + 1
    if (emails[7] != 'ES08'):
        notifs = notifs + 1
    if (emails[8] != 'ES09'):
        notifs = notifs + 1
    if (emails[9] != 'ES10'):
        notifs = notifs + 1           
    
    def tune_piano(up_dn):
        global rav6
        global rav5
        if (up_dn == 'up'):
            rav6 = float(rav6) + 10
        elif (up_dn == 'dn'):
            if (float(rav5) + float(rav6) > 50):
                rav6 = float(rav6) - 10
        main()

    def set_rav12(redefinition):
        global rav1
        global rav2
        if (redefinition != 'a'):
            if (rav3 == 1):
                rav1 = str(rav1) + redefinition
            elif (rav3 == 2):
                rav2 = str(rav2) + redefinition
        elif (redefinition == 'a'):
            if (rav3 == 1):
                rav1 = '0'
            elif (rav3 == 2):
                rav2 = '0'
        main()
        
    def rav3_toggle():
        global rav3
        if (rav3 == 1):
            rav3 = 2
        elif (rav3 == 2):
            rav3 = 1
        elif (rav3 != 1 or rav3 != 2):
            rav3 = 1

    def c1():
        global stage
        global username
        stage = 'home'
        username = username_q.get()
        main()

    def solve1(rava):
        global rav1 #num1
        global rav2 #num2
        global rav4 #answer
        if (rava == '+'):
            rav4 = float(rav1) + float(rav2)
        if (rava == '-'):
            rav4 = float(rav1) - float(rav2)
        if (rava == '*'):
            rav4 = float(rav1) * float(rav2)
        if (rava == '/'):
            rav4 = float(rav1) / float(rav2)
        main()

    def set_stage_to(arg1):
        global stage
        stage = str(arg1)
        main()

    def cdc_(color):
        global background_color
        background_color = color
        main()

    def start_menu_vis_toggle():
        global start_menu_visibility
        if (start_menu_visibility == False):
            start_menu_visibility = True
        elif (start_menu_visibility == True):
            start_menu_visibility = False
        main()

    def rdfs_soundboard():
        global rav5
        global rav6
        rav5 = 500
        rav6 = 0
        main()

    def notifs_menu_vis_toggle():
        global stage
        stage = 'email'
        main()

    def notepad_save():
        global note1
        note1 = ''
        if (notepad_e1.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) + ' ' + str(notepad_e1.get())
        if (notepad_e2.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e2.get())
        if (notepad_e3.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e3.get())
        if (notepad_e4.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e4.get())
        if (notepad_e5.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e5.get())
        if (notepad_e6.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e6.get())
        if (notepad_e7.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e7.get())
        if (notepad_e8.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e8.get())
        if (notepad_e9.get() != '' and notepad_e1.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e9.get())
        if (notepad_e10.get() != '' and notepad_e10.get() != ' '):
            note1 = str(note1) +  ' ' + str(notepad_e1.get())

    def refresh_():
        main()

    def search():
        global stage
        global start_menu_visibility
        start_menu_visibility = False
        searchq = searchbar_query.get()
        searchq = searchq.lower()
        if (searchq == 'settings' or searchq == 'setting'):
            stage = searchq
        elif (searchq == 'calculator' or searchq == 'home'):
            stage = searchq
        elif (searchq == 'home'or searchq == 'main'):
            stage =  searchq
        elif (searchq == 'time'):
            stage = 'settings/time'
        elif (searchq == 'sysinfo'):
            stage = 'settings/sysinfo'
        elif (searchq == 'runs' or searchq == 'run'):
            stage = 'settings/sysinfo/varas'
        elif (searchq == 'native' or searchq == 'natives'):
            stage = 'settings/sysinfo/envinfo'
        elif (searchq == 'vars' or searchq == 'var' or searchq == 'variable' or searchq == 'variables'):
            stage = 'settings/sysinfo/varas'
        elif (searchq == 'notepad'):
            stage = 'notepad'
        elif (searchq == 'piano' or searchq == 'soundboard'):
            stage = 'soundboard'
        elif (searchq == 'included'or searchq == 'module' or searchq == 'modules'):
            stage = 'settings/sysinfo/envinfo'
        elif (searchq == 'color' or searchq == 'colors'):
            stage = 'settings/colorprefs'
        elif (searchq == 'background' or searchq == 'desktop'):
            stage = 'settings/colorprefs/bgndhms'
        elif (searchq == 'internet'):
            stage = 'internet'
        elif (searchq == 'files' or searchq == 'file' or searchq == 'file explorer' or searchq == 'files explorer'):
            stage = 'files'
        elif (searchq == 'notif' or searchq == 'notifs' or searchq == 'email' or searchq == 'emails' or searchq == 'notifications' or searchq == 'notification' or searchq == 'message' or searchq == 'messages'):
            stage = 'email'
        main()

    topbar1 = Button(root, text = 'X', bg = 'lightgray', width = 6, activebackground = 'red', command = lambda: root.destroy() or exit() or quit() or print('Exit failure.'))
    topbar1.place(x = 0, y = 0)
    topbar2 = Button(root, text = '[ ]', bg = 'lightgray', width = 6, activebackground = 'lightgray', command = None)
    topbar2.place(x = 60, y = 0)
    topbar3 = Button(root, text = '-', bg = 'lightgray', width = 6, activebackground = 'lightgray', command = None)
    topbar3.place(x = 120, y = 0)

    root.configure(bg = background_color)

    if (stage != 'login'):
        taskbar_bg = Canvas(root, bg = taskbar_color, width = 1580)
        taskbar_bg.place(x = 0, y = 775)
        taskbar_hos = Button(root, bg = 'black', fg = 'white', width = 5, text = 'H-OS', command = lambda: start_menu_vis_toggle())
        taskbar_hos.place(x = 0, y = 775)
        taskbar_home = Button(root, bg = 'black', fg = 'white', width = 15, text = 'Home', command = lambda: set_stage_to('home'))
        taskbar_home.place(x = 50, y = 775)
        taskbar_settings = Button(root, bg = 'black', fg = 'white', width = 15, text = 'Settings', command = lambda: set_stage_to('settings'))
        taskbar_settings.place(x = 175, y = 775)
        taskbar_calculator = Button(root, bg = 'black', fg = 'white', width = 15, text = 'Calculator', command = lambda: set_stage_to('calculator'))
        taskbar_calculator.place(x = 300, y = 775)
        taskbar_notepad = Button(root, bg = 'black', fg = 'white', width = 15, text = 'Notepad', command = lambda: set_stage_to('notepad'))
        taskbar_notepad.place(x = 425, y = 775)
        taskbar_internet = Button(root, bg = 'black', fg = 'white', width = 15, text = 'Files', command = lambda: set_stage_to('files'))
        taskbar_internet.place(x = 550, y = 775)
        taskbar_notifs = Button(root, bg = 'lightgray', fg = 'black', width = 2, text = notifs, command = lambda: notifs_menu_vis_toggle())
        taskbar_notifs.place(x = 1550, y = 775)
        taskbar_clock = Label(root, text = c_time, bg = 'lightgray')
        taskbar_clock.place(x = 1425, y = 777.5)
        
    if (stage == 'login'):
        start_menu_visibility = False
        screenbackground = Canvas(root, width = 1575, height = 800, bg = background_color)
        screenbackground.place(x = 0, y = 30)
        username_i = Label(root, text = 'Username', bg = background_color)
        username_i.place(x = 820, y = 375)
        username_q = Entry(root, width = 40)
        username_q.place(x = 725, y = 400)
        username_s = Button(root, text = 'Login', bg = background_color, activebackground = background_color, fg = 'black', command = lambda: c1())
        username_s.place(x = 830, y = 430)
        winsound.MessageBeep(10)

    if (stage == 'files'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)

    if (stage == 'email'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        ES01 = Button(root, width = 100, text = (str(emails[0]) + (' ')), command = lambda: set_stage_to('email/email01'))
        ES01.place(y = 30, x = 50)
        ES02 = Button(root, width = 100, text = (str(emails[1]) + (' ')), command = lambda: set_stage_to('email/email02'))
        ES02.place(y = 60, x= 50)
        ES03 = Button(root, width = 100, text = (str(emails[2]) + (' ')), command = lambda: set_stage_to('email/email03'))
        ES03.place(y = 90, x = 50)
        ES04 = Button(root, width = 100, text = (str(emails[3]) + (' ')), command = lambda: set_stage_to('email/email04'))
        ES04.place(y = 120, x = 50)
        ES05 = Button(root, width = 100, text = (str(emails[4]) + (' ')), command = lambda: set_stage_to('email/email05'))
        ES05.place(y = 150, x = 50)
        ES06 = Button(root, width = 100, text = (str(emails[5]) + (' ')), command = lambda: set_stage_to('email/email06'))
        ES06.place(y = 180, x = 50)
        ES07 = Button(root, width = 100, text = (str(emails[6]) + (' ')), command = lambda: set_stage_to('email/email07'))
        ES07.place(y = 210, x = 50)
        ES08 = Button(root, width = 100, text = (str(emails[7]) + (' ')), command = lambda: set_stage_to('email/email08'))
        ES08.place(y = 240, x = 50)
        ES09 = Button(root, width = 100, text = (str(emails[8]) + (' ')), command = lambda: set_stage_to('email/email09'))
        ES09.place(y = 270, x = 50)
        ES10 = Button(root, width = 100, text = (str(emails[9]) + (' ')), command = lambda: set_stage_to('email/email10'))
        ES10.place(y = 300, x = 50)
        test = Button(root, text = 'Test', bg = 'black', fg = 'white', command = lambda: send_email('Test email', 'This email is a test. 0-1-2-3-4-5-6-7-8-9. Test succsessfully completed!'))
        test.place(y = 330, x = 50)
        refresh = Button(root, bg = 'black', fg = 'white', text = 'Refresh inbox', command = refresh_)
        refresh.place(y = 330, x = 85)
        clear = Button(root, bg = 'black', fg = 'white', text = 'Clear inbox', command = lambda: delete_email('all'))
        clear.place(y = 330, x = 170)

    if (stage == 'email/email01'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[0])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_01_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('1'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email02'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[1])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_02_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('2'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email03'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[2])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_03_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('3'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email04'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[3])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_04_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('4'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email05'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[4])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_05_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('5'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email06'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[5])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_06_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('6'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email07'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[6])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_07_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('7'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email08'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[7])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_08_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('8'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email09'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[8])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_09_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('9'))
        delete.place(y = 50, x = 500)
    elif (stage == 'email/email10'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'white')
        screenbackground.place(x = 0, y = 30)
        subject = Label(root, text = ('Subject: ', (emails[9])), bg = 'white')
        subject.place(x = 50, y = 50)
        contents = Label(root, text = ('Message: ', (email_10_context)), bg = 'white')
        contents.place(x = 50, y = 80)
        delete = Button(root, text = 'Delete email', bg = 'red', command = lambda: delete_email('10'))
        delete.place(y = 50, x = 500)

    if (stage == 'soundboard'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        piano_c1 = Canvas(root, bg = 'lightgray', width = 300, height = 300)
        piano_c1.place(x = 200, y = 200)
        piano_l1 = Label(root, text = 'Tuning/Pitch controls:', bg = 'lightgray')
        piano_l1.place(x = 210, y = 210)
        piano_tu = Button(root, bg = 'black', width = 5, fg = 'white', text = 'Pitch +', command = lambda: tune_piano('up'))
        piano_tu.place(x = 210, y = 250)
        piano_td = Button(root, bg = 'black', width = 5, fg = 'white', text = 'Pitch -', command = lambda: tune_piano('dn'))
        piano_td.place(x = 210, y = 275)
        piano_rt = Button(root, bg = 'lightgray', fg = 'Black', border = None, text = 'Restore defualt settings', command = rdfs_soundboard)
        piano_rt.place(x = 210, y = 470)        
        piano_k1 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 0), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 0), 100))
        piano_k1.place(x = 50, y = 50)
        piano_k2 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 50), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 50), 100))
        piano_k2.place(x = 100, y = 50)
        piano_k3 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 100), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 100), 100))
        piano_k3.place(x = 150, y = 50)
        piano_k4 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 150), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 150), 100))
        piano_k4.place(x = 200, y = 50)
        piano_k5 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 200), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 200), 100))
        piano_k5.place(x = 250, y = 50)
        piano_k6 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 250), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 250), 100))
        piano_k6.place(x = 300, y = 50)
        piano_k7 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 300), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 300), 100))
        piano_k7.place(x = 350, y = 50)
        piano_k8 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 350), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 350), 100))
        piano_k8.place(x = 400, y = 50)
        piano_k9 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 400), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 400), 100))
        piano_k9.place(x = 450, y = 50)
        piano_k10 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 450), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 450), 100))
        piano_k10.place(x = 500, y = 50)
        piano_k11 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 500), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 500), 100))
        piano_k11.place(x = 550, y = 50)
        piano_k12 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 550), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 550), 100))
        piano_k12.place(x = 600, y = 50)
        piano_k13 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 600), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 600), 100))
        piano_k13.place(x = 650, y = 50)
        piano_k14 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 650), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 650), 100))
        piano_k14.place(x = 700, y = 50)
        piano_k15 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 700), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 700), 100))
        piano_k15.place(x = 750, y = 50)
        piano_k16 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 750), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 750), 100))
        piano_k16.place(x = 800, y = 50)
        piano_k17 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 800), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 800), 100))
        piano_k17.place(x = 850, y = 50)
        piano_k18 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 850), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 850), 100))
        piano_k18.place(x = 900, y = 50)
        piano_k19 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 900), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 900), 100))
        piano_k19.place(x = 950, y = 50)
        piano_k20 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 950), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 950), 100))
        piano_k20.place(x = 1000, y = 50)
        piano_k21 = Button(root, bg = 'black', fg = 'white', width = 5, text = (float(rav5) + float(rav6) + 1000), command = lambda: winsound.Beep((int(rav5) + int(rav6) + 1000), 100))
        piano_k21.place(x = 1050, y = 50)
        
    if (stage == 'home'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = background_color)
        screenbackground.place(x = 0, y = 30)
        home_soundboard = Button(root, bg = 'black', fg = 'white', width = 10, text = 'Soundboard', height = 3, command = lambda: set_stage_to('soundboard'))
        home_soundboard.place(x = 25, y = 50)
        home_soundboard = Button(root, bg = 'black', fg = 'white', width = 10, text = 'Internet', height = 3, command = lambda: set_stage_to('internet'))
        home_soundboard.place(x = 25, y = 125)

    if (stage == 'internet'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'lightblue')
        screenbackground.place(x = 0, y = 30)

    if (stage == 'notepad'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = background_color)
        screenbackground.place(x = 0, y = 30)
        notepad_c1 = Canvas(root, width = 1000, height = 300, bg = 'white')
        notepad_c1.place(x = 100, y = 100)
        notepad_l1 = Label(root, text = 'Notepad', bg = 'white')
        notepad_l1.place(x = 110, y = 110)
        notepad_e1 = Entry(root, width = 160)
        notepad_e1.place(x = 110, y = 150)
        notepad_e2 = Entry(root, width = 160)
        notepad_e2.place(x = 110, y = 170)
        notepad_e3 = Entry(root, width = 160)
        notepad_e3.place(x = 110, y = 190)
        notepad_e4 = Entry(root, width = 160)
        notepad_e4.place(x = 110, y = 210)
        notepad_e5 = Entry(root, width = 160)
        notepad_e5.place(x = 110, y = 230)
        notepad_e6 = Entry(root, width = 160)
        notepad_e6.place(x = 110, y = 250)
        notepad_e7 = Entry(root, width = 160)
        notepad_e7.place(x = 110, y = 270)
        notepad_e8 = Entry(root, width = 160)
        notepad_e8.place(x = 110, y = 290)
        notepad_e9 = Entry(root, width = 160)
        notepad_e9.place(x = 110, y = 310)
        notepad_e10 = Entry(root, width = 160)
        notepad_e10.place(x = 110, y = 330)
        notepad_e11 = Entry(root, width = 160)
        notepad_e11.place(x = 110, y = 350)
        notepad_e12 = Entry(root, width = 160)
        notepad_e12.place(x = 110, y = 370)
        save = Button(root, text = 'Save', bg = 'green', command = lambda: notepad_save())
        save.place(x = 1060, y = 105)
        emailit = Button(root, text = 'Email saved version to me', bg = 'green', command = lambda: send_email(('Notepad document at ' + c_time + ' from ', username), note1))
        emailit.place(x = 900, y = 105)

    if (stage == 'calculator'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        button_1 = Button(root, text = '1', width = 3, command = lambda: set_rav12(('1')))
        button_1.place(x = 100, y = 100)
        button_2 = Button(root, text = '2', width = 3, command = lambda: set_rav12(('2')))
        button_2.place(x = 150, y = 100)
        button_3 = Button(root, text = '3', width = 3, command = lambda: set_rav12(('3')))
        button_3.place(x = 200, y = 100)
        button_4 = Button(root, text = '4', width = 3, command = lambda: set_rav12(('4')))
        button_4.place(x = 100, y = 150)
        button_5 = Button(root, text = '5', width = 3, command = lambda: set_rav12(('5')))
        button_5.place(x = 150, y = 150)
        button_6 = Button(root, text = '6', width = 3, command = lambda: set_rav12(('6')))
        button_6.place(x = 200, y = 150)
        button_7 = Button(root, text = '7', width = 3, command = lambda: set_rav12(('7')))
        button_7.place(x = 100, y = 200)
        button_8 = Button(root, text = '8', width = 3, command = lambda: set_rav12(('8')))
        button_8.place(x = 150, y = 200)
        button_9 = Button(root, text = '9', width = 3, command = lambda: set_rav12(('9')))
        button_9.place(x = 200, y = 200)
        button_0 = Button(root, text = '0', width = 3, command = lambda: set_rav12(('0')))
        button_0.place(x = 150, y = 250)
        button_clear = Button(root, text = 'Clear', width = 7, command = lambda: set_rav12('a'))
        button_clear.place(x = 135, y = 300)
        rav1_ = Label(root, text = ('Entry 1 = ', rav1), bg = 'darkgray')
        rav1_.place(x = 300, y = 130)
        rav2_ = Label(root, text = ('Entry 2 = ', rav2), bg = 'darkgray')
        rav2_.place(x = 300, y = 150)
        rav4_ = Label(root, text = ('Answer = ', rav4), bg = 'darkgray')
        rav4_.place(x = 300, y = 170)
        button_enter = Button(root, text = 'Enter', width = 7, command = lambda: rav3_toggle())
        button_enter.place(x = 135, y = 350)
        button_solve = Button(root, text = 'Solve', width = 7, command = lambda: solve1(None))
        button_solve.place(x = 135, y = 400)
        button_plus = Button(root, text = '+', width = 2, command = lambda: solve1('+'))
        button_plus.place(x = 100, y = 450)
        button_minus = Button(root, text = '-', width = 2, command = lambda: solve1('-'))
        button_minus.place(x = 130, y = 450)
        button_multiply = Button(root, text = 'X', width = 2, command = lambda: solve1('*'))
        button_multiply.place(x = 170, y = 450)
        button_divide = Button(root, text = '/', width = 2, command = lambda: solve1('/'))
        button_divide.place(x = 200, y = 450)

    if (stage == 'settings'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_op1 = Button(root, text = 'Date and time settings', bg = 'lightgray', command = lambda: set_stage_to('settings/time'))
        settings_op1.place(x = 20, y = 50)
        settings_op2 = Button(root, text = 'System info', bg = 'lightgray', command = lambda: set_stage_to('settings/sysinfo'))
        settings_op2.place(x = 20, y = 80)
        settings_op3 = Button(root, text = 'Color preferences', bg = 'lightgray', command = lambda: set_stage_to('settings/colorprefs'))
        settings_op3.place(x = 20, y = 110)

    if (stage == 'settings/time'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_time_lb1 = Label(root, bg = 'darkgray', text = ('Refreshes: ', runs))
        settings_time_lb1.place(x = 20, y = 50)
        settings_time_lb2 = Label(root, bg = 'darkgray', text = ('Current native time: ', localtime()))
        settings_time_lb2.place(x = 20, y = 70)
        settings_time_lb3 = Label(root, bg = 'darkgray', text = ('Current display time: ', c_time))
        settings_time_lb3.place(x = 20, y = 90)

    if (stage == 'settings/sysinfo'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_sysinfo_op1 = Button(root, text = 'Native environment information', command = lambda: set_stage_to('settings/sysinfo/envinfo'))
        settings_sysinfo_op1.place(x = 20, y = 50)
        settings_sysinfo_op2 = Button(root, text = 'Variable assignments', command = lambda: set_stage_to('settings/sysinfo/varas'))
        settings_sysinfo_op2.place(x = 20, y = 80)
        settings_sysinfo_op3 = Button(root, text = 'Software info', command = lambda: set_stage_to('settings/sysinfo/softi'))
        settings_sysinfo_op3.place(x = 20, y = 110)

    if (stage == 'settings/colorprefs'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_colorprefs_op1 = Button(root, text = 'Buttons', bg = 'lightgray', command = lambda: set_stage_to('settings/colorprefs/bttns'))
        settings_colorprefs_op1.place(x = 20, y = 50)
        settings_colorprefs_op2 = Button(root, text = 'Backgound/Homescreen', bg = 'lightgray', command = lambda: set_stage_to('settings/colorprefs/bgndhms'))
        settings_colorprefs_op2.place(x = 20, y = 80)

    if (stage == 'settings/colorprefs/bgndhms'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_colorprefs_bgndhms_op1 = Button(root, text = 'Change desktop color to white', fg = 'black', bg = 'white', command = lambda: cdc_('white'))
        settings_colorprefs_bgndhms_op1.place(x = 20, y = 50)
        settings_colorprefs_bgndhms_op2 = Button(root, text = 'Change desktop color to lightgray', fg = 'black', bg = 'lightgray', command = lambda: cdc_('lightgray'))
        settings_colorprefs_bgndhms_op2.place(x = 20, y = 80)
        settings_colorprefs_bgndhms_op3 = Button(root, text = 'Change desktop color to lightblue', fg = 'black', bg = 'lightblue', command = lambda: cdc_('lightblue'))
        settings_colorprefs_bgndhms_op3.place(x = 20, y = 110)
        settings_colorprefs_bgndhms_op4 = Button(root, text = 'Change desktop color to lightyellow', fg = 'black', bg = 'lightyellow', command = lambda: cdc_('lightyellow'))
        settings_colorprefs_bgndhms_op4.place(x = 20, y = 140)
        settings_colorprefs_bgndhms_op5 = Button(root, text = 'Change desktop color to orange', fg = 'black', bg = 'orange', command = lambda: cdc_('orange'))
        settings_colorprefs_bgndhms_op5.place(x = 20, y = 170)
        settings_colorprefs_bgndhms_op6 = Button(root, text = 'Change desktop color to purple', fg = 'white', bg = 'purple', command = lambda: cdc_('purple'))
        settings_colorprefs_bgndhms_op6.place(x = 20, y = 200)
        settings_colorprefs_bgndhms_op7 = Button(root, text = 'Change desktop color to red', fg = 'white', bg = 'red', command = lambda: cdc_('red'))
        settings_colorprefs_bgndhms_op7.place(x = 20, y = 230)
        settings_colorprefs_bgndhms_op6 = Button(root, text = 'Change desktop color to blue', fg = 'white', bg = 'blue', command = lambda: cdc_('blue'))
        settings_colorprefs_bgndhms_op6.place(x = 20, y = 260)
        settings_colorprefs_bgndhms_op6 = Button(root, text = 'Change desktop color to darkgray', fg = 'white', bg = 'darkgray', command = lambda: cdc_('darkgray'))
        settings_colorprefs_bgndhms_op6.place(x = 20, y = 290)
        settings_colorprefs_bgndhms_op6 = Button(root, text = 'Change desktop color to darkblue', fg = 'white', bg = 'darkblue', command = lambda: cdc_('darkblue'))
        settings_colorprefs_bgndhms_op6.place(x = 20, y = 320)
        settings_colorprefs_bgndhms_op6 = Button(root, text = 'Change desktop color to black', fg = 'white', bg = 'black', command = lambda: cdc_('black'))
        settings_colorprefs_bgndhms_op6.place(x = 20, y = 350)

    if (stage == 'settings/colorprefs/bttns'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)

    if (stage == 'settings/sysinfo/softi'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_sysinfo_softi_lb1 = Label(root, text = sysinfo, bg = 'darkgray')
        settings_sysinfo_softi_lb1.place(x = 20, y = 50)

    if (stage == 'settings/sysinfo/varas'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_sysinfo_varas_lb1 = Label(root, text = ('Variable [runs] = ', runs), bg = 'darkgray')
        settings_sysinfo_varas_lb1.place(x = 20, y = 50)
        settings_sysinfo_varas_lb2 = Label(root, text = ('Variable [stage] = ', stage), bg = 'darkgray')
        settings_sysinfo_varas_lb2.place(x = 20, y = 70)
        settings_sysinfo_varas_lb3 = Label(root, text = ('Variable [username] = ', username), bg = 'darkgray')
        settings_sysinfo_varas_lb3.place(x = 20, y = 90)
#        settings_sysinfo_varas_lb4 = Label(root, text = ('Variable [warning_1] = ', warning_1), bg = 'darkgray')
#        settings_sysinfo_varas_lb4.place(x = 20, y = 110)
        settings_sysinfo_varas_lb5 = Label(root, text = ('Variable [raised_error] = ', raised_error), bg = 'darkgray')
        settings_sysinfo_varas_lb5.place(x = 20, y = 110)
        settings_sysinfo_varas_lb6 = Label(root, text = ('Variable [taskbar_color] = ', taskbar_color), bg = 'darkgray')
        settings_sysinfo_varas_lb6.place(x = 20, y = 130)
        settings_sysinfo_varas_lb7 = Label(root, text = ('Variable [stack_overflow] = ', stack_overflow), bg = 'darkgray')
        settings_sysinfo_varas_lb7.place(x = 20, y = 150)
        settings_sysinfo_varas_lb8 = Label(root, text = ('Variable [background_color] = ', background_color), bg = 'darkgray')
        settings_sysinfo_varas_lb8.place(x = 20, y = 170)
        settings_sysinfo_varas_lb9 = Label(root, text = ('Variable [start_menu_visibility] = ', start_menu_visibility), bg = 'darkgray')
        settings_sysinfo_varas_lb9.place(x = 20, y = 190)
        settings_sysinfo_varas_lb10 = Label(root, text = ('Random misc variables [1-9]: ', rav1, ' ', rav2, ' ', rav3, ' ', rav4, ' ', rav5, ' ', rav6, ' ', rav7, ' ', rav8, ' ', rav9), bg = 'darkgray')
        settings_sysinfo_varas_lb10.place(x = 20, y = 210)
        settings_sysinfo_varas_lb11 = Label(root, text = ('Variable [notifs] = ', notifs), bg = 'darkgray')
        settings_sysinfo_varas_lb11.place(x = 20, y = 230)
        settings_sysinfo_varas_lb12 = Label(root, text = ('Variable [notif_bar_visibility] = ', notif_bar_visibility), bg = 'darkgray')
        settings_sysinfo_varas_lb12.place(x = 20, y = 250)
        settings_sysinfo_varas_lb13 = Label(root, text = ('Variable [version] = ', version), bg = 'darkgray')
        settings_sysinfo_varas_lb13.place(x = 20, y = 270)
        settings_sysinfo_varas_lb14 = Label(root, text = ('Variable [emails] = ', emails), bg = 'darkgray')
        settings_sysinfo_varas_lb14.place(x = 20, y = 290)
        settings_sysinfo_varas_lb14 = Label(root, text = ('Variable [note1] = ', note1), bg = 'darkgray')
        settings_sysinfo_varas_lb14.place(x = 20, y = 310)

    if (stage == 'settings/sysinfo/envinfo'):
        screenbackground = Canvas(root, width = 1575, height = 740, bg = 'darkgray')
        screenbackground.place(x = 0, y = 30)
        settings_sysinfo_envinfo_lb1 = Label(root, bg = 'darkgray', text = ('Native user: ', os.getlogin()))
        settings_sysinfo_envinfo_lb1.place(x = 20, y = 50)
        settings_sysinfo_envinfo_lb2 = Label(root, bg = 'darkgray', text = ('Native PPID: ', os.getppid()))
        settings_sysinfo_envinfo_lb2.place(x = 20, y = 70)
        settings_sysinfo_envinfo_lb3 = Label(root, bg = 'darkgray', text = ('Native PID: ', os.getpid()))
        settings_sysinfo_envinfo_lb3.place(x = 20, y = 90)
        settings_sysinfo_envinfo_lb4 = Label(root, bg = 'darkgray', text = ('Native cpu count: ', os.cpu_count()))
        settings_sysinfo_envinfo_lb4.place(x = 20, y = 110)
        settings_sysinfo_envinfo_lb5 = Label(root, bg = 'darkgray', text = ('Native path: ', os.get_exec_path()))
        settings_sysinfo_envinfo_lb5.place(x = 20, y = 130)
        settings_sysinfo_envinfo_lb6 = Label(root, bg = 'darkgray', text = ('Native dir __main__: ', dir('__main__')))
        settings_sysinfo_envinfo_lb6.place(x = 20, y = 150)
        settings_sysinfo_envinfo_lb7 = Label(root, bg = 'darkgray', text = ('Native dir __add__: ', dir('__add__')))
        settings_sysinfo_envinfo_lb7.place(x = 20, y = 170)
        settings_sysinfo_envinfo_lb8 = Label(root, bg = 'darkgray', text = ('Native dir __class__: ', dir('__class__')))
        settings_sysinfo_envinfo_lb8.place(x = 20, y = 190)
        settings_sysinfo_envinfo_lb9 = Label(root, bg = 'darkgray', text = ('Native module tkinter: ', tkinter))
        settings_sysinfo_envinfo_lb9.place(x = 20, y = 210)
        settings_sysinfo_envinfo_lb10 = Label(root, bg = 'darkgray', text = ('Native module socketserver: ', socketserver))
        settings_sysinfo_envinfo_lb10.place(x = 20, y = 230)
        settings_sysinfo_envinfo_lb11 = Label(root, bg = 'darkgray', text = ('Native module random: ', random))
        settings_sysinfo_envinfo_lb11.place(x = 20, y = 250)
        settings_sysinfo_envinfo_lb12 = Label(root, bg = 'darkgray', text = ('Native module time: ', time))
        settings_sysinfo_envinfo_lb12.place(x = 20, y = 270)
        settings_sysinfo_envinfo_lb13 = Label(root, bg = 'darkgray', text = ('Native module os: ', os))
        settings_sysinfo_envinfo_lb13.place(x = 20, y = 290)
        settings_sysinfo_envinfo_lb14 = Label(root, bg = 'darkgray', text = ('Native module math: ', math))
        settings_sysinfo_envinfo_lb14.place(x = 20, y = 310)
        settings_sysinfo_envinfo_lb15 = Label(root, bg = 'darkgray', text = ('Native module winsound', winsound))
        settings_sysinfo_envinfo_lb15.place(x = 20, y = 330)
        settings_sysinfo_envinfo_lb16 = Label(root, bg = 'darkgray', text = ('Native module parser', parser))
        settings_sysinfo_envinfo_lb16.place(x = 20, y = 350)
        settings_sysinfo_envinfo_lb17 = Label(root, bg = 'darkgray', text = ('Native module sys', sys))
        settings_sysinfo_envinfo_lb17.place(x = 20, y = 370)
        settings_sysinfo_envinfo_lb18 = Label(root, bg = 'darkgray', text = ('Native language: ', 'IDLE python V3.5.0/V3.7.0 [py.exe]'))
        settings_sysinfo_envinfo_lb18.place(x = 20, y = 390)

    directory_current = Label(root, text = stage, bg = background_color)
    directory_current.place(x = 1400, y = 35)

    def restart():
        global rav1
        global rav2
        global rav3
        global rav4
        global rav5
        global rav6
        global rav7
        global rav8
        global rav9
        global runs
        global stage
        global note1
        global emails
        global c_time
        global notifs
        global sysinfo
        global version
        global username
        global warning_1
        global raised_error
        global taskbar_color
        global stack_overflow
        global background_color
        global notif_bar_visibility
        global start_menu_visibility
        global email_01_context, email_02_context, email_03_context, email_04_context, email_05_context
        global email_06_context, email_07_context, email_08_context, email_09_context, email_10_context
        stage = 'login'                                             
        background_color = 'gray'                                 
        taskbar_color = 'lightgray'                                
        username = 'username'                     
        start_menu_visibility = False
        notif_bar_visibility = False
        c_time = '00:00'
        notifs = 1
        emails = ['ES01', 'ES02', 'ES03', 'ES04', 'ES05', 'ES06', 'ES07', 'ES08', 'ES09', 'ES10']
        runs = 0
        stack_overflow = 350
        raised_error = None
        version = 'HOS 1.4.1'
        warning_1 = '''
        WARNING:
        THIS APPLICATION IS NEARING A STACK OVERFLOW
        PLEASE EXIT THE APPLICATION
        IF YOU DO NOT SUCCEED TO EXIT, YOUR COMPUTER MAY CRASH
        THIS IS YOUR FINAL WARNING
        FROM HERE ON, THIS MESSAGE WILL STAY PERMENANTLY ON YOUR SCREEN
        IF YOU FAIL TO EXIT, THEN THE APPLICATION WILL SELF TERMINATE
        '''
        sysinfo = '''
        #########################################################################
                                                                                
            THIS BELONGS TO HARRISON LINDGREN [harrison.lindgren@gmail.com]     
            COPYING IS AGAINST THE TERMS OF CONDITIONS OF THIS SCRIPT           
            THIS SCRIPT WAS CREATED 02/06/2018 [MM/DD/YYYY]                     
            ENVIRONMENTAL LANGUAGE IS PYTHON / CAN RUN ON PYTHON ENV            
            SCRIPT NATIVE TO IDLE PYTHON V 3.5.0                                
                                                                                
        #########################################################################

        Script tidal version: 1
        Script build version: 4
        Script update version: 0
        [1.4.0]
        '''

        note1 = ''

        rav1 = 0 #calculator
        rav2 = 0 #calculator
        rav3 = 1 #calculator
        rav4 = 0 #calculator
        rav5 = 500 #paino
        rav6 = 0 #piano
        rav7 = 0
        rav8 = 0
        rav9 = 0

        email_01_context = ''
        email_02_context = ''
        email_03_context = ''
        email_04_context = ''
        email_05_context = ''
        email_06_context = ''
        email_07_context = ''
        email_08_context = ''
        email_09_context = ''
        email_10_context = ''
        if (version == 'HOS 1.4.1'):
            send_email('Whats in the new update?', '''
Tons of new features have been added in the recent 1.4.1 update!
Here are just a few of the things that have been added:

1.] New parser. This will make using searchbars much easier.

2.] New email feature. This feature will help you get all the latest updates
from your favirote websites or from the computer, regarding information.

3.] New clock, because time flies when you are having fun!

And many more things...
Stay tuned, for HOS 1.4.2
''')
        main()
    
    if (start_menu_visibility == True):
        smu_bg = Canvas(root, width = 200, height = 300, bg = 'black')
        smu_bg.place(x = 0, y = 470)
        smu_widget_settings = Button(root, text = 'Settings', fg = 'white', bg = 'black', command = lambda: set_stage_to('settings') or start_menu_vis_toggle())
        smu_widget_settings.place(x = 10, y = 480)
        smu_widget_home = Button(root, text = 'Home', fg = 'white', bg = 'black', command = lambda: set_stage_to('home') or start_menu_vis_toggle())
        smu_widget_home.place(x = 10, y = 510)
        smu_widget_logoff = Button(root, text = 'Logout', fg = 'white', bg = 'black', command = lambda: set_stage_to('login') or start_menu_vis_toggle())
        smu_widget_logoff.place(x = 10, y = 540)
        smu_widget_restart = Button(root, text = 'Restart', fg = 'white', bg = 'black', command = lambda: restart())
        smu_widget_restart.place(x = 10, y = 570)
        directory_current = Label(root, text = (str(stage) + '/start-menu-visible'), bg = background_color)
        directory_current.place(x = 1400, y = 35)
        searchbar_query = Entry(root)
        searchbar_query.place(x = 5, y = 750)
        searchbar_search = Button(root, text = 'Search', bg = 'black', fg = 'white', command = search)
        searchbar_search.place(x = 135, y = 745)

    if (runs >= stack_overflow):
        raised_error = 'error_class_1'
        warning_p1 = Canvas(root, width = 500, height = 200, bg = 'red')
        warning_p1.place(x = 280, y = 180)
        warning_p2 = Label(root, text = warning_1, bg = 'red', fg = 'black')
        warning_p2.place(x = 330, y = 200)
        winsound.MessageBeep(10)

    if (raised_error == 'error_class_1'):
        error = Label(root, text = '/////////// ERROR_CLASS_1 RAISED /////////////', bg = 'red')
        error.place(x = 600, y = 5)
        winsound.MessageBeep(10)

    if (runs >= (float(stack_overflow) + (float(stack_overflow) / math.pi))):
        winsound.MessageBeep(10)
        os.abort()

    if (stage.lower() != 'login' and stage.lower() != 'home'):
        x = Button(root, text = 'X', bg = 'red', width = 1, command = lambda: set_stage_to('home'))
        x.place(x = 1565, y = 30)
    
    runs = float(runs) + 1
    root.mainloop()


main()

'''
ERROR_CLASS_1 = Stack overflow warning
ERROR_CLASS_2 = N/A
'''

