#ADD ACCEPTIONS TO COUNT ERRORS ONCE DONE WITH OS CODE

from time import localtime
from tkinter import *
import tkinter
import random
import math
import time
import sys
import os

screen = None
SBV = False
applications = ['desktop', 'settings', 'files', 'cmd']
runs = 0
start = time.time()
USER = None
RAM = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
FILES = [['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'],
         ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'],
         ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'],
         ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS'], ['FILENAME', 'FILETYPE', 'CONTENTS']]
EMAILS = [['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'],
          ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'],
          ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'],
          ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING'], ['MESSAGE, SENDER, HEADING']]
ERRORS = [['SYNTAXERROR', 0], ['VALUEERROR', 0], ['INDEXERROR', 0], ['NAMEERROR', 0], ['TYPEERROR', 0], ['IMPORTERROR', 0], ['OSERROR', 0], ['ATTRIBUTEERROR', 0]]
commands = '''
RES == PRINTS THE SCREEN RESOLUTION FOR THE OS WINDOW
ERRORS == PRINTS THE ACCOUNTED/HANDLED ERRORS FOR THE SYSTEM OS
TREE == GIVES A GRAPHICAL DESCIPTION OF SCRIPT DIRECTORIES
PY.EXE -E /PYTHON COMMAND/ == EXECUTES THE DESIGNATED PYTHON COMMAND USING THE SYSLOG
FO /FILENO/ == PRINTS THE DESIGNATED FILE CONTENTS
SCREENSET /SCREEN/ == SETS THE CURRENT SCREEN TO THE INPUT SCREEN
PY.EXE -M /TEXT/ == WRITES TEXT TO THE SYSLOG
PY.EXE -Q == QUITS THE OS/SCRIPT
CONSOLE.LOG /TEXT/ == PRINTS THE TEXT TO THE COMMAND SHELL UI
CONSOLE.UTM == PRINTS THE UPTIME INFORMATION
CONSOLE.MOD == PRINTS THE INCLUDED MODULES
CONSOLE.RAM == PRINTS THE RAM STORAGE CHART/GRID
EXIT == EXITS THE COMMAND SHELL
'''

__ = Tk()
__.title('Harrison OS v1.7.0')
__.minsize(width = 1580, height = 800)
__.maxsize(width = 1580, height = 800)

class _():
    class __files__():
        def __init__(filename, filetype, filecontents):
            global FILES
            filename = str(filename)
            filetype = str(filetype)
            filecontents = str(filecontents)
            DN = False
            for ____ in range(19):
                if FILES[____] == ['FILENAME', 'FILETYPE', 'CONTENTS'] and DN == False:
                    FILES[____] = [filename, filetype, filecontents]
                    DN = True
        def __open__(fileno):
            global FILES
            filename = (FILES[(fileno - 1)])[0]
            filetype = (FILES[(fileno - 1)])[1]
            filecontents = (FILES[(fileno - 1)])[2]
            if filetype == '.exe': exec(str(filecontents))
    class __email__():
        None
    class __startbar__():
        def __toggle__():
            global SBV
            if SBV == False: SBV = True
            else: SBV = False
            _.__os__.__main__()
        def __draw__():
            global SBV
            if SBV == True:
                Canvas(__, width = 200, height = 300, bg = 'gray12', highlightthickness = 0).place(x = 0, y = 460)
                Button(__, bg = 'gray12', borderwidth = 0, text = 'Desktop', command = lambda: _.__screen__handling__.__screen__set__('desktop'), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 2, y = 462)
                Button(__, bg = 'gray12', borderwidth = 0, text = 'Settings', command = lambda: _.__screen__handling__.__screen__set__('settings'), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 2, y = 492)
                Button(__, bg = 'gray12', borderwidth = 0, text = 'Logout', command = lambda: _.__screen__handling__.__screen__set__('login'), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 2, y = 522)
                Button(__, bg = 'gray12', borderwidth = 0, text = 'Power off', command = lambda: quit(), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 2, y = 552)
    class __taskbar__():
        def __taskbarbg__():
            Canvas(__, bg = 'gray12', width = 1580, height = 45, highlightthickness = 0).place(x = 0, y = 755)
        def __taskbar__widgets__applications__():
            Button(__, bg = 'gray12', borderwidth = 0, text = 'OS', width = 4, command = lambda: _.__startbar__.__toggle__(), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 10, y = 762.5)
            Button(__, bg = 'gray12', borderwidth = 0, text = 'Settings', width = 20, command = lambda: _.__screen__handling__.__screen__set__('settings'), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 50, y = 762.5)
            Button(__, bg = 'gray12', borderwidth = 0, text = 'Files', width = 20, command = lambda: _.__screen__handling__.__screen__set__('files'), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 200, y = 762.5)
            Button(__, bg = 'gray12', borderwidth = 0, text = 'CMD', width = 20, command = lambda: _.__screen__handling__.__screen__set__('cmd'), fg = 'white', activebackground = 'gray12', activeforeground = 'white').place(x = 350, y = 762.5)
    class __screen__handling__():
        def __get__screen__():
            global screen
            return screen
        def __screen__set__(name):
            global screen, SBV
            SBV = False
            screen = str(name)
            _.__os__.__main__()
        def __if__screen__is__():
            global screen, FILES
            if screen == 'desktop':
                _.__widget__handling__.__cover__top__('gray50')
            elif screen == 'settings':
                _.__widget__handling__.__cover__top__('gray2')
            elif screen == 'files':
                _.__widget__handling__.__cover__top__('white')
                a = 10
                b = 0
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(1), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(2), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(3), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(4), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(5), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(6), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(7), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(8), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(9), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(10), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(11), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(12), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(13), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(14), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(15), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(16), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(17), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(18), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(19), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
                a += 30
                b += 1
                Button(__, bg = 'tan', borderwidth = 0, text = (str((FILES[b])[0]) + str((FILES[b])[1])), command = lambda: _.__files__.__open__(20), fg = 'black', activebackground = 'tan', activeforeground = 'black', width = 200).place(x = 10, y = a)
            elif screen == 'cmd':
                _.__widget__handling__.__cover__top__('black')
                _.__cmd__.__graphics__()
            elif screen == 'login':
                Canvas(__, width = 1580, height = 800, bg = 'gray62', highlightthickness = 0).place(x = 0, y = 0)
                e = Entry(__, width = 30, bg = 'white', fg = 'black')
                e.place(x = 750, y = 400)
                _.__widget__handling__.__misc__label__(('Username:'), 'gray62', 'black', 810, 375, '_')
                Button(__, bg = 'gray62', borderwidth = 0, text = 'Login', command = lambda: _.__login__.__login__(e.get()), fg = 'black', activebackground = 'gray62', activeforeground = 'black').place(x = 825, y = 425)
    class __login__():
        def __login__(user):
            global USER
            USER = str(user)
            _.__screen__handling__.__screen__set__('desktop')
            _.__taskbar__.__taskbarbg__()
            _.__taskbar__.__taskbar__widgets__applications__()
    class __cmd__():
        def __graphics__():
            a = Entry(__, width = 70, bg = 'black', fg = 'green', font = 'Courier 10')
            a.place(x = 33, y = 710)
            Button(__, bg = 'black', borderwidth = 0, text = '>>>', command = lambda: _.__cmd__.__interperet__command__(a.get()), fg = 'green', activebackground = 'black', activeforeground = 'green').place(x = 2, y = 708.5)
        def __interperet__command__(command):
            _.__cmd__.__clear__slate__()
            global ERRORS, runs, start
            command = (str(command)).lower()
            if command == 'exit': _.__screen__handling__.__screen__set__('desktop')
            elif command == 'help': _.__widget__handling__.__misc__label__((commands), 'black', 'green', 10, 10, 'Courier 9')
            elif command == 'res':
                _.__widget__handling__.__misc__label__(('W = 1580 PX'), 'black', 'green', 10, 10, 'Courier 10')
                _.__widget__handling__.__misc__label__(('W = 0800 PX'), 'black', 'green', 10, 30, 'Courier 10')
            elif (command.split(' ')[0]) == 'fo':
                _.__widget__handling__.__misc__label__(((_.__files__.__open__(int(command.split('/')[1])))[0]), 'black', 'green', 10, 10, 'Courier 10')
                _.__widget__handling__.__misc__label__(((_.__files__.__open__(int(command.split('/')[1])))[1]), 'black', 'green', 10, 30, 'Courier 10')
                _.__widget__handling__.__misc__label__(((_.__files__.__open__(int(command.split('/')[1])))[2]), 'black', 'green', 10, 50, 'Courier 10')
            elif command == 'tree':
                _.__widget__handling__.__misc__label__((_), 'black', 'green', 10, 10, 'Courier 9')
                #Give a tree of all the classes and commands under class<_> once done with os script.
            elif (command.split(' ')[0]) == 'screenset': _.__screen__handling__.__screen__set__(str(command.split('/')[1]))
            elif command == 'errors':
                _.__widget__handling__.__misc__label__((ERRORS[0]), 'black', 'green', 10, 10, 'Courier 10')
                _.__widget__handling__.__misc__label__((ERRORS[1]), 'black', 'green', 10, 30, 'Courier 10')
                _.__widget__handling__.__misc__label__((ERRORS[2]), 'black', 'green', 10, 50, 'Courier 10')
                _.__widget__handling__.__misc__label__((ERRORS[3]), 'black', 'green', 10, 70, 'Courier 10')
                _.__widget__handling__.__misc__label__((ERRORS[4]), 'black', 'green', 10, 90, 'Courier 10')
                _.__widget__handling__.__misc__label__((ERRORS[5]), 'black', 'green', 10, 110, 'Courier 10')
                _.__widget__handling__.__misc__label__((ERRORS[6]), 'black', 'green', 10, 130, 'Courier 10')
                _.__widget__handling__.__misc__label__((ERRORS[7]), 'black', 'green', 10, 150, 'Courier 10')
            elif (command.split(' ')[0]) == 'py.exe':
                if (command.split(' ')[1]) == '-e': exec(str(command.split('/')[1]))
                elif (command.split(' ')[1]) == '-w': print(command.split('/')[1])
                elif (command.split(' ')[1]) == '-q': quit() or exit() or os.abort()
            elif (command.split('.')[0]) == 'console':
                if (command.split('.')[1]) == 'log': _.__widget__handling__.__misc__label__((command.split('/')[1]), 'black', 'green', 10, 10, 'Courier 10')
                elif (command.split('.')[1]) == 'utm':
                    _.__widget__handling__.__misc__label__(('RUN COUNT: ' + str(runs)), 'black', 'green', 10, 10, 'Courier 10')
                    _.__widget__handling__.__misc__label__(('UPTIME [SECONDS]: ' + str(float(time.time()) - float(start))), 'black', 'green', 10, 30, 'Courier 10')
                elif (command.split('.')[1]) == 'mod':
                    _.__widget__handling__.__misc__label__((localtime), 'black', 'green', 10, 10, 'Courier 10')
                    _.__widget__handling__.__misc__label__((tkinter), 'black', 'green', 10, 30, 'Courier 10')
                    _.__widget__handling__.__misc__label__((random), 'black', 'green', 10, 50, 'Courier 10')
                    _.__widget__handling__.__misc__label__((math), 'black', 'green', 10, 70, 'Courier 10')
                    _.__widget__handling__.__misc__label__((sys), 'black', 'green', 10, 90, 'Courier 10')
                    _.__widget__handling__.__misc__label__((os), 'black', 'green', 10, 110, 'Courier 10')
                    _.__widget__handling__.__misc__label__((time), 'black', 'green', 10, 130, 'Courier 10')
                elif (command.split('.')[1]) == 'ram': _.__widget__handling__.__misc__label__(('RAM is not yet accessible. <ERNO #1>'), 'black', 'green', 10, 10, 'Courier 10')
        def __clear__slate__():
            Canvas(__, bg = 'black', highlightthickness = 0, width = 1580, height = 680).place(x = 0, y = 0)
    class __widget__handling__():
        def __cover__top__(bgcolor):
            Canvas(__, width = 1580, height = 755, bg = bgcolor, highlightthickness = 0).place(x = 0, y = 0)
        def __misc__label__(labeltext, bgcolor, fgcolor, xcor, ycor, font_):
            if font_ == '_': font_ = 'Courier_new_baltic 10'
            Label(__, text = labeltext, bg = bgcolor, fg = fgcolor, font = font_).place(x = xcor, y = ycor)
    class __os__():
        def __main__():
            global runs
            runs += 1
            _.__screen__handling__.__if__screen__is__()
            _.__startbar__.__draw__()
    class __time__():
        def __localtime__():
            OLD = str(localtime())
            YEAR = str((OLD.split(',')[0]).split('=')[1])
            MONTH = str((OLD.split(',')[1]).split('=')[1])
            DAY = str((OLD.split(',')[2]).split('=')[1])
            HOUR = str((OLD.split(',')[3]).split('=')[1])
            MINUTE = str((OLD.split(',')[4]).split('=')[1])
            SECOND = str((OLD.split(',')[5]).split('=')[1])
            NEW = [(MONTH + '/' + DAY + '/' + YEAR + '-' + HOUR + ':'+ MINUTE), SECOND]
            return NEW

_.__taskbar__.__taskbarbg__()
_.__taskbar__.__taskbar__widgets__applications__()
_.__screen__handling__.__screen__set__('desktop')
_.__time__.__localtime__()
_.__os__.__main__()

_.__files__.__init__('Test', '.exe', 'print("Hello")')              #For testing file function

__.mainloop()
