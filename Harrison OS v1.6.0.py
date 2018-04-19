#<PYv3.5.0>
#<OS>
#color codes: https://www.bing.com/images/search?view=detailV2&ccid=c2vcyswu&id=984D994C3CE73F68872EF9AD206441CDA215EED4&thid=OIP.c2vcyswudIpUXn1EftxIFwHaFT&mediaurl=http%3a%2f%2fwww.cs.washington.edu%2feducation%2fcourses%2fcse142%2f08su%2fpython%2fpython_colors.png&exph=861&expw=1201&q=python+color+codes&simid=608021634515208567&selectedIndex=12&ajaxhist=0

#.txt documents are for notepad
#.eml files are for email
#.mp3 files are for winsound usage
#.exe files are executable document scripts

#add a random number generator in the calculator section

###################################################################################################################IMPORTS#
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
###################################################################################################################IMPORTS#
#############################################################################################################VARIABLES-DEF#
screen = 'login'
ram01 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram02 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram03 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram04 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram05 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram06 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram07 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram08 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram09 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram10 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram11 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram12 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram13 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram14 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram15 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram16 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram17 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram18 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram19 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
ram20 = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] #31 slots of RAM
_collective_ram_ = [ram01, ram02, ram03, ram04, ram05, ram06, ram07, ram08, ram09, ram10, ram11, ram12, ram13, ram14, ram15, ram16, ram17, ram18, ram19, ram20]
recursiondepthlimit = 400
applications = 'desktop settings email notepad cmd files calculator trash music'
startbarvisible = False
modulesincludedwithOS = 'webbrowser winsound tkinter parser random time math sys os'
bottomrightcornernotificationcount = 0
currentsystemtime = ['00', ':', '00', '-', '00', '/', '00', '/', '0000']
emailcontext01 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext02 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext03 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext04 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext05 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext06 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext07 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext08 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext09 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext10 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext11 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext12 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext13 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext14 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext15 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext16 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext17 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext18 = ['SENDER', 'HEADING', 'MESSAGE']
emailcontext19 = ['SENDER', 'HEADING', 'MESSAGE']
runs = 0
hourmode = '12HR'
filesall = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
line1 = 0
line2 = 0
line3 = 0
line4 = 0
line5 = 0
#                       Line1 Line2  Error Operation
calculatorstatusinfo = [True, False, None, None]
#############################################################################################################VARIABLES-DEF#
#############################################################################################################VARIABLES-LST#
info = '''
Current running OS: HarrisonOS V1.6.0
Copyleft: Harrison Lindgren
Native language: Python 3.5.0 [IDLE]
'''
welcomeemail = '''
Welcome to HarrisonOS v1.6.0!

Thank you for using our product.
In this new version of HarrisonOS, there have been many improvments
from the previous version[s]. To get started, due to the new parser
searching for apps and using textboxes should be much easier now so
that you will have a smoother experience. There is also much more
ram added to the OS so now settings and applications will be replinished
to their previous state [more ram = more memory].
'''
cmdcommands = '''
NETSTAT == GIVES STATISTICS OF THE NATIVE ENVIRONMENT
PY.EXE -E /PYTHON COMMAND/ == EXCEUTES A PYTHON COMMAND IN THE LAUNCH WINDOW
PY.EXE -W /TEXT/ == PRINTS THE DESIRED TEXT IN THE NATIVE LAUNCHER
LOCAL RAM_DUMP == PRINTS THE STATUS OF RAM SCRIPT MEMORY
SYS_RUNS == PRINTS THE SYSTEM RUNTIME COUNT
LOCAL -O /APPLICATION_NAME/ == OPENS THE DESIRED APPLICATION
BEEP [FREQ] [MILLISECONDS] == MAKES A BEEP USING WINSOUND
ABORT == EXITS THE HarrisonOS APPLICATION
EXIT == EXITS THE COMMAND SHELL
'''
bsodtext = '''
A CRITICAL ERROR HAS OCCURED ON THE HARRISON-OS OPERATING SYSTEM WHICH YOU
ARE CURRENTLY USING. THIS HAS CAUSED YOUR PC TO SHUT DOWN. THIS IS[3] MOST
LIKELY BECAUSE THERE WAS A BYPASSED EXEPTION IN THE SOURCE CODE. ERROR NO:
'''
#############################################################################################################VARIABLES-LST#
###################################################################################################################OS-INIT#
OS = Tk()
OS.configure(bg = 'gray18')
OS.title('Harrison OS V1.6.0')
OS.maxsize(width = 1580, height = 800)
OS.minsize(width = 1580, height = 800)
###################################################################################################################OS-INIT#
############################################################################################################CLASS-FUNCTION#
class _os_():
    def _main_():
        global ram01, ram02, ram03, ram04, ram05, ram06, ram07, ram08, ram09, ram10
        global ram11, ram12, ram13, ram14, ram15, ram16, ram17, ram18, ram19, ram20
        global screen, recursiondepthlimit, applications, info, welcomeemail
        global startbarvisible, modulesincludedwithOS, cmdcommands, runs, hourmode
        global bottomrightcornernotificationcount, currentsystemtime, filesall
        global emailcontext01, emailcontext02, emailcontext03, emailcontext04, emailcontext05, emailcontext06, emailcontext07, emailcontext08, emailcontext09, emailcontext10
        global emailcontext11, emailcontext12, emailcontext13, emailcontext14, emailcontext15, emailcontext16, emailcontext17, emailcontext18, emailcontext19
        global calculatorstatusinfo, _collective_ram_
        sys.setrecursionlimit(recursiondepthlimit)
        _os_._cover_('gray18')
        _os_._taskbar_()
        _os_._email_._emailcountupdate_()
        _os_._gathertimeinfo_()
        runs += 1
        if screen == 'desktop':
            trashwidget_ = Button(OS, height = 4, width = 10, text = '''

 |  |
  --
TRASH BIN
''', fg = 'white', bg = 'black', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('trash'))
            trashwidget_.place(x = 30, y = 30)
            cmdwidget_ = Button(OS, height = 4, width = 10, text = '''

>>>_/

CMD.exe
''', fg = 'white', bg = 'black', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('cmd'))
            cmdwidget_.place(x = 30, y = 130)
            emailwidget_ = Button(OS, height = 4, width = 10, text = '''
 ___
[_E_]

INBOX
''', fg = 'white', bg = 'black', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('email'))
            emailwidget_.place(x = 30, y = 230)
            calcwidget_ = Button(OS, height = 4, width = 10, text = '''

 + - =

CALUCLATOR
''', fg = 'white', bg = 'black', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('calculator'))
            calcwidget_.place(x = 30, y = 330)
            musicwidget_ = Button(OS, height = 4, width = 10, text = '''

<.mp3>

MUSIC
''', fg = 'white', bg = 'black', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('music'))
            musicwidget_.place(x = 30, y = 430)
            notepadwidget_ = Button(OS, height = 4, width = 10, text = '''
~~~~~~
~~~~~~

NOTEPAD
''', fg = 'white', bg = 'black', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('notepad'))
            notepadwidget_.place(x = 30, y = 530)
            fileswidget_ = Button(OS, height = 4, width = 10, text = '''
<.txt>
<.eml>

FILES
''', fg = 'white', bg = 'black', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('files'))
            fileswidget_.place(x = 30, y = 630)
        if screen == 'login':
            cover = Canvas(OS, width = 1580, height = 800, highlightthickness = 0, bg = 'gray70')
            cover.place(x = 0, y = 0)
            _os_._createmisclabel_(OS, ('Username:'), 'gray70', 'black', 775, 375)
            usernameentry = Entry(OS, width = 50)
            usernameentry.place(x = 650, y = 400)
            login = Button(OS, text = 'Login', command = lambda: _os_._screenset_('desktop'), activebackground = 'black', activeforeground = 'black', borderwidth = 1)
            login.place(x = 780, y = 430)
        if screen == 'music':
            _os_._cover_('purple4')
            xb__ = Button(OS, text = 'X', bg = 'purple4', fg = 'white', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'purple4', activeforeground = 'white')
            xb__.place(x = 1565, y = 0)
        if screen == 'cmd':
            _os_._cover_('gray9')
            commandlineentryaccept = Button(OS, text = '>>>', width = 3, bg = 'gray9', fg = 'green3', borderwidth = 0, activebackground = 'gray9', activeforeground = 'green3', command = lambda: _os_._cmdcommand_(str(commandlineentry.get())))
            commandlineentryaccept.place(x = 10, y = 717.5)
            commandlineentry = Entry(OS, bg = 'gray72', width = 50)
            commandlineentry.place(x = 50, y = 720)
        if screen == 'trash':
            _os_._cover_('gray54')
            xb__ = Button(OS, text = 'X', bg = 'gray54', fg = 'black', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'gray54', activeforeground = 'black')
            xb__.place(x = 1565, y = 0)
        if screen == 'settings':
            _os_._cover_('gray45')
            settingbuttonsetscreensystem = Button(OS, text = 'System settings', bg = 'gray45', fg = 'white', borderwidth = 0, activebackground = 'gray45', activeforeground = 'white', command = lambda: _os_._screenset_('settings/system'))
            settingbuttonsetscreensystem.place(x = 20, y = 20)
            settingbuttonsetscreentime = Button(OS, text = 'Time settings', bg = 'gray45', fg = 'white', borderwidth = 0, activebackground = 'gray45', activeforeground = 'white', command = lambda: _os_._screenset_('settings/time'))
            settingbuttonsetscreentime.place(x = 20, y = 50)
            settingbuttonsetscreensshell = Button(OS, text = 'Command line', bg = 'gray45', fg = 'white', borderwidth = 0, activebackground = 'gray45', activeforeground = 'white', command = lambda: _os_._screenset_('cmd'))
            settingbuttonsetscreensshell.place(x = 20, y = 80)
            settingbuttonsetscreenfiles = Button(OS, text = 'Files', bg = 'gray45', fg = 'white', borderwidth = 0, activebackground = 'gray45', activeforeground = 'white', command = lambda: _os_._screenset_('files'))
            settingbuttonsetscreenfiles.place(x = 20, y = 110)
            settingbuttonsetscreenprefs = Button(OS, text = 'Preferences', bg = 'gray45', fg = 'white', borderwidth = 0, activebackground = 'gray45', activeforeground = 'white', command = lambda: _os_._screenset_('settings/prefs'))
            settingbuttonsetscreenprefs.place(x = 20, y = 140)
            xb__ = Button(OS, text = 'X', bg = 'gray45', fg = 'black', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'gray45', activeforeground = 'black')
            xb__.place(x = 1565, y = 0)
        if screen == 'settings/time':
            _os_._cover_('gray45')
            _os_._createmisclabel_(OS, ('Time setting[s] information:'), 'gray45', 'black', 20, 20)
            _os_._createmisclabel_(OS, ('-Current time mode = '), 'gray45', 'black', 20, 60)
            _os_._createmisclabel_(OS, (hourmode), 'gray45', 'black', 140, 60)
            switchtimestatbutton = Button(OS, text = '-Click here to switch time mode', command = lambda: _os_._switchtime_(), borderwidth = 0, activebackground = 'gray45', activeforeground = 'black', bg = 'gray45', fg = 'black')
            switchtimestatbutton.place(x = 20, y = 80)
            _os_._createmisclabel_(OS, ('-Current OS time: ' + str(currentsystemtime)), 'gray45', 'black', 20, 100)
            _os_._createmisclabel_(OS, ('-Currtne unparsed native time: ' + str(localtime())), 'gray45', 'black', 20, 120)
            xb__ = Button(OS, text = 'X', bg = 'gray45', fg = 'black', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'gray45', activeforeground = 'black')
            xb__.place(x = 1565, y = 0)
        if screen == 'settings/system':
            _os_._cover_('gray45')
            xb__ = Button(OS, text = 'X', bg = 'gray45', fg = 'black', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'gray45', activeforeground = 'black')
            xb__.place(x = 1565, y = 0)
        if screen == 'settings/prefs':
            _os_._cover_('gray45')
            xb__ = Button(OS, text = 'X', bg = 'gray45', fg = 'black', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'gray45', activeforeground = 'black')
            xb__.place(x = 1565, y = 0)
        if screen == 'email':
            _os_._cover_('cyan2')
            email_top_cover = Canvas(OS, width = 1580, height = 150, highlightthickness = 0, bg = 'cyan4')
            email_top_cover.place(x = 0, y = 0)
            email_slot_01 = Button(OS, text = ((emailcontext01[0]) + '  -  ' + (emailcontext01[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(1), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_01.place(x = 20, y = 170)
            email_slot_02 = Button(OS, text = ((emailcontext02[0]) + '  -  ' + (emailcontext02[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(2), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_02.place(x = 20, y = 200)
            email_slot_03 = Button(OS, text = ((emailcontext03[0]) + '  -  ' + (emailcontext03[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(3), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_03.place(x = 20, y = 230)
            email_slot_04 = Button(OS, text = ((emailcontext04[0]) + '  -  ' + (emailcontext04[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(4), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_04.place(x = 20, y = 260)
            email_slot_05 = Button(OS, text = ((emailcontext05[0]) + '  -  ' + (emailcontext05[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(5), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_05.place(x = 20, y = 290)
            email_slot_06 = Button(OS, text = ((emailcontext06[0]) + '  -  ' + (emailcontext06[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(6), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_06.place(x = 20, y = 320)
            email_slot_07 = Button(OS, text = ((emailcontext07[0]) + '  -  ' + (emailcontext07[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(7), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_07.place(x = 20, y = 350)
            email_slot_08 = Button(OS, text = ((emailcontext08[0]) + '  -  ' + (emailcontext08[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(8), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_08.place(x = 20, y = 380)
            email_slot_09 = Button(OS, text = ((emailcontext09[0]) + '  -  ' + (emailcontext09[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(9), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_09.place(x = 20, y = 410)
            email_slot_10 = Button(OS, text = ((emailcontext10[0]) + '  -  ' + (emailcontext10[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(10), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_10.place(x = 20, y = 440)
            email_slot_11 = Button(OS, text = ((emailcontext11[0]) + '  -  ' + (emailcontext11[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(11), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_11.place(x = 20, y = 470)
            email_slot_12 = Button(OS, text = ((emailcontext12[0]) + '  -  ' + (emailcontext12[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(12), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_12.place(x = 20, y = 500)
            email_slot_13 = Button(OS, text = ((emailcontext13[0]) + '  -  ' + (emailcontext13[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(13), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_13.place(x = 20, y = 530)
            email_slot_14 = Button(OS, text = ((emailcontext14[0]) + '  -  ' + (emailcontext14[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(14), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_14.place(x = 20, y = 560)
            email_slot_15 = Button(OS, text = ((emailcontext15[0]) + '  -  ' + (emailcontext15[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(15), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_15.place(x = 20, y = 590)
            email_slot_16 = Button(OS, text = ((emailcontext16[0]) + '  -  ' + (emailcontext16[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(16), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_16.place(x = 20, y = 620)
            email_slot_17 = Button(OS, text = ((emailcontext17[0]) + '  -  ' + (emailcontext17[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(17), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_17.place(x = 20, y = 650)
            email_slot_18 = Button(OS, text = ((emailcontext18[0]) + '  -  ' + (emailcontext18[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(18), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_18.place(x = 20, y = 680)
            email_slot_19 = Button(OS, text = ((emailcontext19[0]) + '  -  ' + (emailcontext19[1])), bg = 'white', fg  = 'black', command = lambda: _os_._email_._viewemail_(19), borderwidth = 1, activebackground = 'white', activeforeground = 'gray83', width = 100)
            email_slot_19.place(x = 20, y = 710)
            _os_._createmisclabel_(OS, ('Inbox'), 'cyan4', 'black', 2, 2)
            testemail = Button(OS, text = 'Send a test email to me', command = lambda: _os_._email_._sendemail_('HarrisonOS.co', 'Test', 'This email is a test to see if your inbox is functional.'), borderwidth = 1, activebackground = 'cyan4', bg = 'cyan4', fg = 'black', activeforeground = 'black')
            testemail.place(x = 50, y = 20)
            testemail = Button(OS, text = 'Refresh inbox', command = lambda: _os_._main_(), borderwidth = 1, activebackground = 'cyan4', bg = 'cyan4', fg = 'black', activeforeground = 'black')
            testemail.place(x = 200, y = 20)
            xb__ = Button(OS, text = 'X', bg = 'cyan4', fg = 'black', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'cyan4', activeforeground = 'black')
            xb__.place(x = 1565, y = 0)
        if screen == 'notepad':
            notepadx = random.randint(100, 400)
            notepady = random.randint(100, 300)
            notepadbg = Canvas(OS, bg = 'gray45', width = 600, height = 300, highlightthickness = 1)
            notepadbg.place(x = notepadx, y = notepady)
            notepadxbutton = Button(OS, command = lambda: _os_._screenset_('desktop'), text = 'X', fg = 'white', bg = 'gray45', borderwidth = 0)
            notepadxbutton.place(x = (notepadx + 2), y = (notepady + 2))
            notepadtextsave = Button(OS, text = 'Save', bg = 'gray45', fg = 'green3', borderwidth = 0, command = lambda: _os_._files_._savefile_(str(filename_.get()), '.txt', [notepadline1.get(), notepadline2.get(),
                                                                                                                                                                                notepadline3.get(), notepadline4.get(),
                                                                                                                                                                                notepadline5.get(), notepadline6.get(),
                                                                                                                                                                                notepadline7.get(), notepadline8.get(),
                                                                                                                                                                                notepadline9.get()]))
                                                                                                                                                                                                                 #ALG_1
            notepadtextsave.place(x = (notepadx + 550), y = (notepady + 2))
            notepadtextopen = Button(OS, text = 'Open', bg = 'gray45', fg = 'green3', borderwidth = 0, command = lambda: _os_._screenset_('files'))
            notepadtextopen.place(x = (notepadx + 500), y = (notepady + 2))
            #Create nine entry lines for notepad
            notepadline1 = Entry(OS, width = 90, bg = 'gray77')
            notepadline2 = Entry(OS, width = 90, bg = 'gray77')
            notepadline3 = Entry(OS, width = 90, bg = 'gray77')
            notepadline4 = Entry(OS, width = 90, bg = 'gray77')
            notepadline5 = Entry(OS, width = 90, bg = 'gray77')
            notepadline6 = Entry(OS, width = 90, bg = 'gray77')
            notepadline7 = Entry(OS, width = 90, bg = 'gray77')
            notepadline8 = Entry(OS, width = 90, bg = 'gray77')
            notepadline9 = Entry(OS, width = 90, bg = 'gray77')
            notepadline1.place(x = (notepadx + 30), y = (notepady + 50))
            notepadline2.place(x = (notepadx + 30), y = (notepady + 70))
            notepadline3.place(x = (notepadx + 30), y = (notepady + 90))
            notepadline4.place(x = (notepadx + 30), y = (notepady + 110))
            notepadline5.place(x = (notepadx + 30), y = (notepady + 130))
            notepadline6.place(x = (notepadx + 30), y = (notepady + 150))
            notepadline7.place(x = (notepadx + 30), y = (notepady + 170))
            notepadline8.place(x = (notepadx + 30), y = (notepady + 190))
            notepadline9.place(x = (notepadx + 30), y = (notepady + 210))
            filename_ = Entry(OS, width = 10, bg = 'gray80')
            filename_.place(x = (notepadx + 400), y = (notepady + 2))
            _os_._createmisclabel_(OS, ('Save as:'), 'gray45', 'black', (notepadx + 350), (notepady + 2))
        if screen == 'calculator':
            _os_._cover_('gray72')
            _os_._calculator_._mainloop_()
        if screen == 'files':
            _os_._cover_('tan3')
            _os_._createmisclabel_(OS, ('Files'), 'tan3', 'black', 10, 10)
            file_slot = Button(OS, text = ((str(filesall[0])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(1), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 40)
            file_slot = Button(OS, text = ((str(filesall[1])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(2), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 70)
            file_slot = Button(OS, text = ((str(filesall[2])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(3), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 100)
            file_slot = Button(OS, text = ((str(filesall[3])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(4), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 130)
            file_slot = Button(OS, text = ((str(filesall[4])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(5), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 160)
            file_slot = Button(OS, text = ((str(filesall[5])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(6), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 190)
            file_slot = Button(OS, text = ((str(filesall[6])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(7), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 220)
            file_slot = Button(OS, text = ((str(filesall[7])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(8), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 250)
            file_slot = Button(OS, text = ((str(filesall[8])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(9), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 280)
            file_slot = Button(OS, text = ((str(filesall[9])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(10), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 310)
            file_slot = Button(OS, text = ((str(filesall[10])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(11), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 340)
            file_slot = Button(OS, text = ((str(filesall[11])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(12), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 370)
            file_slot = Button(OS, text = ((str(filesall[12])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(13), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 400)
            file_slot = Button(OS, text = ((str(filesall[13])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(14), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 430)
            file_slot = Button(OS, text = ((str(filesall[14])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(15), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 460)
            file_slot = Button(OS, text = ((str(filesall[15])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(16), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 490)
            file_slot = Button(OS, text = ((str(filesall[16])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(17), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 520)
            file_slot = Button(OS, text = ((str(filesall[17])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(18), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 550)
            file_slot = Button(OS, text = ((str(filesall[18])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(19), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 580)
            file_slot = Button(OS, text = ((str(filesall[19])).split('|')[0]), bg = 'tan1', fg  = 'black', command = lambda: _os_._files_._openfile_(20), borderwidth = 1, activebackground = 'tan1', activeforeground = 'black', width = 100)
            file_slot.place(x = 20, y = 610)
            xb__ = Button(OS, text = 'X', bg = 'tan3', fg = 'black', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'tan3', activeforeground = 'black')
            xb__.place(x = 1565, y = 0)
        if screen == 'calculator':
            _os_._calculator_._mainloop_()
    def delete_last(string):
        old = str(string)
        new = ''
        old_c = 0
        for _ in old: old_c += 1
        old_c -= 1
        for _ in range(old_c): new = str(new) + old[_]
        return new
    def BSOD(ERROR):
        global bsodtext
        BSOD_= Canvas(OS, width = 1580, height = 800, bg = 'blue2', highlightthickness = 0)
        BSOD_.place(x = 0, y = 0)
        BSODERR1 = Label(OS, text = bsodtext, bg = 'blue2', fg = 'white', font = 'Courier')
        BSODERR1.place(x = 10, y = 10)
        BSODERR2 = Label(OS, text = ERROR, bg = 'blue2', fg = 'white', font = 'Courier')
        BSODERR2.place(x = 10, y = 110)
    class _calculator_():
        def _mainloop_():
            global line1, line2, line3, line4, line5
            _os_._calculator_._cscreen_()
            _os_._calculator_._cbuttons_()
        def _cscreen_():
            global line1, line2, line3, line4, line5, calculatorstatusinfo
            bg1_ = Canvas(OS, width = 1540, height = 720, bg = 'gray13', highlightthickness = 0)
            bg1_.place(x = 20, y = 20)
            outputscreen_ = Canvas(OS, width = 300, height = 200, bg = 'black', highlightthickness = 0)
            outputscreen_.place(x = 22, y = 22)
            _os_._createmisclabel_(OS, (line1), 'black', 'white', 30, 30)
            _os_._createmisclabel_(OS, (line2), 'black', 'white', 30, 50)
            _os_._createmisclabel_(OS, (line3), 'black', 'white', 30, 70)
            _os_._createmisclabel_(OS, (line4), 'black', 'white', 30, 90)
            _os_._createmisclabel_(OS, (line5), 'black', 'white', 30, 110)
            xb__ = Button(OS, text = 'X', bg = 'gray13', fg = 'white', command = lambda: _os_._screenset_('desktop'), borderwidth = 0, activebackground = 'gray13', activeforeground = 'white')
            xb__.place(x = 1545, y = 20)
            #                       Line1 Line1  Error Operation
            if calculatorstatusinfo[0] == True and calculatorstatusinfo[1] == False: _os_._createmisclabel_(OS, ('<------'), 'black', 'white', 265, 30)
            else: _os_._createmisclabel_(OS, ('<------'), 'black', 'white', 265, 50)
        def _cbuttons_():
            global line1, line2, line3, line4, line5
            _1 = Button(OS, text = '1', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _1.place(x = 30, y = 240)
            _2 = Button(OS, text = '2', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _2.place(x = 60, y = 240)
            _3 = Button(OS, text = '3', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _3.place(x = 90, y = 240)
            _4 = Button(OS, text = '4', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _4.place(x = 30, y = 270)
            _5 = Button(OS, text = '5', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _5.place(x = 60, y = 270)
            _6 = Button(OS, text = '6', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _6.place(x = 90, y = 270)
            _7 = Button(OS, text = '7', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _7.place(x = 30, y = 300)
            _8 = Button(OS, text = '8', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _8.place(x = 60, y = 300)
            _9 = Button(OS, text = '9', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _9.place(x = 90, y = 300)
            _0 = Button(OS, text = '0', width = 2, bg = 'gray13', command = lambda: None, fg = 'white')
            _0.place(x = 60, y = 330)
            et_ = Button(OS, text = 'Enter', width = 6, bg = 'gray13', fg = 'white', command = lambda: _os_._calculator_._entrytoggle_())
            et_.place(x = 150, y = 240)
        def _entrytoggle_():
            global calculatorstatusinfo
            if calculatorstatusinfo[0] == True and calculatorstatusinfo[1] == False:
                calculatorstatusinfo[0] = False
                calculatorstatusinfo[1] = True
            else:
                calculatorstatusinfo[0] = True
                calculatorstatusinfo[1] = False
            _os_._main_()
    class _files_():
        def _openfile_(number):
            global filesall
            try:
                filetype = str((str(filesall[(number - 1)]).split(',')[0]).split('.')[1]).split("'")[0]
                if filetype == 'txt':
                    _os_._cover_('tan3')
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[3]), 'tan3', 'black', 10, 10)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[5]), 'tan3', 'black', 10, 30)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[7]), 'tan3', 'black', 10, 50)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[9]), 'tan3', 'black', 10, 70)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[11]), 'tan3', 'black', 10, 90)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[13]), 'tan3', 'black', 10, 110)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[15]), 'tan3', 'black', 10, 130)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[17]), 'tan3', 'black', 10, 150)
                    _os_._createmisclabel_(OS, (str(filesall[(number - 1)]).split("'")[19]), 'tan3', 'black', 10, 170)
                elif filetype == 'mp3':
                    mp3w1 = Tk()
                    mp3w1.title('MP3 file')
                elif filetype == 'exe':
                    exec(str(((filesall[0])[1]).split('|')[1]))
            except IndexError: None
        def _savefile_(name, filetype, context):
            global filesall, currentsystemtime
            if (filesall[0] == ''): filesall[0] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[1] == ''): filesall[1] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[2] == ''): filesall[2] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[3] == ''): filesall[3] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[4] == ''): filesall[4] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[5] == ''): filesall[5] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[6] == ''): filesall[6] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[7] == ''): filesall[7] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[8] == ''): filesall[8] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[9] == ''): filesall[9] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[10] == ''): filesall[10] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[11] == ''): filesall[11] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[12] == ''): filesall[12] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[13] == ''): filesall[13] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[14] == ''): filesall[14] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[15] == ''): filesall[15] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[16] == ''): filesall[16] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[17] == ''): filesall[17] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[18] == ''): filesall[18] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[19] == ''): filesall[19] = [str(str(name)+ str(filetype)), '|' + str(context)]
            elif (filesall[20] == ''): filesall[20] = [str(str(name)+ str(filetype)), '|' + str(context)]
    def _switchtime_():
        global hourmode
        if hourmode == '12HR': hourmode = '24HR'
        else: hourmode = '12HR'
        _os_._main_()
        _os_._main_()
    def _gathertimeinfo_():
        global currentsystemtime, hourmode
        try:
            struct = str(localtime())
            year = struct.split('=')[1]
            year = year.split(',')[0]
            month = struct.split('=')[2]
            month = month.split(',')[0]
            day = struct.split('=')[3]
            day = day.split(',')[0]
            hour = struct.split('=')[4]
            hour = hour.split(',')[0]
            minute = struct.split('=')[5]
            minute = minute.split(',')[0]
            if minute == '1' or minute == '2' or minute == '3' or minute == '4' or minute == '5' or minute == '6' or minute == '7' or minute == '8' or minute == '9' or minute == '0': minute = '0' + str(minute)
            if hourmode == '24HR': None
            elif hourmode == '12HR':
                if int(hour) > 12: hour = int(hour) - 12
            currentsystemtime = (str(hour) + ':' + str(minute) + '     ' + str(month) + '/' + str(day) + '/' + str(year))
        except NameError: '_os_.BSOD("<ERR:exception_passed[INVALID-RESPONSE]09287409#5%%1>**APPact = Time**EXEPTIONtype = NameError")'
    def _screenset_(arg):
        global screen
        screen = (str(arg).lower())
        _os_._main_()
    def _startbar_():
        global startbarvisible
        if startbarvisible == False: startbarvisible = True
        else: startbarvisible = False
        if startbarvisible == True:
            startbar = Canvas(OS, width = 200, height = 300, bg = 'black', highlightthickness = 0)
            startbar.place(x = 0, y = 462)
            startbar_searchreq = Button(OS, text = 'Search', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._applicationsearch_((str(startbar_searchentry.get()))))
            startbar_searchreq.place(x = 140, y = 720)
            startbar_searchentry = Entry(OS, width = 20, bg = 'gray77')
            startbar_searchentry.place(x = 5, y = 721.5)
            startbar_buttonsetscreendesktop = Button(OS, text = 'Go to desktop', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('desktop'))
            startbar_buttonsetscreendesktop.place(x = 5, y = 470)
            startbar_buttonrestartsystem = Button(OS, text = 'Restart', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: None)
            startbar_buttonrestartsystem.place(x = 5, y = 500)
            startbar_buttonpoweroffOS = Button(OS, text = 'Power off', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: quit())
            startbar_buttonpoweroffOS.place(x = 5, y = 530)
            startbar_buttonlogout = Button(OS, text = 'Switch user', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('login'))
            startbar_buttonlogout.place(x = 5, y = 560)
        else: _os_._main_()
    def _cmdcommand_(command):
        global screen, hourmode
        try:
            command = str(command.lower())
            _os_._main_()
            if command.split(' ')[0] == 'py.exe' and command.split(' ')[1] == '-e': _os_._execute_((command.split('/')[1]))
            elif command.split(' ')[0] == 'py.exe' and command.split(' ')[1] == '-w': print((command.split('/')[1]))
            elif command == 'help': _os_._createmisclabel_(OS, (cmdcommands), 'gray9', 'green3', 20, 20)
            elif command == 'exit': _os_._screenset_('desktop')
            elif command == 'abort': quit()
            elif command == 'sys_runs': _os_._createmisclabel_(OS, (runs), 'gray9', 'green3', 20, 20)
            elif command == 'bsod': _os_.BSOD('<ERR:exception_passed[INVALID-RESPONSE]09287409#5%%1>**APPact = CMD**EXEPTIONtype = SelfTerminationTrigger[UserInitiated]')
            elif command == 'zimbawe': os.abort()
            elif command == 'netstat':
                _os_._createmisclabel_(OS, (os.getlogin()), 'gray9', 'green3', 20, 20)
                _os_._createmisclabel_(OS, (os.getpid()), 'gray9', 'green3', 20, 40)
                _os_._createmisclabel_(OS, (os.getppid()), 'gray9', 'green3', 20, 60)
                _os_._createmisclabel_(OS, (os.cpu_count()), 'gray9', 'green3', 20, 80)
            elif (command.split(' ')[0] == 'beep'): winsound.Beep(int(command.split(' ')[1]), int(command.split(' ')[2]))
            elif (command.split(' ')[0] == 'local'):
                if (command.split(' ')[1] == '-o'): _os_._applicationsearch_(str(command.split('/')[1]))
                elif (command.split(' ')[1] == '-a'): None
                elif (command.split(' ')[1] == 'ram_dump'):
                    _os_._createmisclabel_(OS, (ram01), 'gray9', 'green3', 20, 20)
                    _os_._createmisclabel_(OS, (ram02), 'gray9', 'green3', 20, 40)
                    _os_._createmisclabel_(OS, (ram03), 'gray9', 'green3', 20, 60)
                    _os_._createmisclabel_(OS, (ram04), 'gray9', 'green3', 20, 80)
                    _os_._createmisclabel_(OS, (ram05), 'gray9', 'green3', 20, 100)
                    _os_._createmisclabel_(OS, (ram06), 'gray9', 'green3', 20, 120)
                    _os_._createmisclabel_(OS, (ram07), 'gray9', 'green3', 20, 140)
                    _os_._createmisclabel_(OS, (ram08), 'gray9', 'green3', 20, 160)
                    _os_._createmisclabel_(OS, (ram09), 'gray9', 'green3', 20, 180)
                    _os_._createmisclabel_(OS, (ram10), 'gray9', 'green3', 20, 200)
                    _os_._createmisclabel_(OS, (ram11), 'gray9', 'green3', 20, 220)
                    _os_._createmisclabel_(OS, (ram12), 'gray9', 'green3', 20, 240)
                    _os_._createmisclabel_(OS, (ram13), 'gray9', 'green3', 20, 260)
                    _os_._createmisclabel_(OS, (ram14), 'gray9', 'green3', 20, 280)
                    _os_._createmisclabel_(OS, (ram15), 'gray9', 'green3', 20, 300)
                    _os_._createmisclabel_(OS, (ram16), 'gray9', 'green3', 20, 320)
                    _os_._createmisclabel_(OS, (ram17), 'gray9', 'green3', 20, 340)
                    _os_._createmisclabel_(OS, (ram18), 'gray9', 'green3', 20, 360)
                    _os_._createmisclabel_(OS, (ram19), 'gray9', 'green3', 20, 380)
                    _os_._createmisclabel_(OS, (ram20), 'gray9', 'green3', 20, 400)
                    _os_._createmisclabel_(OS, ('Local ram dump rows 01 - 20 complete'), 'gray9', 'green3', 20, 420)
            else:
                _os_._createmisclabel_(OS, ('<stdin> ERROR:'), 'gray9', 'green3', 20, 20)
                _os_._createmisclabel_(OS, ('COMMAND NAME (' + command + ') IS NOT A VALID SYSTEM COMMAND'), 'gray9', 'green3', 30, 40)
                _os_._createmisclabel_(OS, ('TYPE "HELP" FOR A LIST OF COMMANDS'), 'gray9', 'green3', 30, 60)
        except IndexError: None
        except TypeError: None
    def _applicationsearch_(search):
        global screen, applications
        match = screen
        totalapplicationnumber = (1 + (applications.count(' ')))
        search = str(search.lower())
        try:
            for i in range(totalapplicationnumber):
                if (applications.split(' ')[(i - 1)]) == search: _os_._screenset_(search)
        except IndexError: None
    def _execute_(command):
        command = str(command)
        try: exec(command)
        except SyntaxError: return ('SyntaxError')
        except NameError: return ('NameError')
    def _createmisclabel_(parent_, text_, background_, foreground_, x_, y_):
        _miscitem83267945832_ = Label(parent_, text = text_, bg = background_, fg = foreground_)
        _miscitem83267945832_.place(x = x_, y = y_)
    def _cover_(color):
        cover = Canvas(OS, width = 1580, height = 760, bg = color, highlightthickness = 0)
        cover.place(x = 0, y = 0)
    def _taskbar_():
        global bottomrightcornernotificationcount, currentsystemtime
        taskbar = Canvas(OS, width = 1580, height = 45, bg = 'black', highlightthickness = 0)
        taskbar.place(x = 0, y = 755)
        taskbarbutton1 = Button(OS, width = 3, text = 'H', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._startbar_())
        taskbarbutton1.place(x = 10, y = 766)
        taskbarbutton2 = Button(OS, width = 20, text = 'Settings', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('settings'))
        taskbarbutton2.place(x = 50, y = 766)
        taskbarbutton3 = Button(OS, width = 20, text = 'Email', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('email'))
        taskbarbutton3.place(x = 200, y = 766)
        taskbarbutton4 = Button(OS, width = 20, text = 'Notepad', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('notepad'))
        taskbarbutton4.place(x = 350, y = 766)
        taskbarbutton5 = Button(OS, width = 20, text = 'Files', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('files'))
        taskbarbutton5.place(x = 500, y = 766)
        taskbarbutton6 = Button(OS, width = 20, text = 'Calculator', bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('calculator'))
        taskbarbutton6.place(x = 650, y = 766)
        taskbarbutton_notifs = Button(OS, text = bottomrightcornernotificationcount, bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('email'))
        taskbarbutton_notifs.place(x = 1550, y = 766)
        taskbarbutton_notifs = Button(OS, text = currentsystemtime, bg = 'black', fg = 'white', borderwidth = 0, activebackground = 'black', activeforeground = 'white', command = lambda: _os_._screenset_('settings/time'))
        taskbarbutton_notifs.place(x = 1400, y = 766)
    class _email_():
        def _emailcountupdate_():
            global emailcontext01, emailcontext02, emailcontext03, emailcontext04, emailcontext05, emailcontext06, emailcontext07, emailcontext08, emailcontext09, emailcontext10
            global emailcontext11, emailcontext12, emailcontext13, emailcontext14, emailcontext15, emailcontext16, emailcontext17, emailcontext18, emailcontext19, bottomrightcornernotificationcount
            bottomrightcornernotificationcount = 19
            if (emailcontext01 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext02 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext03 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext04 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext05 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext06 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext07 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext08 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext09 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext10 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext11 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext12 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext13 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext14 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext15 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext16 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext17 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext18 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
            if (emailcontext19 == ['SENDER', 'HEADING', 'MESSAGE']): bottomrightcornernotificationcount -= 1
        def _viewemail_(emailnumber):
            global emailcontext01, emailcontext02, emailcontext03, emailcontext04, emailcontext05, emailcontext06, emailcontext07, emailcontext08, emailcontext09, emailcontext10
            global emailcontext11, emailcontext12, emailcontext13, emailcontext14, emailcontext15, emailcontext16, emailcontext17, emailcontext18, emailcontext19
            if (emailnumber >= 1 and emailnumber <= 19):
                email_view_cover = Canvas(OS, width = 600, height = 500, highlightthickness = 0, bg = 'cyan4')
                email_view_cover.place(x = 850, y = 200)
                _os_._createmisclabel_(OS, ('Email'), 'cyan4', 'black', 852, 202)
                if emailnumber == 1:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext01[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext01[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext01[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 2:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext02[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext02[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext02[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 3:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext03[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext03[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext03[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 4:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext04[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext04[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext04[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 5:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext05[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext05[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext05[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 6:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext06[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext06[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext06[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 7:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext07[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext07[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext07[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 8:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext08[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext08[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext08[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 9:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext09[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext09[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext09[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 10:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext10[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext10[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext10[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 11:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext11[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext11[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext11[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 12:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext12[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext12[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext12[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 13:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext13[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext13[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext13[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 14:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext14[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext14[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext14[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 15:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext15[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext15[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext15[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 16:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext16[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext16[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext16[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 17:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext17[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext17[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext17[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 18:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext18[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext18[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext18[2]), 'cyan4', 'black', 950, 300)
                if emailnumber == 19:
                    _os_._createmisclabel_(OS, ('Sender: ', emailcontext19[0]), 'cyan4', 'black', 860, 220)
                    _os_._createmisclabel_(OS, ('Heading: ', emailcontext19[1]), 'cyan4', 'black', 860, 240)
                    _os_._createmisclabel_(OS, (emailcontext19[2]), 'cyan4', 'black', 950, 300)
                _ = Button(OS, borderwidth = 0, activeforeground = 'black', fg = 'black', bg = 'cyan4', activebackground = 'cyan4', command = lambda: _os_._main_(), text = 'Close')
                _.place(x = 1400, y = 200)
        def _sendemail_(sender, heading, message):
            global emailcontext01, emailcontext02, emailcontext03, emailcontext04, emailcontext05, emailcontext06, emailcontext07, emailcontext08, emailcontext09, emailcontext10
            global emailcontext11, emailcontext12, emailcontext13, emailcontext14, emailcontext15, emailcontext16, emailcontext17, emailcontext18, emailcontext19
            if emailcontext01 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext01 = [sender, heading, message]
            elif emailcontext02 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext02 = [sender, heading, message]
            elif emailcontext03 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext03 = [sender, heading, message]
            elif emailcontext04 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext04 = [sender, heading, message]
            elif emailcontext05 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext05 = [sender, heading, message]
            elif emailcontext06 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext06 = [sender, heading, message]
            elif emailcontext07 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext07 = [sender, heading, message]
            elif emailcontext08 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext08 = [sender, heading, message]
            elif emailcontext09 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext09 = [sender, heading, message]
            elif emailcontext10 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext10 = [sender, heading, message]
            elif emailcontext11 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext11 = [sender, heading, message]
            elif emailcontext12 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext12 = [sender, heading, message]
            elif emailcontext13 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext13 = [sender, heading, message]
            elif emailcontext14 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext14 = [sender, heading, message]
            elif emailcontext15 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext15 = [sender, heading, message]
            elif emailcontext16 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext16 = [sender, heading, message]
            elif emailcontext17 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext17 = [sender, heading, message]
            elif emailcontext18 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext18 = [sender, heading, message]
            elif emailcontext19 == ['SENDER', 'HEADING', 'MESSAGE']: emailcontext19 = [sender, heading, message]
#SETUP#
_os_._email_._sendemail_('HarrisonOS.co', 'Introduction to HarrisonOS v1.6.0', welcomeemail)
_os_._email_._emailcountupdate_()
_os_._files_._savefile_('BSOD-COMMAND', '.exe', '_os_.BSOD("<ERR:exception_passed[INVALID-RESPONSE]09287409#5%%1>**APPact = Files**EXEPTIONtype = SelfTermination")')
_os_._gathertimeinfo_()
_os_._main_()
_os_._switchtime_()
_os_._switchtime_()
_os_._main_()
_os_._switchtime_()
_os_._switchtime_()
_os_._main_()
OS.mainloop()
#SETUP#
#</OS>
#</PYv3.5.0>
