#Fix the [h:/desktop/notepad] application
#Add an API to the shell [h:/cmd.exe]

#########################################################################
#                                                                       #
#   THIS BELONGS TO HARRISON LINDGREN [harrison.lindgren@gmail.com]     #
#   COPYING IS AGAINST THE TERMS OF CONDITIONS OF THIS SCRIPT           #
#   THIS SCRIPT WAS CREATED 03/14/2018 [MM/DD/YYYY]                     #
#   ENVIRONMENTAL LANGUAGE IS PYTHON / CAN RUN ON PYTHON ENV            #
#   SCRIPT NATIVE TO IDLE PYTHON V 3.5.0                                #
#   COPYLEFT OF HARRISON LINDGREN [harrison.lindgren@gmail.com]         #
#                                                                       #
#########################################################################

import webbrowser
import winsound
import tkinter
import parser
import random
import time
import math
import sys
import os
from time import localtime
from tkinter import *
from parser import *
from sys import *

HOS = Tk()
HOS.title('Harrison OS V1.5.0')
HOS.maxsize(width = 1580, height = 800)
HOS.minsize(width = 1580, height = 800)

screen = 'login'

taskbar_color = 'black'
desktop_color = 'lightgray'
buttons_color = 'black'
foregnd_color = 'black'

rps_scores = [0, 0]

uptime = 0

start = time.time()

cv1 = ''
cv2 = ''
ans = ''
ope = ''
current_var = [True, False]
stage = 'main'

command1 = None

version = 'HOS 1.5.0'

recursion_depth = 400

search1 = None

user = 'admin'

notif_count = 0

width_ = 1580
height_ = 800

runs = 0

cv1 = 0
cv2 = 0
ope = ''
ans = 0

ram0 = 0
ram1 = 0
ram2 = 0
ram3 = 0
ram4 = 0
ram5 = 0
ram6 = 0
ram7 = 0
ram8 = 0
ram9 = 0

message_ = 'None'

contexts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
emails = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

login_failed = False
stack_overflow = False
taskbar_visibility = False
dev_email_sent = False

warning_1 = '''
WARNING:
THIS APPLICATION IS NEARING A STACK OVERFLOW
PLEASE EXIT THE APPLICATION
IF YOU DO NOT SUCCEED TO EXIT, YOUR COMPUTER MAY CRASH
THIS IS YOUR FINAL WARNING
FROM HERE ON, THIS MESSAGE WILL STAY PERMENANTLY ON YOUR SCREEN
IF YOU FAIL TO EXIT, THEN THE APPLICATION WILL SELF TERMINATE
'''

dev1email = '''
Welcome to HOS v1.5.0!

It has only been a month since the last tidal update came to the HOS software
and here is another one! In this version of HOS, many new things have been added.
One thing that has been added is a better software design and a copyleft. One
thing that has been improved on is the inbox/email application. Not only now can
you write and send emails, but soon we will include a network in which clients
can exchange emails over the inbox/email application. Another thing that has been
improved on is the event handling. Now, there should be less random crashes and
the OS should flow much better. Another new thing added is the command shell
[shell/cmd.exe] which can be used for debugging. One exciting thing that this
version of HOS has is the very first game ever developed by harrisonOS.co. Enjoy!

-Sincerely, the HOS team
'''

sysinfo_ = '''
#########################################################################
                                                                        
    THIS BELONGS TO HARRISON LINDGREN [harrison.lindgren@gmail.com]     
    COPYING IS AGAINST THE TERMS OF CONDITIONS OF THIS SCRIPT           
    THIS SCRIPT WAS CREATED 03/14/2018 [MM/DD/YYYY]                     
    ENVIRONMENTAL LANGUAGE IS PYTHON / CAN RUN ON PYTHON ENV            
    SCRIPT NATIVE TO IDLE PYTHON V 3.5.0                                
                                                                        
#########################################################################

Script tidal version: 1
Script build version: 5
Script update version: 0
[1.5.0]
'''

commands_ = '''
VARIABLES - GATHERS A LIST OF SYSTEM VARIABLES
MODULES - GATHERS A LIST OF SYSTEM MODULES
REC_DEPTH [ARGS] - SETS THE SYSTEM RECURSION LIMIT TO SAID NUMBER
GET_RECD - RETRIVES THE RECURSION LIMIT
CDIR - PRINTS THE CURRENT DIRECTORY
SEARCH [ARGS] - USES THE APPLICATION SEARCH COMMAND
REGEDIT - OPENS THE HOS REGISTRY
REFRESH - FORCE REFRESHES THE HOS WINDOW
PRINT [ARGS] - WILL PRINT THE NEXT WORD
NETSTAT - GETS A LIST OF NETWORK INFO
RUNSAMT [ARGS] - WILL SET THE RUNS VARIABLE TO THE SET AMOUNT
UTIME - PRINTS UPTIME INFO
ZIMBAWE - SENDS OFF FALSE SYSTEM ALERTS [FOR TESTING :D]
VERSION - GETS THE HOS (harrisonOS) SOFTWARE VERSION
USERACCOUNT - GETS THE CURRENT USER NAME
SYSACCOUNT - GETS ALL USER NAMES
TIMESTAT - PRINTS THE SYNCED TIME
DEV - SWITCHES USER TO THE DEVELOPER ACCOUNT
EXIT - EXITS THE COMMAND SHELL
ABORT - EXITS THE HOS (harrisonOS) APPLICATION
'''

def get_text(arg1, arg2):
    global user
    global search1
    global screen
    global login_failed
    text = arg1.get()
    user = str(text)
    screen = 'desktop'
    main()

def set_screen_to(arg):
    global screen
    screen = arg
    main()

def taskbar_toggle():
    global taskbar_visibility
    if (taskbar_visibility == True): taskbar_visibility = False
    elif (taskbar_visibility == False): taskbar_visibility = True
    else: taskbar_visibility = False
    main()

def search(a): #for taskbar, is not very strict.
    search = a.get()
    search = search.lower()
    search = search
    global screen
    if (search == 'cmd.exe' or search == 'shell'): screen = 'cmd.exe'
    elif (search == 'settings' or search == 'setting' or search == 'settings menu' or search == 'setting menu'): screen = 'settings'
    elif (search == 'colors' or search == 'color' or search == 'coloration' or search == 'color prefrences'): screen = 'settings/colorprefs'
    elif (search == 'emails' or search == 'email' or search == 'inbox'): screen = 'inbox'
    elif (search == 'calc' or search == 'calculate' or search == 'calculator' or search == 'calculations' or search == 'graphing' or search == 'graphing calculator'): screen = 'calculator'
    elif (search == 'game1' or search == 'rps' or search == 'rock paper scissors' or search == 'rock' or search == 'paper' or search == 'scissors'): screen = 'rps'
    elif (search == 'registry' or search == 'log'): screen = 'regedit'
    taskbar_toggle()
    main()

def searchcmd(a): #for command shell, and is extremely strict.
    search = a.lower()
    search = search
    global screen
    if (search == 'h:/settings'): screen = 'settings'
    elif (search == 'h:/desktop/inbox'): screen = 'inbox'
    elif (search == 'h:/desktop/calculator'): screen = 'calculator'
    elif (search == 'h:/desktop/notepad'): screen = 'notepad'
    main()

def send_email(subject, sender, message):
    global emails
    sender = (str(sender) + '@harrisonOS.net')
    if (emails[0] == '1'):
        emails[0] = (subject, ' | ', sender)
        contexts[0] = message
    elif (emails[1] == '2'):
        emails[1] = (subject, ' | ', sender)
        contexts[1] = message
    elif (emails[2] == '3'):
        emails[2] = (subject, ' | ', sender)
        contexts[2] = message
    elif (emails[3] == '4'):
        emails[3] = (subject, ' | ', sender)
        contexts[3] = message
    elif (emails[4] == '5'):
        emails[4] = (subject, ' | ', sender)
        contexts[4] = message
    elif (emails[5] == '6'):
        emails[5] = (subject, ' | ', sender)
        contexts[5] = message
    elif (emails[6] == '7'):
        emails[6] = (subject, ' | ', sender)
        contexts[6] = message
    elif (emails[7] == '8'):
        emails[7] = (subject, ' | ', sender)
        contexts[7] = message
    elif (emails[8] == '9'):
        emails[8] = (subject, ' | ', sender)
        contexts[8] = message
    elif (emails[9] == '10'):
        emails[9] = (subject, ' | ', sender)
        contexts[9] = message
    elif (emails[10] == '11'):
        emails[10] = (subject, ' | ', sender)
        contexts[10] = message
    elif (emails[11] == '12'):
        emails[11] = (subject, ' | ', sender)
        contexts[11] = message
    elif (emails[12] == '13'):
        emails[12] = (subject, ' | ', sender)
        contexts[12] = message
    elif (emails[13] == '14'):
        emails[13] = (subject, ' | ', sender)
        contexts[13] = message
    elif (emails[14] == '15'):
        emails[14] = (subject, ' | ', sender)
        contexts[14] = message
    elif (emails[15] == '16'):
        emails[15] = (subject, ' | ', sender)
        contexts[15] = message
    elif (emails[16] == '17'):
        emails[16] = (subject, ' | ', sender)
        contexts[16] = message
    elif (emails[17] == '18'):
        emails[17] = (subject, ' | ', sender)
        contexts[17] = message
    elif (emails[18] == '19'):
        emails[18] = (subject, ' | ', sender)
        contexts[19] = message
    elif (emails[19] == '20'):
        emails[19] = (subject, ' | ', sender)
        contexts[19] = message

def refresh_inbox():
    global notif_count
    global emails
    notif_count = 20
    if (emails[0] == '1'):notif_count = notif_count - 1
    if (emails[1] == '2'):notif_count = notif_count - 1
    if (emails[2] == '3'):notif_count = notif_count - 1
    if (emails[3] == '4'):notif_count = notif_count - 1
    if (emails[4] == '5'):notif_count = notif_count - 1
    if (emails[5] == '6'):notif_count = notif_count - 1
    if (emails[6] == '7'):notif_count = notif_count - 1
    if (emails[7] == '8'):notif_count = notif_count - 1
    if (emails[8] == '9'):notif_count = notif_count - 1
    if (emails[9] == '10'):notif_count = notif_count - 1
    if (emails[10] == '11'):notif_count = notif_count - 1
    if (emails[11] == '12'):notif_count = notif_count - 1
    if (emails[12] == '13'):notif_count = notif_count - 1
    if (emails[13] == '14'):notif_count = notif_count - 1
    if (emails[14] == '15'):notif_count = notif_count - 1
    if (emails[15] == '16'):notif_count = notif_count - 1
    if (emails[16] == '17'):notif_count = notif_count - 1
    if (emails[17] == '18'):notif_count = notif_count - 1
    if (emails[18] == '19'):notif_count = notif_count - 1
    if (emails[19] == '20'):notif_count = notif_count - 1

def gather_1(a, b, c, d, e, f, g, h, i):
    global message_
    message_ = [(a.get()),
                (b.get()),
                (c.get()),
                (d.get()),
                (e.get()),
                (f.get()),
                (g.get()),
                (h.get()),
                (i.get())
                ]

def delete_email(arg):
    global emails
    global contexts
    global screen
    emails[(arg - 1)] = str(arg)
    contexts[(arg - 1)] = str(arg)
    screen = 'inbox'
    main()

def delete_inbox():
    delete_email(1)
    delete_email(2)
    delete_email(3)
    delete_email(4)
    delete_email(5)
    delete_email(6)
    delete_email(7)
    delete_email(8)
    delete_email(9)
    delete_email(10)
    delete_email(11)
    delete_email(12)
    delete_email(13)
    delete_email(14)
    delete_email(15)
    delete_email(16)
    delete_email(17)
    delete_email(18)
    delete_email(19)
    delete_email(20)

def make_cover(color):
    cover_ = Canvas(HOS, width = (width_ - 5), height = (height_ - 37.5), bg = color)
    cover_.place(x = 0, y = 0)

def view_email(email_number):
    global contexts
    global emails
    try:
        emails_ = str(emails[(email_number - 1)])
        sender = emails_.split("'")[5]
        subject = emails_.split("'")[1]
        context = contexts[(email_number - 1)]
    except IndexError:
        sender = 'None'
        subject = 'None'
        context = 'None'
    Cover_1 = Canvas(HOS, width = 600, height = 610, bg = 'lightgray')
    Cover_1.place(x = 900, y = 90)
    Subject = Label(HOS, bg = 'lightgray', text = ('Subject: ', subject))
    Subject.place(x = 1000, y = 150)
    Sender = Label(HOS, bg = 'lightgray', text = ('Sender: ', sender))
    Sender.place(x = 1000, y = 200)
    Context = Label(HOS, bg = 'lightgray', text = ('Message: ', context))
    Context.place(x = 1000, y = 250)
    Back = Button(HOS, text = 'Return to inbox', command = lambda: set_screen_to('inbox'))
    Back.place(x = 1000, y = 100)
    Delete_email = Button(HOS, text = 'Delete email', command = lambda: delete_email(email_number))
    Delete_email.place(x = 1150, y = 100)

def cmd_interperet(arg):
    command_ = arg.get()
    command_ = command_.lower()
    global ram0, ram1, ram2, ram3, ram4
    global ram5, ram6, ram7, ram8, ram9
    global runs, recursion_depth, version
    global taskbar_color, desktop_color
    global buttons_color, foregnd_color
    global width_, height_, search1, user
    global login_failed, stack_overflow
    global taskbar_visibility, notif_count
    global emails, command1, message_, ope
    global cv1, cv2, ans, current_var, stage
    global uptime, start

    end = time.time()
    
    uptime = (end - start)

    runs = runs + 1

    cmdcover = Canvas(HOS, bg = 'black', width = 1575, height = 730, border = 0)
    cmdcover.place(x = 0, y = 0)

    try:

        entire = ('Variable list is not yet available.')
        
        if (command_ == 'help' or command_ == '/help'):
            help_ = Label(HOS, bg = 'black', fg = 'green', text = '''
    VARIABLES - GATHERS A LIST OF SYSTEM VARIABLES
    MODULES - GATHERS A LIST OF SYSTEM MODULES
    REC_DEPTH [ARGS] - SETS THE SYSTEM RECURSION LIMIT TO SAID NUMBER
    GET_RECD - RETRIVES THE RECURSION LIMIT
    CDIR - PRINTS THE CURRENT DIRECTORY
    SEARCH [ARGS] - USES THE APPLICATION SEARCH COMMAND
    REGEDIT - OPENS THE HOS REGISTRY
    REFRESH - FORCE REFRESHES THE HOS WINDOW
    PRINT [ARGS] - WILL PRINT THE NEXT WORD
    NETSTAT - GETS A LIST OF NETWORK INFO
    RUNSAMT [ARGS] - WILL SET THE RUNS VARIABLE TO THE SET AMOUNT
    UTIME - PRINTS UPTIME INFO
    ZIMBAWE - SENDS OFF FALSE SYSTEM ALERTS [FOR TESTING :D]
    VERSION - GETS THE HOS (harrisonOS) SOFTWARE VERSION
    USERACCOUNT - GETS THE CURRENT USER NAME
    SYSACCOUNT - GETS ALL USER NAMES
    TIMESTAT - PRINTS THE SYNCED TIME
    DEV - SWITCHES USER TO THE DEVELOPER ACCOUNT
    BEEP [FREQ] [MILLISECONDS] - MAKES A BEEP
    EXIT - EXITS THE COMMAND SHELL
    ABORT - EXITS THE HOS (harrisonOS) APPLICATION
    ''')
            help_.place(x = 10, y = 10)
        elif (command_ == 'variables'):
            variables = Label(HOS, bg = 'black', fg = 'green', text = entire)
            variables.place(x = 10, y = 10)
        elif (command_ == 'cdir'):
            cdir = Label(HOS, bg = 'black', fg = 'green', text = screen)
            cdir.place(x = 10, y = 10)
        elif (command_.split(' ')[0] == 'search'):
            try:
                searchcmd((command_.split(' ')[1]))
            except IndexError:
                command_ = ''
        elif (command_ == 'regedit'):
            set_screen_to('regedit')
        elif (command_ == 'refresh'):
            main()
        elif (command_.split(' ')[0] == 'print'):
            try:
                rest = command_.split(' ')[1]
                textrest = Label(HOS, text = rest, bg = 'black', fg = 'green')
                textrest.place(x = 10, y = 10)
            except IndexError:
                command_ = ''
        elif (command_.split(' ')[0] == 'rec_depth'):
            try:
                rest = command_.split(' ')[1]
                try:
                    sys.setrecursionlimit(int(rest))
                except ValueError:
                    rest = ''
            except IndexError:
                resr = ''
        elif (command_ == 'utime'):
            make_label(('RUN COUNT: ', runs), 'black', 'green', 10, 10)
            make_label(('UPTIME [SECONDS]: ', uptime), 'black', 'green', 10, 30)
        elif (command_ == 'get_recd'):
            make_label((sys.getrecursionlimit()), 'black', 'green', 20, 20)
        elif ((command_.split(' ')[0]) == 'runsamnt'):
            runs = int((command_.split(' ')[1]))
            make_label((runs), 'black', 'green', 20, 20)
        elif (command_ == 'zimbawe'):
            warning_p1 = Canvas(HOS, width = 500, height = 200, bg = 'red')
            warning_p1.place(x = 280, y = 180)
            warning_p2 = Label(HOS, text = warning_1, bg = 'red', fg = 'black')
            warning_p2.place(x = 330, y = 200)
            winsound.MessageBeep(10)
            time.sleep(999)
        elif (command_ == 'version'):
            make_label(version, 'black', 'green', 20, 20)
        elif (command_ == 'dev'):
            user = 'dev'
        elif (command_ == 'useraccount'):
            make_label((user), 'black', 'green', 20, 20)
        elif (command_ == 'exit'):
            set_screen_to('desktop')
        elif (command_ == 'sysaccount'):
            make_label((user), 'black', 'green', 20, 20)
            make_label(('developer'), 'black', 'green', 20, 40)
        elif (command_ == 'timestat'):
            make_label((localtime()), 'black', 'green', 20, 20)
        elif (command_ == 'netstat'):
            make_label(('PID: ', os.getpid()), 'black', 'green', 20, 20)
            make_label(('PPID: ', os.getppid()), 'black', 'green', 20, 40)
            make_label(('NATIVE USER: ', os.getlogin()), 'black', 'green', 20, 60)
            make_label(('NATIVE CPUS: ', os.cpu_count()), 'black', 'green', 20, 80)
            make_label(('NATIVE TIME: ', localtime()), 'black', 'green', 20, 100)
        elif ((command_.split(' ')[0]) == 'beep'):
            try: winsound.Beep(int(command_.split(' ')[1]), int(command_.split(' ')[2]))
            except ValueError or IndexError: None
        elif (command_ == 'abort'):
            os.abort()
        else:
            make_label(('ERROR:'), 'black', 'green', 20, 20)
            make_label(('COMMAND ', command_, ' DOES NOT EXIST'), 'black', 'green', 20, 40)
            make_label(('TYPE "HELP" FOR A LIST OF COMMANDS'), 'black', 'green', 20, 60)
    except IndexError or ValueError or RecursionError or OSError:
        make_label(('Shell error at ', uptime), 'black', 'green', 10, 10)

def make_label(text_, bg_, fg_, x_, y_):
    name = Label(HOS, text = text_, bg = bg_, fg = fg_)
    name.place(x = x_, y = y_)

def edit_calcv(str_, addon_, modify_):
    global cv1, cv2, ans, ope
    if (modify_ == True):
        if (str_ == cv1):
            cv1 = (cv1) + addon_
        elif (str_ == cv2):
            cv2 = str(cv2) + addon_
        elif (str_ == ans):
            ans = addon_
        elif (str_ == ope):
            ope = addon_
    elif (modify_ == False):
        if (str_ == cv1):
            cv1 = 0
        elif (str_ == cv2):
            cv2 = 0
        elif (str_ == ans):
            ans = 0
        elif (str_ == ope):
            ope = ''
    else:
        raise SyntaxError('FUNCTION: "edit_calcv" HAS TOOK AN INCORRECT TOKEN. CHECK YOUR SYNTAX.[edit_calcv(str_, addon_, modify_)]')

def roll(arg):                                                                                                                                                    # IMPROVE RPS APPLICATION INTERFACE #
    global rps_scores
    #1 = rock, 2 = paper, 3 = scissors
    computer_roll = random.randint(1, 3)
    if (computer_roll == 1):
        if (arg == 'r'):
            rps_scores[0] = int(rps_scores[0]) + 1
            rps_scores[1] = int(rps_scores[1]) + 1
        elif (arg == 'p'):
            rps_scores[0] = int(rps_scores[0]) + 1
        elif (arg == 's'):
            rps_scores[1] = int(rps_scores[1]) + 1
    elif (computer_roll == 2):
        if (arg == 'p'):
            rps_scores[0] = int(rps_scores[0]) + 1
            rps_scores[1] = int(rps_scores[1]) + 1
        elif (arg == 's'):
            rps_scores[0] = int(rps_scores[0]) + 1
        elif (arg == 'r'):
            rps_scores[1] = int(rps_scores[1]) + 1
    elif (computer_roll == 3):
        if (arg == 's'):
            rps_scores[0] = int(rps_scores[0]) + 1
            rps_scores[1] = int(rps_scores[1]) + 1
        elif (arg == 'r'):
            rps_scores[0] = int(rps_scores[0]) + 1
        elif (arg == 'p'):
            rps_scores[1] = int(rps_scores[1]) + 1
    main()
    if (computer_roll == 1):
        make_label('Computer rolled rock!', 'gray', 'white', 200, 60)
    elif (computer_roll == 2):
        make_label('Computer rolled paper!', 'gray', 'white', 200, 60)
    elif (computer_roll == 3):
        make_label('Computer rolled scissors!', 'gray', 'white', 200, 60)

def recolor(item, color):
    global screen
    global taskbar_color, desktop_color
    global buttons_color, foregnd_color
    if (item == 'taskbar'):
        taskbar_color = color
    elif (item == 'desktop'):
        desktop_color = color
    elif (item == 'buttons'):
        buttons_color = color
    elif (item == 'foregnd'):
        foregnd_color = color
    main()

#Login screen is temporarily disabled due to to development conveniences.

#screen = 'login'
screen = 'desktop'

def main():
    global ram0, ram1, ram2, ram3, ram4
    global ram5, ram6, ram7, ram8, ram9
    global runs, recursion_depth, version
    global taskbar_color, desktop_color
    global buttons_color, foregnd_color
    global width_, height_, search1, user
    global login_failed, stack_overflow
    global taskbar_visibility, notif_count
    global emails, command1, dev_email_sent
    global contexts, screen, cv1, cv2, ans
    global current_var, stage, ope, uptime
    global start, rps_scores, warning1
    global sysinfo_, commands_

    if ((user.lower()) != 'dev'):
        if (dev_email_sent == False):
            send_email('What is new in HOS v1.5.0?', 'no.reply', dev1email)
            dev_email_sent = True

        refresh_inbox()

        runs = runs + 1

        sys.setrecursionlimit(recursion_depth)

        cover = Canvas(HOS, width = (width_ - 5), height = (height_ - 5), bg = desktop_color)
        cover.place(x = 0, y = 0)

        if (screen != 'login'):
            taskbar = Canvas(HOS, width = (width_ - 5), height = 30, bg = taskbar_color)
            taskbar.place(x = 0, y = 765)
            taskbar_btn1 = Button(HOS, width = 3, text = 'HOS', bg = 'blue', fg = 'white', command = lambda: taskbar_toggle())
            taskbar_btn1.place(x = 5, y = (height_ - 30))
            taskbar_btn2 = Button(HOS, width = 20, text = 'Settings', bg = taskbar_color, fg = 'white', command = lambda: set_screen_to('settings'))
            taskbar_btn2.place(x = 40, y = (height_ - 30))
            taskbar_btn2 = Button(HOS, width = 20, text = 'Calculator', bg = taskbar_color, fg = 'white', command = lambda: set_screen_to('calculator'))
            taskbar_btn2.place(x = 195, y = (height_ - 30))
            taskbar_btn3 = Button(HOS, width = 20, text = 'Rock Paper Scissors!', bg = taskbar_color, fg = 'white', command = lambda: set_screen_to('rps'))
            taskbar_btn3.place(x = 350, y = (height_ - 30))
            taskbar_btn4 = Button(HOS, width = 20, text = 'Notepad', bg = taskbar_color, fg = 'white', command = lambda: set_screen_to('notepad'))
            taskbar_btn4.place(x = 350, y = (height_ - 30))
            taskbar_notifs = Button(HOS, width = 2, text = notif_count, bg = taskbar_color, fg = 'white', command = lambda: set_screen_to('inbox'))
            taskbar_notifs.place(x = 1550, y = (height_ - 30))

    #---------------------------------------------------------------------------------------MAIN APPLICATION DEFS---------------------------------------------------------------#
    #---------------------------------------------------------------------------------------MAIN APPLICATION DEFS---------------------------------------------------------------#
    #---------------------------------------------------------------------------------------MAIN APPLICATION DEFS---------------------------------------------------------------#
            
            if (screen == 'desktop'):
                Trash_shortcut_desktop = Button(HOS, text = 'Trash', bg = buttons_color, width = 7, height = 3, fg = 'white', command = lambda: set_screen_to('trash'))
                Trash_shortcut_desktop.place(x = 25, y = 25)
                Email_shortcut_desktop = Button(HOS, text = 'Inbox', bg = buttons_color, width = 7, height = 3, fg = 'white', command = lambda: set_screen_to('inbox'))
                Email_shortcut_desktop.place(x = 25, y = 100)
                Cmd_shortcut_desktop = Button(HOS, text = 'Shell', bg = buttons_color, width = 7, height = 3, fg = 'white', command = lambda: set_screen_to('cmd.exe'))
                Cmd_shortcut_desktop.place(x = 25, y = 175)
                Rps_shortcut_desktop = Button(HOS, text = '''
Rock
Paper
Scissors
                ''', bg = buttons_color, width = 7, height = 3, fg = 'white', command = lambda: set_screen_to('rps'))
                Rps_shortcut_desktop.place(x = 25, y = 250)

            if (screen == 'notepad'):
                make_cover(desktop_color)
            
            if (screen == 'settings'):
                make_cover('gray')
                colorprefs = Button(HOS, text = 'Color prefrences', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('settings/colorprefs'))
                colorprefs.place(x = 25, y = 25)
                sysinfo = Button(HOS, text = 'System information', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('settings/sysinfo'))
                sysinfo.place(x = 25, y = 55)
                emailinfo = Button(HOS, text = 'Email information', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('settings/emailinfo'))
                emailinfo.place(x = 25, y = 85)
                
            elif (screen == 'settings/colorprefs'):
                make_cover('gray')
                tca = Button(HOS, text = 'Taskbar coloration', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('settings/colorprefs/taskbar'))
                tca.place(x = 25, y = 25)
                bca = Button(HOS, text = 'Button coloration', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('settings/colorprefs/buttons'))
                bca.place(x = 25, y = 55)
                dca = Button(HOS, text = 'Home screen coloration', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('settings/colorprefs/desktop'))
                dca.place(x = 25, y = 85)
                
            elif (screen == 'settings/colorprefs/taskbar'):
                make_cover('gray')
                green_ = Button(HOS, text = 'Change taskbar color to green', bg = 'green', command = lambda: recolor('taskbar', 'green'))
                green_.place(x = 25, y = 25)
                blue_ = Button(HOS, text = 'Change taskbar color to blue', bg = 'blue', command = lambda: recolor('taskbar', 'blue'))
                blue_.place(x = 25, y = 55)
                orange_ = Button(HOS, text = 'Change taskbar color to orange', bg = 'orange', command = lambda: recolor('taskbar', 'orange'))
                orange_.place(x = 25, y = 85)
                purple_ = Button(HOS, text = 'Change taskbar color to purple', bg = 'purple', command = lambda: recolor('taskbar', 'purple'))
                purple_.place(x = 25, y = 115)
                gray_ = Button(HOS, text = 'Change taskbar color to gray', bg = 'gray', command = lambda: recolor('taskbar', 'gray'))
                gray_.place(x = 25, y = 145)
                lightblue_ = Button(HOS, text = 'Change taskbar color to light blue', bg = 'lightblue', command = lambda: recolor('taskbar', 'lightblue'))
                lightblue_.place(x = 25, y = 175)
                black_ = Button(HOS, text = 'Change taskbar color to black', fg = 'white', bg = 'black', command = lambda: recolor('taskbar', 'black'))
                black_.place(x = 25, y = 205)
                back = Button(HOS, text = '<--', bg = 'gray', fg = 'black', command = lambda: set_screen_to('settings/colorprefs'))
                back.place(x = 500, y = 25)
                
            elif (screen == 'settings/colorprefs/buttons'):
                make_cover('gray')
                green_ = Button(HOS, text = 'Change button color to green', bg = 'green', command = lambda: recolor('button', 'green'))
                green_.place(x = 25, y = 25)
                blue_ = Button(HOS, text = 'Change button color to blue', bg = 'blue', command = lambda: recolor('button', 'blue'))
                blue_.place(x = 25, y = 55)
                orange_ = Button(HOS, text = 'Change button color to orange', bg = 'orange', command = lambda: recolor('button', 'orange'))
                orange_.place(x = 25, y = 85)
                purple_ = Button(HOS, text = 'Change button color to purple', bg = 'purple', command = lambda: recolor('button', 'purple'))
                purple_.place(x = 25, y = 115)
                gray_ = Button(HOS, text = 'Change button color to gray', bg = 'gray', command = lambda: recolor('button', 'gray'))
                gray_.place(x = 25, y = 145)
                lightblue_ = Button(HOS, text = 'Change button color to light blue', bg = 'lightblue', command = lambda: recolor('button', 'lightblue'))
                lightblue_.place(x = 25, y = 175)
                back = Button(HOS, text = '<--', bg = 'gray', fg = 'black', command = lambda: set_screen_to('settings/colorprefs'))
                back.place(x = 500, y = 25)
                
            elif (screen == 'settings/colorprefs/desktop'):
                make_cover('gray')
                green_ = Button(HOS, text = 'Change desktop color to green', bg = 'green', command = lambda: recolor('desktop', 'green'))
                green_.place(x = 25, y = 25)
                blue_ = Button(HOS, text = 'Change desktop color to blue', bg = 'blue', command = lambda: recolor('desktop', 'blue'))
                blue_.place(x = 25, y = 55)
                orange_ = Button(HOS, text = 'Change desktop color to orange', bg = 'orange', command = lambda: recolor('desktop', 'orange'))
                orange_.place(x = 25, y = 85)
                purple_ = Button(HOS, text = 'Change desktop color to purple', bg = 'purple', command = lambda: recolor('desktop', 'purple'))
                purple_.place(x = 25, y = 115)
                gray_ = Button(HOS, text = 'Change desktop color to gray', bg = 'gray', command = lambda: recolor('desktop', 'gray'))
                gray_.place(x = 25, y = 145)
                lightblue_ = Button(HOS, text = 'Change desktop color to light blue', bg = 'lightblue', command = lambda: recolor('desktop', 'lightblue'))
                lightblue_.place(x = 25, y = 175)
                back = Button(HOS, text = '<--', bg = 'gray', fg = 'black', command = lambda: set_screen_to('settings/colorprefs'))
                back.place(x = 500, y = 25)
            
            elif (screen == 'settings/sysinfo'):
                make_cover('gray')
                cmdI = Button(HOS, text = 'Interactive command shell', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('cmd.exe'))
                cmdI.place(x = 25, y = 25)
                copyright_ = Button(HOS, text = 'Copyleft', bg = buttons_color, fg = 'white', command = lambda: set_screen_to('settings/sysinfo/copyleft'))
                copyright_.place(x = 25, y = 55)

            elif (screen == 'settings/emailinfo'):
                make_cover('gray')
                make_label(('Local email server: ', 'harrisonOS.net'), 'gray', 'black', 20, 20)
                make_label(('Current email count: ', notif_count), 'gray', 'black', 20, 40)

            elif (screen == 'settings/sysinfo/copyleft'):
                make_cover('gray')
                make_label((sysinfo_), 'gray', 'black', 20, 20)
                
            elif (screen == 'cmd.exe'):
                make_cover('black')
                icm = Entry(HOS, width = 100, bg = 'darkgray')
                icm.place(x = 37, y = 737.5)
                icme = Button(HOS, text = '>>>', width = 3, bg = 'black', fg = 'green', command = lambda: cmd_interperet(icm))
                icme.place(x = 5, y = 735)

            elif (screen == 'inbox'):
                make_cover('lightgray')
                Topbar_1 = Canvas(HOS, width = (width_ - 5), height = (75), bg = 'white')
                Topbar_1.place(x = 0, y = 0)
                is_01 = Button(HOS, width = 100, text = (emails[0]), bg = 'gray', fg = 'white', command = lambda: view_email(1))
                is_01.place(x = 20, y = 100)
                is_02 = Button(HOS, width = 100, text = (emails[1]), bg = 'gray', fg = 'white', command = lambda: view_email(2))
                is_02.place(x = 20, y = 130)
                is_03 = Button(HOS, width = 100, text = (emails[2]), bg = 'gray', fg = 'white', command = lambda: view_email(3))
                is_03.place(x = 20, y = 160)
                is_04 = Button(HOS, width = 100, text = (emails[3]), bg = 'gray', fg = 'white', command = lambda: view_email(4))
                is_04.place(x = 20, y = 190)
                is_05 = Button(HOS, width = 100, text = (emails[4]), bg = 'gray', fg = 'white', command = lambda: view_email(5))
                is_05.place(x = 20, y = 220)
                is_06 = Button(HOS, width = 100, text = (emails[5]), bg = 'gray', fg = 'white', command = lambda: view_email(6))
                is_06.place(x = 20, y = 250)
                is_07 = Button(HOS, width = 100, text = (emails[6]), bg = 'gray', fg = 'white', command = lambda: view_email(7))
                is_07.place(x = 20, y = 280)
                is_08 = Button(HOS, width = 100, text = (emails[7]), bg = 'gray', fg = 'white', command = lambda: view_email(8))
                is_08.place(x = 20, y = 310)
                is_09 = Button(HOS, width = 100, text = (emails[8]), bg = 'gray', fg = 'white', command = lambda: view_email(9))
                is_09.place(x = 20, y = 340)
                is_10 = Button(HOS, width = 100, text = (emails[9]), bg = 'gray', fg = 'white', command = lambda: view_email(10))
                is_10.place(x = 20, y = 370)
                is_11 = Button(HOS, width = 100, text = (emails[10]), bg = 'gray', fg = 'white', command = lambda: view_email(11))
                is_11.place(x = 20, y = 400)
                is_12 = Button(HOS, width = 100, text = (emails[11]), bg = 'gray', fg = 'white', command = lambda: view_email(12))
                is_12.place(x = 20, y = 430)
                is_13 = Button(HOS, width = 100, text = (emails[12]), bg = 'gray', fg = 'white', command = lambda: view_email(13))
                is_13.place(x = 20, y = 460)
                is_14 = Button(HOS, width = 100, text = (emails[13]), bg = 'gray', fg = 'white', command = lambda: view_email(14))
                is_14.place(x = 20, y = 490)
                is_15 = Button(HOS, width = 100, text = (emails[14]), bg = 'gray', fg = 'white', command = lambda: view_email(15))
                is_15.place(x = 20, y = 520)
                is_16 = Button(HOS, width = 100, text = (emails[15]), bg = 'gray', fg = 'white', command = lambda: view_email(16))
                is_16.place(x = 20, y = 550)
                is_17 = Button(HOS, width = 100, text = (emails[16]), bg = 'gray', fg = 'white', command = lambda: view_email(17))
                is_17.place(x = 20, y = 580)
                is_18 = Button(HOS, width = 100, text = (emails[17]), bg = 'gray', fg = 'white', command = lambda: view_email(18))
                is_18.place(x = 20, y = 610)
                is_19 = Button(HOS, width = 100, text = (emails[18]), bg = 'gray', fg = 'white', command = lambda: view_email(19))
                is_19.place(x = 20, y = 640)
                is_20 = Button(HOS, width = 100, text = (emails[19]), bg = 'gray', fg = 'white', command = lambda: view_email(20))
                is_20.place(x = 20, y = 670)
                Delete_all = Button(HOS, text = 'Clear inbox', bg = 'white', command = lambda: delete_inbox())
                Delete_all.place(x = 10, y = 10)
                Total_emails = Label(HOS, bg = 'white', text = ('Total emails: ', notif_count, '      Total empty slots: ', (20 - int(notif_count))))
                Total_emails.place(x = 100, y = 13)
                Create_email = Button(HOS, text = 'Create new email', bg = 'white', command = lambda: set_screen_to('build_new_email'))
                Create_email.place(x = 370, y = 10)
                Test_email = Button(HOS, text = 'Send a test email', bg = 'white', command = lambda: send_email('Test email', 'Test', 'This is a test email'))
                Test_email.place(x = 500, y = 10)
                Refresh_inbox = Button(HOS, text = 'Refresh inbox', bg = 'white', command = lambda: main())
                Refresh_inbox.place(x = 625, y = 10)
                
            elif (screen == 'build_new_email'):
                make_cover('lightgray')
                subject_label = Label(HOS, bg = 'lightgray', text = 'Subject:')
                subject_label.place(x = 30, y = 30)
                subject_entry = Entry(HOS, bg = 'lightgray', width = 30)
                subject_entry.place(x = 100, y = 30)
                from_label = Label(HOS, bg = 'lightgray', text = 'From:')
                from_label.place(x = 30, y = 60)
                from_entry = Entry(HOS, bg = 'lightgray', width = 30)
                from_entry.place(x = 100, y = 60)
                message_label = Label(HOS, bg = 'lightgray', text = 'Message:')
                message_label.place(x = 30, y = 90)
                message_entry1 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry1.place(x = 100, y = 90)
                message_entry2 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry2.place(x = 100, y = 110)
                message_entry3 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry3.place(x = 100, y = 130)
                message_entry4 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry4.place(x = 100, y = 150)
                message_entry5 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry5.place(x = 100, y = 170)
                message_entry6 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry6.place(x = 100, y = 190)
                message_entry7 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry7.place(x = 100, y = 210)
                message_entry8 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry8.place(x = 100, y = 230)
                message_entry9 = Entry(HOS, bg = 'lightgray', width = 100)
                message_entry9.place(x = 100, y = 250)
                send_button = Button(HOS, text = ' Send ', bg = 'lightgray', command = lambda: gather_1(message_entry1, message_entry2, message_entry3, message_entry4, message_entry5, message_entry6, message_entry7, message_entry8,
                                                                                                        message_entry9) or send_email((subject_entry.get()), (from_entry.get()), (message_)) or set_screen_to('inbox'))
                send_button.place(x = 30, y = 3)

            elif (screen == 'regedit'):
                make_cover('gray')
                make_label(('Module: ', webbrowser), 'gray', 'black', 20, 20)
                make_label(('Module: ', winsound), 'gray', 'black', 20, 40)
                make_label(('Module: ', tkinter), 'gray', 'black', 20, 60)
                make_label(('Module: ', parser), 'gray', 'black', 20, 80)
                make_label(('Module: ', random), 'gray', 'black', 20, 100)
                make_label(('Module: ', time), 'gray', 'black', 20, 120)
                make_label(('Module: ', math), 'gray', 'black', 20, 140)
                make_label(('Module: ', sys), 'gray', 'black', 20, 160)
                make_label(('Module: ', os), 'gray', 'black', 20, 180)
                make_label(('Email assignments 1-10:', emails[0], emails[1], emails[2], emails[3], emails[4], emails[5], emails[6], emails[7], emails[8], emails[9]), 'gray', 'black', 20, 200)
                make_label(('Email assignments 11-20:', emails[10], emails[11], emails[12], emails[13], emails[14], emails[15], emails[16], emails[17], emails[18], emails[19]), 'gray', 'black', 20, 220)
                make_label(('RAM variables 1-10: ', ram0, ram1, ram2, ram3, ram4, ram5, ram6, ram7, ram8, ram9), 'gray', 'black', 20, 240)
                make_label(('Variables [login_failed, stack_overflow]: ', login_failed, stack_overflow), 'gray', 'black', 20, 260)
                make_label(('Variables [taskbar_visibility, dev_email_sent] ',taskbar_visibility , dev_email_sent), 'gray', 'black', 20, 280)
                make_label(('Variable localtime: ', localtime()), 'gray', 'black', 20, 300)

            elif (screen == 'rps'):
                make_cover('gray')
                r = Button(HOS, text = 'Roll rock', fg = 'white', bg = 'black', command = lambda: roll('r'))
                r.place(x = 20, y = 20)
                p = Button(HOS, text = 'Roll paper', fg = 'white', bg = 'black', command = lambda: roll('p'))
                p.place(x = 20, y = 60)
                s = Button(HOS, text = 'Roll scissors', fg = 'white', bg = 'black', command = lambda: roll('s'))
                s.place(x = 20, y = 100)
                make_label(("Human's score: ", (rps_scores[0])), 'gray', 'black', 200, 20)
                make_label(("Computer's score: ", (rps_scores[1])), 'gray', 'black', 200, 40)

            elif (screen == 'calculator'):
                calccnv = Canvas(HOS, width = 300, height = 600, bg = 'gray')
                calccnv.place(x = 0, y = 0)
                def add(arg, path):
                    global cv1, cv2, current_var
                    if (path == False):
                        if (current_var[0] == False and current_var[1] == True):cv2 = str(cv2) + str(arg)
                        elif (current_var[1] == False and current_var[0] == True):cv1 = str(cv1) + str(arg)
                        else:raise SyntaxError('////  INVALID VALUES  ////')
                    elif (path == True):
                        if (arg == 'pi'):
                            if (current_var[0] == False and current_var[1] == True):cv2 = str(cv2) + str(math.pi)
                            elif (current_var[1] == False and current_var[0] == True):cv1 = str(cv2) + str(math.pi)
                    elif (path.lower() == 'else'):
                        if (current_var[0] == False and current_var[1] == True):cv2 = ''
                        elif (current_var[1] == False and current_var[0] == True):cv1 = ''
                    else:raise SyntaxError('////  INVALID VALUE FOR path. MUST BE True Or False or Else  ////')
                    main()

                def operation(arg):
                    global ope
                    if (arg == '/' or arg == '+' or arg == '-' or arg == '*' or arg == '**'):ope = str(arg)
                    else:raise SyntaxError('////  INVALID OPERATION. MUST BE [/, -, +, *, **]  ////')
                    main()

                def switch_entry():
                    global current_var
                    if (current_var[1] == False and current_var[0] == True):current_var = [False, True]
                    elif (current_var[1] == True and current_var[0] == False):current_var = [True, False]
                    else:current_var = [True, False]
                    main()

                def stage_equals(arg):
                    global stage
                    stage = str(arg)
                    main()

                def solve():
                    global ope, cv1, cv2, ans
                    try:
                        ans = ''
                        if (ope == '+'):
                            ans = str(ans) + str(cv1) + ' ' + str(ope) + ' ' + str(cv2) + ' = ' + str(int(cv1) + int(cv2))
                        elif (ope == '-'):
                            ans = str(ans) + str(cv1) + ' ' + str(ope) + ' ' + str(cv2) + ' = ' + str(int(cv1) - int(cv2))
                        elif (ope == '/'):
                            ans = str(ans) + str(cv1) + ' ' + str(ope) + ' ' + str(cv2) + ' = ' + str(int(cv1) / int(cv2))
                        elif (ope == '*'):
                            ans = str(ans) + str(cv1) + ' ' + str(ope) + ' ' + str(cv2) + ' = ' + str(int(cv1) * int(cv2))
                        elif (ope == '**'):
                            ans = str(ans) + str(cv1) + ' ' + str(ope) + ' ' + str(cv2) + ' = ' + str(int(cv1) ** int(cv2))
                    except ValueError or IndexError or ArithmeticError:ans = 'Error'
                    main()

                def clear(arg):
                    global ope, cv1, cv2, ans, current_var
                    if (arg == True):
                        ope = ''
                        cv1 = ''
                        cv2 = ''
                        ans = ''
                        current_var = [True, False]
                    main()

                def cmain():
                    global cv1, cv2, ans, ope, current_var, stage
                    _screen = Canvas(HOS, width = 295, height = 200, bg = 'black')
                    _screen.place(x = 0, y = 0)
                    enter = Button(HOS, text = 'Enter', width = 6, fg = 'white', bg = 'gray', command = lambda: switch_entry())
                    enter.place(x = 170, y = 210)
                    graph = Button(HOS, text = 'Graph', width = 6, fg = 'white', bg = 'gray', command = lambda: stage_equals('graph'))
                    graph.place(x = 170, y = 250)
                    exec_ = Button(HOS, text = 'Solve', width = 6, fg = 'white', bg = 'gray', command = lambda: solve())
                    exec_.place(x = 170, y = 330)
                    home = Button(HOS, text = 'Home', width = 6, fg = 'white', bg = 'gray', command = lambda: stage_equals('main'))
                    home.place(x = 170, y = 290)
                    clr = Button(HOS, width = 6, bg = 'gray', fg = 'white', text = 'Clear', command = lambda: clear(True))
                    clr.place(x = 170, y = 370)
                    _1 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '1', command = lambda: add('1', False))
                    _1.place(x = 10, y = 210)
                    _2 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '2', command = lambda: add('2', False))
                    _2.place(x = 50, y = 210)
                    _3 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '3', command = lambda: add('3', False))
                    _3.place(x = 90, y = 210)
                    _4 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '4', command = lambda: add('4', False))
                    _4.place(x = 10, y = 250)
                    _5 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '5', command = lambda: add('5', False))
                    _5.place(x = 50, y = 250)
                    _6 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '6', command = lambda: add('6', False))
                    _6.place(x = 90, y = 250)
                    _7 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '7', command = lambda: add('7', False))
                    _7.place(x = 10, y = 290)
                    _8 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '8', command = lambda: add('8', False))
                    _8.place(x = 50, y = 290)
                    _9 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '9', command = lambda: add('9', False))
                    _9.place(x = 90, y = 290)
                    _0 = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '0', command = lambda: add('0', False))
                    _0.place(x = 50, y = 330)
                    _dot = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '.', command = lambda: add('.', False))
                    _dot.place(x = 10, y = 330)
                    _del = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = 'DEL', command = lambda: add('', 'ELSE'))
                    _del.place(x = 90, y = 330)
                    _pi = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = 'PI', command = lambda: add('pi', True))
                    _pi.place(x = 10, y = 370)
                    _addition = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '+', command = lambda: operation('+'))
                    _addition.place(x = 130, y = 210)
                    _division = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '/', command = lambda: operation('/'))
                    _division.place(x = 130, y = 250)
                    _subtraction = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '-', command = lambda: operation('-'))
                    _subtraction.place(x = 130, y = 290)
                    _multiplication = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '*', command = lambda: operation('*'))
                    _multiplication.place(x = 130, y = 330)
                    _power = Button(HOS, width = 3, bg = 'gray', fg = 'white', text = '^', command = lambda: operation('**'))
                    _power.place(x = 130, y = 370)
                    if (stage == 'main'):
                        line1 = Label(HOS, bg = 'black', fg = 'white', text = cv1)
                        line1.place(x = 10, y = 10)
                        line2 = Label(HOS, bg = 'black', fg = 'white', text = cv2)
                        line2.place(x = 10, y = 30)
                        line3 = Label(HOS, bg = 'black', fg = 'white', text = ans)
                        line3.place(x = 10, y = 50)
                        if (current_var == [True, False]):
                            a = Label(HOS, bg = 'black', fg = 'white', text = '<--')
                            a.place(x = 270, y = 10)
                        elif (current_var == [False, True]):
                            a = Label(HOS, bg = 'black', fg = 'white', text = '<--')
                            a.place(x = 270, y = 30)
                cmain()


    #---------------------------------------------------------------------------------------MAIN APPLICATION DEFS---------------------------------------------------------------#
    #---------------------------------------------------------------------------------------MAIN APPLICATION DEFS---------------------------------------------------------------#
    #---------------------------------------------------------------------------------------MAIN APPLICATION DEFS---------------------------------------------------------------#
            
            #The following windows are overlays - they must come after initial screen applications are created.
            if (taskbar_visibility == True):
                popup = Canvas(HOS, width = (width_ / 10), height = (height_ / 3), bg = taskbar_color)
                popup.place(x = 5, y = 495)
                popup_home = Button(HOS, text = 'Home', bg = taskbar_color, fg = 'white', command = lambda: set_screen_to('desktop'))
                popup_home.place(x = 10, y = 500)
                popup_settings = Button(HOS, text = 'Settings', bg = taskbar_color, fg = 'white', command = lambda: set_screen_to('settings'))
                popup_settings.place(x = 10, y = 530)
                popup_entry = Entry(HOS, width = 17, bg = 'lightgray')
                popup_entry.place(x = 10, y = 740)
                popup_search = Button(HOS, text = 'Search', bg = taskbar_color, fg = 'white', command = lambda: search(popup_entry))
                popup_search.place(x = 117.5, y = 737)

            if (runs >= (int(sys.getrecursionlimit()))):
                warning_p1 = Canvas(HOS, width = 500, height = 200, bg = 'red')
                warning_p1.place(x = 280, y = 180)
                warning_p2 = Label(HOS, text = warning_1, bg = 'red', fg = 'black')
                warning_p2.place(x = 330, y = 200)
                winsound.MessageBeep(10)

            if (runs >= ((int(sys.getrecursionlimit())) + (((int(sys.getrecursionlimit())) / 20)))): os.abort()
            
        elif (screen == 'login'):
            username_text = Label(HOS, bg = desktop_color, text = 'Username:', fg = foregnd_color)
            username_text.place(x = ((width_ + 25) / 2), y = ((height_ - 50) / 2))
            user_entry = Entry(HOS, width = 40)
            user_entry.place(x = ((width_ - 150) / 2), y = ((height_ - 5) / 2))
            username_accept = Button(HOS, bg = desktop_color, fg = foregnd_color, text = 'Login', command = lambda: get_text(user_entry, 'login'))
            username_accept.place(x = ((width_ + 50) / 2), y = ((height_ + 40) / 2))
    if ((user.lower()) == 'dev'):
        screen = 'dev_console'
        make_cover('black')
        icm = Entry(HOS, width = 100, bg = 'darkgray')
        icm.place(x = 37, y = 737.5)
        icme = Button(HOS, text = '>>>', width = 3, bg = 'black', fg = 'green', command = lambda: cmd_interperet(icm))
        icme.place(x = 5, y = 735)
    HOS.mainloop()

main()

#1038 Lines of code scripted by a 13 year old. :D
