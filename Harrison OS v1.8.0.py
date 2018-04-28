#########################################################################
#                                                                       #
#   THIS BELONGS TO HARRISON LINDGREN [harrison.lindgren@gmail.com]     #
#   COPYING IS AGAINST THE TERMS OF CONDITIONS OF THIS SCRIPT           #
#   THIS SCRIPT WAS CREATED 04/20/2018 [MM/DD/YYYY]                     #
#   ENVIRONMENTAL LANGUAGE IS PYTHON / CAN RUN ON PYTHON ENV            #
#   SCRIPT NATIVE TO IDLE PYTHON V 3.5.0                                #
#   COPYLEFT OF HARRISON LINDGREN [harrison.lindgren@gmail.com]         #
#                                                                       #
#########################################################################

#Add a calculator application

import tkinter, random, sys, os, math, time, winsound
from tkinter import *
from time import localtime

sys.setrecursionlimit(1000)

OS = Tk()
OS.title('Harrison OS v1.8.0')
OS.geometry('1580x800')
OS.minsize(width = 1580, height = 800)

SCREENS = ['login', 'desktop', 'cmd', 'files', 'python', 'settings', 'dvc', 'notepad', 'calculator']
USERNAME = 'null'
SCREEN = SCREENS[0]
FILES = ''
STARTBARVIS = False
RUNS = 0
LASTRUNTIME = 0
ERRORS = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#syntaxerror, overflowerror, valueerror, indexerror, oserror, permissionerror, nameerror, importerror, typeerror
CALC_VARS = [0, 0, 0, '+', None]
#line1, line2, answer, operation, error

for _ in range(25): FILES = str(FILES) + '/type|name|contents|'
FILES = FILES.split('/')

def restart_os(mode):
    global SCREENS, USERNAME, SCREEN, FILES, STARTBARVIS, LASTRUNTIME, CALC_VARS, RUNS, ERRORS
    SCREENS = ['login', 'desktop', 'cmd', 'files', 'python', 'settings', 'dvc', 'notepad', 'calculator']
    USERNAME = 'null'
    SCREEN = SCREENS[0]
    FILES = ''
    STARTBARVIS = False
    LASTRUNTIME = 0
    CALC_VARS = [0, 0, 0, '+', None]
    for _ in range(25): FILES = str(FILES) + '/type|name|contents|'
    FILES = FILES.split('/')
    if mode == 'factory':
        ERRORS = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        RUNS = 0
    main()

def screenset(screen):
    global SCREEN, STARTBARVIS
    SCREEN = str(screen)
    main()
    STARTBARVIS = False

def login(username):
    global USERNAME
    if username == '' or username == ' ': None
    else: USERNAME = str(username)
    screenset('desktop')
    winsound.MessageBeep(1)
    taskbar()
    main()
    main()
    #shell()  #uncomment for released version

def appsearch(query):
    _ = str(query)
    _ = _.lower()
    global SCREENS, STARTBARVIS
    for __ in SCREENS:
        if __ == _ and _ != 'login':
            screenset(__)
            STARTBARVIS = False

def toggle_startbar_vis():
    global STARTBARVIS
    if STARTBARVIS == False: STARTBARVIS = True
    else: STARTBARVIS = False
    if STARTBARVIS == True:
        canvas(OS, 200, 300, 'black', 0, 0, 450)
        buttont(OS, 9, 1, 'black', 'white', 0, 'pos()', 10, 460, 'Power off')
        buttont(OS, 12, 1, 'black', 'white', 0, 'screenset("desktop")', 10, 490, 'Home screen')
        buttont(OS, 14, 1, 'black', 'white', 0, 'screenset("settings")', 10, 520, 'System settings')
        searchquery = Entry(OS, bg = 'gray70', fg = 'blue')
        searchquery.place(x = 5, y = 715)
        Button(OS, text = 'Search', bg = 'black', fg = 'white', command = lambda: appsearch(searchquery.get()), borderwidth = 0, activebackground = 'black', activeforeground = 'black').place(x = 135, y = 715)
    else: main()

def taskbar():
    canvas(OS, 1580, 50, 'black', 0, 0, 750)
    buttont(OS, 3, 1, 'black', 'white', 0, 'toggle_startbar_vis()', 10, 760, 'H.os')
    buttont(OS, 20, 1, 'black', 'white', 0, 'screenset("files")', 70, 760, 'Files')
    buttont(OS, 20, 1, 'black', 'white', 0, 'screenset("python")', 200, 760, 'Python')            ##
    buttont(OS, 20, 1, 'black', 'white', 0, 'screenset("notepad")', 330, 760, 'Notepad')
    buttont(OS, 20, 1, 'black', 'white', 0, 'screenset("calculator")', 460, 760, 'Calculator')

def gettime():
    OLD = str(localtime())
    YEAR = str((OLD.split(',')[0]).split('=')[1])
    MONTH = str((OLD.split(',')[1]).split('=')[1])
    DAY = str((OLD.split(',')[2]).split('=')[1])
    HOUR = str((OLD.split(',')[3]).split('=')[1])
    MINUTE = str((OLD.split(',')[4]).split('=')[1])
    SECOND = str((OLD.split(',')[5]).split('=')[1])
    if len(str(MINUTE)) == 1: MINUTE = '0' + str(MINUTE)
    NEW = [(MONTH + '/' + DAY + '/' + YEAR + '-' + HOUR + ':'+ MINUTE), SECOND]
    return NEW

def run(script, save):
    global ERRORS
    if save == False:
        NEW = ''
        for _ in range(20):
            NEW = str(NEW) + str(script[_]) + '\n'
        try: exec(NEW)
        except OverflowError: ERRORS[1] += 1
        except SyntaxError: ERRORS[0] += 1
        except ValueError: ERRORS[2] += 1
        except IndexError: ERRORS[3] += 1
        except OSError: ERRORS[4] += 1
        except PermissionError: ERRORS[5] += 1
        except NameError: ERRORS[6] += 1
        except ImportError: ERRORS[7] += 1
        except TypeError: ERRORS[8] += 1
    elif save == True:
        NEW = ''
        for _ in range(20):
            NEW = str(NEW) + str(script[_]) + '\n'
        return NEW

class files():
    def savefile(filename, filetype, contents):
        global FILES
        DONE = False
        for _ in range(25):
            if DONE == False and FILES[_] == ('type|name|contents|'): DONE = _
        REP = (str(filetype) + '|' + str(filename) + '|' + str(contents) + '|')
        FILES[DONE] = REP
        main()
    def startfile(fileno):
        global FILES
        FILE = FILES[(fileno - 1)]
        if str(FILE).split('|')[0] == '.exe': exec(str(str(FILE).split('|')[2]))
        elif str(FILE).split('|')[0] == '.txt':
            cover('tan')
            buttont(OS, 6, 1, 'tan', 'black', 2, 'screenset("files")', 10, 10, '<----')
            label(OS, 'tan', 'black', str(FILE.split('|')[2]), 10, 50)
        elif str(FILE).split('|')[0] == '.mp3': exec(str(str(FILE).split('|')[2]))
    def test():
        files.savefile('exe_test', '.exe', 'sys_gen_notif("The test worked")')
        files.savefile('mp3_test', '.mp3', 'winsound.MessageBeep()')
        files.savefile('txt_test', '.txt', 'This is a test\n1\n2\n3\n4\n5\nThis document was displayed succsessfully')

def savenotepad(document, name):
    document_new = ''
    for _ in document: document_new = str(document_new) + str(_) + '\n'
    files.savefile(str(name), '.txt', str(document_new))

def shell():
    global ERRORS, FILES
    print ('HarrisonOS command line shell restart ///// shell version 1.0.0 ///// harrisonOS version 1.8.0')
    print ('Type "help" for command line help\n')
    try:
        while True:
            command = str(input('HarrisonOS//cmd//shell> '))
            if command == 'help':
                print ('''
    ----------------------------COMMANDS---------------------------

    netstat = DISPLAYS THE NATIVE NETWORK INFORMATION
    errors = DISPLAYS THE SYSTEM ERROR COUNT
    python[python command] = EXECUTES THE SELECTEF PYTHON COMMAND
    included = DISPLAYS THE NATIVE SYSTEM MODULES
    quit = EXITS THE COMMAND SHELL
    exit = EXITS THE HarrisonOS APPLICATION

    ----------------------------CLASSES----------------------------

    files {
        .init|filename|filetype|filecontents
        .startfile|filenumber
        .test
        .files
    }

    os {
        .error|errortype
        .notif|notification
        .exec|pythonCommand
    }

    screen {
        .set|screenName
        .refresh
    }
    ''')
            elif command == 'netstat':
                print (os.getcwd())
                print (os.getlogin())
                print (os.getppid())
                print (os.getpid())
                print (os.cpu_count())
            elif command == 'errors': print (ERRORS)
            elif command == 'quit': break
            elif command == 'exit':
                if str(input('Are you sure (y/n)? ')).lower() == 'y':
                    exit()
                    quit()
            elif command == 'included':
                print (tkinter, random, sys, os, math, time, winsound)
            elif command.split('.')[0] == 'files':
                if (command.split('.')[1])[0:4] == 'init': files.savefile((str(command.split('init')[1]).split('|')[0]), str(command.split('|')[1]), str(command.split('|')[2]))
                elif (command.split('.')[1]).split('|')[0] == 'startfile': files.startfile(int(command.split('|')[1]))
                elif (command.split('.')[1]) == 'test': files.test()
                elif (command.split('.')[1]) == 'files': print (FILES)
            elif command.split('.')[0] == 'screen':
                if command.split('.')[1] == 'refresh': main()
                elif (command.split('.')[1]).split('|')[0] == 'set': screenset(str(command.split('|')[1]))
            elif command.split('.')[0] == 'os':
                if (command.split('.')[1]).split('|')[0] == 'error': sys_error_notif(str(command.split('|')[1]))
                elif (command.split('.')[1]).split('|')[0] == 'notif': sys_gen_notif(str(command.split('|')[1]))
                elif (command.split('.')[1]).split('|')[0] == 'exec': exec(str(command.split('|')[1]))
            else: print ('ERROR:\n  <stdin>\n   Unknown command: ' + str(command))
    except SyntaxError:
        ERRORS[0] += 1
        sys_error_notif(SyntaxError)
        shell()
    except OverflowError:
        ERRORS[1] += 1
        sys_error_notif(OverflowError)
        shell()
    except ValueError:
        ERRORS[2] += 1
        sys_error_notif(ValueError)
        shell()
    except IndexError:
        ERRORS[3] += 1
        sys_error_notif(IndexError)
        shell()
    except OSError:
        ERRORS[4] += 1
        sys_error_notif(OSError)
        shell()
    except PermissionError:
        ERRORS[5] += 1
        sys_error_notif(PermissionError)
        shell()
    except NameError:
        ERRORS[6] += 1
        sys_error_notif(NameError)
        shell()
    except ImportError:
        ERRORS[7] += 1
        sys_error_notif(ImportError)
        shell()
    except TypeError:
        ERRORS[8] += 1
        sys_error_notif(TypeError)
        shell()

def cmdinterpret(command):#syntaxerror, overflowerror, valueerror, indexerror, oserror, permissionerror, nameerror, importerror, typeerror
    global ERRORS, SCREENS, SCREEN, RUNS
    command = str(command)
    canvas(OS, 1580, 690, 'black', 0, 0, 0)
    try:
        if command == 'help': label(OS, 'black', 'green', """
----------------------------- SYSTEM COMMANDS [CASE SENSITIVE] -----------------------------

netstat = GIVES THE NATIVE NETWORK INFORMATION
dvc = TAKES YOU TO THE DEVICE HANDLING SCREEN
errors = DISPLAYS THE SYSTEM ERROR COUNT
screens = DISPLAYS THE SYSTEM APPLICATIONS/SCREENS
self.error.[error type] = RAISES THE DESIGNATED ERROR
self.exec./python command/ = EXECUTES THE DESIGNATED COMMAND
self.runs = DISPLAYS THE SYSTEM RUN COUNT
zimbawe = STRANGER STUFF
shell_init = RUNS THE HARRISON OS RAW COMMAND LINE
restart <uxi949> = REBOOTS AND CLEARS THE SYSTEM
restart <fac326> = FACTORY RESETS THE COMPUTER
""", 10, 10)
        elif command == 'dvc': screenset('dvc')
        elif command == 'netstat':
            label(OS, 'black', 'green', os.getlogin(), 10, 10)
            label(OS, 'black', 'green', os.getppid(), 10, 30)
            label(OS, 'black', 'green', os.getpid(), 10, 50)
            label(OS, 'black', 'green', os.cpu_count(), 10, 70)
        elif command == 'errors': label(OS, 'black', 'green', ('SyntaxError: ' + str(ERRORS[0]) + '\nOverflowError: ' + str(ERRORS[1]) + '\nValueError: ' + str(ERRORS[2]) + '\nIndexError: ' + str(ERRORS[3]) + '\nOSError: ' + str(ERRORS[4]) + '\nPermissionError: ' + str(ERRORS[5]) + '\nNameError: ' + str(ERRORS[6]) + '\nImportError: ' + str(ERRORS[7]) + '\nTypeError: ' + str(ERRORS[8])), 10, 10)
        elif command == 'screens':
            label(OS, 'black', 'green', SCREENS, 10, 10)
            label(OS, 'black', 'green', ('Current screen: ' + str(SCREEN)), 10, 30)
        elif command.split('.')[0] == 'self':
            if command.split('.')[1] == 'error': exec(str('raise ' + str((command.split('[')[1]).split(']')[0])))
            elif (command.split('.')[1].split('/')[0]) == 'exec' or (command.split('.')[1].split('/')[0]) == ' exec': exec(str(command.split('/')[1]))
            elif (command.split('.')[1]) == 'runs': label(OS, 'black', 'green', RUNS, 10, 10)
        elif command == 'zimbawe':
            for _ in range(500):
                sys_error_notif(SyntaxError)
                sys_gen_notif('SoMe StRaNgE sTuFf tHiS iS')
            sys_gen_notif('You might want to abort this OS process :D', 'exit()\nquit()')
        elif command == 'shell_init': shell()
        elif command == 'restart <uxi949>': restart_os(None)
        elif command == 'restart <fac326>': restart_os('factory')
    except SyntaxError:
        ERRORS[0] += 1
        sys_error_notif(SyntaxError)
    except OverflowError:
        ERRORS[1] += 1
        sys_error_notif(OverflowError)
    except ValueError:
        ERRORS[2] += 1
        sys_error_notif(ValueError)
    except IndexError:
        ERRORS[3] += 1
        sys_error_notif(IndexError)
    except OSError:
        ERRORS[4] += 1
        sys_error_notif(OSError)
    except PermissionError:
        ERRORS[5] += 1
        sys_error_notif(PermissionError)
    except NameError:
        ERRORS[6] += 1
        sys_error_notif(NameError)
    except ImportError:
        ERRORS[7] += 1
        sys_error_notif(ImportError)
    except TypeError:
        ERRORS[8] += 1
        sys_error_notif(TypeError)

def label(root_, bg_, fg_, text_, x_, y_): Label(root_, bg = bg_, fg = fg_, text = text_).place(x = x_, y = y_)
def canvas(root_, width_, height_, bg_, bw_, x_, y_): Canvas(root_, width = width_, height = height_, bg = bg_, highlightthickness = bw_).place(x = x_, y = y_)
def cover(bg_): Canvas(OS, width = 1580, height = 750, highlightthickness = 0, bg = bg_).place(x = 0, y = 0)
def button(root_, width_, height_, bg_, fg_, bw_, command_, x_, y_): Button(root_, width = width_, height = height_, bg = bg_, fg = fg_, activebackground = bg_, activeforeground = fg_, borderwidth = bw_, command = lambda: exec(str(command_))).place(x = x_, y = y_)
def buttont(root_, width_, height_, bg_, fg_, bw_, command_, x_, y_, text_): Button(root_, text = text_, width = width_, height = height_, bg = bg_, fg = fg_, activebackground = bg_, activeforeground = fg_, borderwidth = bw_, command = lambda: exec(str(command_))).place(x = x_, y = y_)

def pos():
    canvas(OS, 1580, 800, 'black', 0, 0, 0)
    label(OS, 'black', 'white', 'Powering off...', 700, 370)
    def qt():
        quit()
        exit()
    def rt():
        screenset('desktop')
        taskbar()
        main()
    Button(OS, command = lambda: qt(), borderwidth = 2, bg = 'black', fg = 'white', text = 'Shut down').place(x = 706, y = 400)
    Button(OS, command = lambda: rt(), borderwidth = 2, bg = 'black', fg = 'white', text = 'Cancel').place(x = 713, y = 430)

def main():
    OS.update()
    OS.update_idletasks()
    Tk.update(OS)
    Tk.update_idletasks(OS)
    global SCREENS, SCREEN, FILES, EMAILS, STARTBARVIS, RUNS, LASTRUNTIME, CALS_VARS
    RUNS += 1
    start = time.time()
    try:
        if SCREEN == 'login':
            OS.configure(bg = 'blue')
            canvas(OS, 1580, 800, 'gray73', 0, 0, 0)
            label(OS, 'gray73', 'black', 'Username:', 600, 400)
            u_E = Entry(OS, width = 70, bg = 'white', fg = 'purple3')
            u_E.place(x = 670, y = 400)
            l_B = Button(OS, text = 'Login', bg = 'black', fg = 'white', activebackground = 'green', activeforeground = 'green', command = lambda: login(u_E.get()))
            l_B.place(x = 850, y = 430)
            button(OS, 1, 10, 'black', 'black', 0, "button(OS, 1, 10, 'blue', 'black', 0, None, 700, 100)", 700, 100)
            button(OS, 10, 1, 'black', 'black', 0, "button(OS, 10, 1, 'blue', 'black', 0, None, 700, 170)", 700, 170)
            button(OS, 1, 10, 'black', 'black', 0, "button(OS, 1, 10, 'blue', 'black', 0, None, 770, 100)", 770, 100)
            button(OS, 1, 1, 'black', 'black', 0, "button(OS, 1, 1, 'green', 'black', 0, None, 800, 235)", 800, 235)
            button(OS, 10, 1, 'black', 'black', 0, "button(OS, 10, 1, 'purple', 'black', 0, None, 830, 235)", 830, 235)
            button(OS, 10, 1, 'black', 'black', 0, "button(OS, 10, 1, 'purple', 'black', 0, None, 830, 160)", 830, 160)
            button(OS, 1, 6, 'black', 'black', 0, "button(OS, 1, 6, 'purple', 'black', 0, None, 830, 160)", 830, 160)
            button(OS, 1, 6, 'black', 'black', 0, "button(OS, 1, 6, 'purple', 'black', 0, None, 900, 160)", 900, 160)
            button(OS, 1, 3, 'black', 'black', 0, "button(OS, 1, 3, 'purple', 'black', 0, None, 930, 160)", 930, 160)
            button(OS, 10, 1, 'black', 'black', 0, "button(OS, 10, 1, 'purple', 'black', 0, None, 930, 160)", 930, 160)
            button(OS, 10, 1, 'black', 'black', 0, "button(OS, 10, 1, 'purple', 'black', 0, None, 930, 190)", 930, 190)
            button(OS, 1, 3, 'black', 'black', 0, "button(OS, 1, 3, 'purple', 'black', 0, None, 993, 190)", 993, 190)
            button(OS, 10, 1, 'black', 'black', 0, "button(OS, 10, 1, 'purple', 'black', 0, None, 930, 235)", 930, 235)
            label(OS, 'gray73', 'black', '~ V1.8.0 ~', 840, 260)
        elif SCREEN == 'desktop':
            cover('green')
            button(OS, 10, 1, 'green1', 'black', 0, "button(OS, 10, 1, 'yellow', 'black', 0, None, 1504, 0)", 1504, 0)
            button(OS, 10, 1, 'green2', 'black', 0, "button(OS, 10, 1, 'red', 'black', 0, None, 1504, 22)", 1504, 22)
            button(OS, 10, 1, 'green2', 'black', 0, "button(OS, 10, 1, 'orange', 'black', 0, None, 1428, 0)", 1428, 0)
            button(OS, 10, 1, 'green3', 'black', 0, "button(OS, 10, 1, 'purple', 'black', 0, None, 1504, 44)", 1504, 44)
            button(OS, 10, 1, 'green3', 'black', 0, "button(OS, 10, 1, 'pink', 'black', 0, None, 1428, 22)", 1428, 22)
            button(OS, 10, 1, 'green3', 'black', 0, "button(OS, 10, 1, 'white', 'black', 0, None, 1352, 0)", 1352, 0)
            button(OS, 10, 1, 'green4', 'black', 0, "button(OS, 10, 1, 'gray', 'black', 0, None, 1504, 66)", 1504, 66)
            button(OS, 10, 1, 'green4', 'black', 0, "button(OS, 10, 1, 'green1', 'black', 0, None, 1428, 44)", 1428, 44)
            button(OS, 10, 1, 'green4', 'black', 0, "button(OS, 10, 1, 'purple', 'black', 0, None, 1352, 22)", 1352, 22)
            button(OS, 10, 1, 'green4', 'black', 0, "button(OS, 10, 1, 'red', 'black', 0, None, 1276, 0)", 1276, 0)
        elif SCREEN == 'files':
            cover('white')
            for __ in range(1, 25): buttont(OS, 200, 1, 'tan', 'black', 0, ("files.startfile(" + str((__ + 1)) + ")"), 10, (__ * 30), (str(FILES[__]).split('|')[1] + str(FILES[__]).split('|')[0]))
        elif SCREEN == 'python':
            cover('white')
            _01 = Entry(bg = 'white', width = 200, fg = 'blue')
            _01.place(x = 0, y = 10)
            _02 = Entry(bg = 'white', width = 200, fg = 'blue')
            _02.place(x = 0, y = 30)
            _03 = Entry(bg = 'white', width = 200, fg = 'blue')
            _03.place(x = 0, y = 50)
            _04 = Entry(bg = 'white', width = 200, fg = 'blue')
            _04.place(x = 0, y = 70)
            _05 = Entry(bg = 'white', width = 200, fg = 'blue')
            _05.place(x = 0, y = 90)
            _06 = Entry(bg = 'white', width = 200, fg = 'blue')
            _06.place(x = 0, y = 110)
            _07 = Entry(bg = 'white', width = 200, fg = 'blue')
            _07.place(x = 0, y = 130)
            _08 = Entry(bg = 'white', width = 200, fg = 'blue')
            _08.place(x = 0, y = 150)
            _09 = Entry(bg = 'white', width = 200, fg = 'blue')
            _09.place(x = 0, y = 170)
            _10 = Entry(bg = 'white', width = 200, fg = 'blue')
            _10.place(x = 0, y = 190)
            _11 = Entry(bg = 'white', width = 200, fg = 'blue')
            _11.place(x = 0, y = 210)
            _12 = Entry(bg = 'white', width = 200, fg = 'blue')
            _12.place(x = 0, y = 230)
            _13 = Entry(bg = 'white', width = 200, fg = 'blue')
            _13.place(x = 0, y = 250)
            _14 = Entry(bg = 'white', width = 200, fg = 'blue')
            _14.place(x = 0, y = 270)
            _15 = Entry(bg = 'white', width = 200, fg = 'blue')
            _15.place(x = 0, y = 290)
            _16 = Entry(bg = 'white', width = 200, fg = 'blue')
            _16.place(x = 0, y = 310)
            _17 = Entry(bg = 'white', width = 200, fg = 'blue')
            _17.place(x = 0, y = 330)
            _18 = Entry(bg = 'white', width = 200, fg = 'blue')
            _18.place(x = 0, y = 350)
            _19 = Entry(bg = 'white', width = 200, fg = 'blue')
            _19.place(x = 0, y = 370)
            _20 = Entry(bg = 'white', width = 200, fg = 'blue')
            _20.place(x = 0, y = 390)
            saveas = Entry(bg = 'tan', fg = 'black')
            saveas.place(x = 60, y = 462.5)
            label(OS, 'white', 'blue', 'Use double spaces instead of indents for script writing. Do not refresh the screen without saving your script.', 0, 410)
            Button(bg = 'blue', fg = 'white', text = 'Save as:', command = lambda: files.savefile(str(saveas.get()), '.exe', (run([_01.get(), _02.get(), _03.get(), _04.get(), _05.get(), _06.get(), _07.get(), _08.get(), _09.get(), _10.get(), _11.get(), _12.get(), _13.get(), _14.get(), _15.get(), _16.get(), _17.get(), _18.get(), _19.get(), _20.get()], True)))).place(x = 0, y = 460)
            Button(bg = 'blue', fg = 'white', text = 'Execute script', command = lambda: run([_01.get(), _02.get(), _03.get(), _04.get(), _05.get(), _06.get(), _07.get(), _08.get(), _09.get(), _10.get(), _11.get(), _12.get(), _13.get(), _14.get(), _15.get(), _16.get(), _17.get(), _18.get(), _19.get(), _20.get()], False)).place(x = 0, y = 430)
        elif SCREEN == 'cmd':
            cover('black')
            commandentry = Entry(bg = 'black', fg = 'green2', width = 100)
            commandentry.place(x = 50, y = 700)
            Button(OS, text = '>>>', bg = 'black', fg = 'green2', command = lambda: cmdinterpret(commandentry.get()), borderwidth = 0, activebackground = 'black', activeforeground = 'green').place(x = 10, y = 700)
        elif SCREEN == 'dvc':
            cover('orange')
        elif SCREEN == 'notepad':
            cover('gray50')
            canvas(OS, 500, 500, 'white', 0, 600, 25)
            _1 = Entry(bg = 'white', width = 82, fg = 'black')
            _1.place(x = 602, y = 25)
            _2 = Entry(bg = 'white', width = 82, fg = 'black')
            _2.place(x = 602, y = 45)
            _3 = Entry(bg = 'white', width = 82, fg = 'black')
            _3.place(x = 602, y = 65)
            _4 = Entry(bg = 'white', width = 82, fg = 'black')
            _4.place(x = 602, y = 85)
            _5 = Entry(bg = 'white', width = 82, fg = 'black')
            _5.place(x = 602, y = 105)
            _6 = Entry(bg = 'white', width = 82, fg = 'black')
            _6.place(x = 602, y = 125)
            _7 = Entry(bg = 'white', width = 82, fg = 'black')
            _7.place(x = 602, y = 145)
            _8 = Entry(bg = 'white', width = 82, fg = 'black')
            _8.place(x = 602, y = 165)
            _9 = Entry(bg = 'white', width = 82, fg = 'black')
            _9.place(x = 602, y = 185)
            _10 = Entry(bg = 'white', width = 82, fg = 'black')
            _10.place(x = 602, y = 205)
            _11 = Entry(bg = 'white', width = 82, fg = 'black')
            _11.place(x = 602, y = 225)
            _12 = Entry(bg = 'white', width = 82, fg = 'black')
            _12.place(x = 602, y = 245)
            _13 = Entry(bg = 'white', width = 82, fg = 'black')
            _13.place(x = 602, y = 265)
            _14 = Entry(bg = 'white', width = 82, fg = 'black')
            _14.place(x = 602, y = 285)
            _15 = Entry(bg = 'white', width = 82, fg = 'black')
            _15.place(x = 602, y = 305)
            _16 = Entry(bg = 'white', width = 82, fg = 'black')
            _16.place(x = 602, y = 325)
            _17 = Entry(bg = 'white', width = 82, fg = 'black')
            _17.place(x = 602, y = 345)
            _18 = Entry(bg = 'white', width = 82, fg = 'black')
            _18.place(x = 602, y = 365)
            _19 = Entry(bg = 'white', width = 82, fg = 'black')
            _19.place(x = 602, y = 385)
            _20 = Entry(bg = 'white', width = 82, fg = 'black')
            _20.place(x = 602, y = 405)
            _21 = Entry(bg = 'white', width = 82, fg = 'black')
            _21.place(x = 602, y = 425)
            _22 = Entry(bg = 'white', width = 82, fg = 'black')
            _22.place(x = 602, y = 445)
            _23 = Entry(bg = 'white', width = 82, fg = 'black')
            _23.place(x = 602, y = 465)
            _24 = Entry(bg = 'white', width = 82, fg = 'black')
            _24.place(x = 602, y = 485)
            _25 = Entry(bg = 'white', width = 82, fg = 'black')
            _25.place(x = 602, y = 505)
            Button(OS, text = 'Save as:', bg = 'black', fg = 'white', command = lambda: savenotepad([_1.get(), _2.get(), _4.get(), _5.get(), _6.get(), _7.get(), _8.get(), _9.get(), _10.get(), _11.get(), _12.get(), _13.get(), _14.get(), _15.get(), _16.get(), _17.get(), _18.get(), _19.get(), _20.get(), _21.get(), _22.get(), _23.get(), _24.get(), _25.get()], _name.get())).place(x = 600, y = 540)
            _name = Entry(OS, width = 20, bg = 'white', fg = 'blue')
            _name.place(x = 660, y = 542.5)
        elif SCREEN == 'settings':
            cover('gray32')
            label(OS, 'gray32', 'black', 'Settings menu', 700, 10)
            buttont(OS, (1 + len('date and time')), 1, 'gray32', 'black', 2, 'screenset("settings/time")', 20, 20, 'Date and time')
            buttont(OS, (1 + len('Debug console')), 1, 'gray32', 'black', 2, 'screenset("cmd")', 20, 60, 'Debug console')
            buttont(OS, (1 + len('System colors')), 1, 'gray32', 'black', 2, 'screenset("settings/color")', 20, 100, 'System colors')
        elif SCREEN == 'settings/time':
            canvas(OS, 1000, 650, 'white', 0, 500, 50)
            label(OS, 'white', 'black', 'Time and date settings', 500, 50)
        elif SCREEN == 'settings/color':
            canvas(OS, 1000, 650, 'white', 0, 500, 50)
            label(OS, 'white', 'black', 'System color preferences', 500, 50)
        elif SCREEN == 'calculator':
           cover('cyan3')
        if SCREEN != 'login': label(OS, 'black', 'white', str(gettime()).split("'")[1], 1450, 760)
        end = time.time()
        LASTRUNTIME = (end - start)
    except SyntaxError:
        ERRORS[0] += 1
        sys_error_notif(SyntaxError)
    except OverflowError:
        ERRORS[1] += 1
        sys_error_notif(OverflowError)
    except ValueError:
        ERRORS[2] += 1
        sys_error_notif(ValueError)
    except IndexError:
        ERRORS[3] += 1
        sys_error_notif(IndexError)
    except OSError:
        ERRORS[4] += 1
        sys_error_notif(OSError)
    except PermissionError:
        ERRORS[5] += 1
        sys_error_notif(PermissionError)
    except NameError:
        ERRORS[6] += 1
        sys_error_notif(NameError)
    except ImportError:
        ERRORS[7] += 1
        sys_error_notif(ImportError)
    except TypeError:
        ERRORS[8] += 1
        sys_error_notif(TypeError)

def sys_error_notif(ertype):
    x = random.randint(100, 1000)
    y = random.randint(50, 530)
    canvas(OS, 400, 200, 'gray', 2, x, y)
    label(OS, 'gray32', 'black', 'Error                                                                                                                           ', (x + 2), (y + 2))
    label(OS, 'gray', 'black', ('Type of error: ' + str(ertype)), (x + 30), (y + 50))
    buttont(OS, 3, 1, 'gray', 'black', 1, "main()", (x + 200), (y + 100), 'Ok')

def sys_gen_notif(notif, command = 'main()'):
    x = random.randint(100, 1000)
    y = random.randint(50, 530)
    canvas(OS, 400, 200, 'gray', 2, x, y)
    label(OS, 'gray32', 'black', 'Notification                                                                                                             ', (x + 2), (y + 2))
    label(OS, 'gray', 'black', (str(notif)), (x + 30), (y + 50))
    buttont(OS, 3, 1, 'gray', 'black', 1, command, (x + 200), (y + 100), 'Ok')

files.test()
main()
label(OS, 'yellow', 'black', '( ͡° ͜ʖ ͡°)', 1850, 990)
OS.mainloop()
