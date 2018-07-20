try:
    from tkinter import *
    from tkinter import messagebox
    import os, random, time, math, tkinter
    from time import localtime
except ImportError: input('One or more of the following modules could not be imported:\n    tkinter.*\n    tkinter.messagebox\n    os\n    random\n    time\n    math\n    tkinter\n')

class framework():
    class file_handling():
        def save(account_info = 'null', account_name = os.getlogin()):
            file = open(str(str(account_name) + '.haros'), 'w')
            file.write(str(account_info))
            file.close()
        def new(account_name = os.getlogin()):
            file = open(str(str(account_name) + '.haros'), 'w')
            file.write('USERNAME = "' + str(account_name) + '"\nPASSWORD = ""\nGLOBAL_RUNS = 0\nFILES = "' + str('|///' * 100) + '"\nRESOLUTION = "1200x600"\nSETUP = False\nDESKTOP_COLOR = "green"')
            file.close()
        def get(account_name = os.getlogin()):
            for _ in os.listdir(os.getcwd()):
                if '.haros' in str(_): account_name = _.split('.haros')[0]
            ret = ''
            file = open(str(str(account_name) + '.haros'), 'r')
            ret = file.read()
            file.close()
            return ret

def cover(color):
    global RESOLUTION
    Canvas(FRAME, bg = color, highlightthickness = 0, height = int(RESOLUTION.split('x')[1]), width = int(RESOLUTION.split('x')[0])).place(x = 0, y = 0)

TREE = '''
|DESKTOP:
|    SETTINGS:
|        SETTINGS/DISC_INFO
|        SETTINGS/PRIVACY
|        SETTINGS/DATE_TIME
|        SETTINGS/COLORS
|        SETTINGS/DISPLAY
|        
|    APPS:
|        PYTHON
|        CMD
|        CALCULATOR
|        NOTEPAD
|        
|    FILES:
|        SYSTEM FILES X100
'''
COMMANDS = '''
tree - Displays a tree of the system files/directories
exit - Exits the command shell and returns to the home screen
help - Displays a list of command shell commands
mods - Displays a list of included modules
netstat - Gives natvie network statistics
'''

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

def WH_set(WH, stage = False, refresh = True):
    global RESOLUTION, SCREEN
    if WH.count('x') == 1 and int(WH.split('x')[0]) >= 1200 and int(WH.split('x')[1]) >= 600:
        if stage == False: RESOLUTION = WH
        if stage == True:
            try:
                if int(WH.split('x')[0]) >= 1000 and int(WH.split('x')[1]) >= 500:
                    RESOLUTION = WH
                    Label(FRAME, bg = 'white', fg = 'green', text = 'Resolution submitted.').place(x = 20, y = 80)
                else: raise Exception
            except Exception: Label(FRAME, bg = 'white', fg = 'red', text = 'Invaild resolution.').place(x = 20, y = 80)
        if refresh == True: main()

def UNAME_set(uname, stage = False):
    global USERNAME
    if stage == False: USERNAME = str(uname)
    else:
        if uname != '' and uname != ' ':
            USERNAME = str(uname)
            Label(FRAME, bg = 'white', fg = 'green', text = 'Username submitted.').place(x = 20, y = 120)
        else: Label(FRAME, bg = 'white', fg = 'red', text = 'Invalid username.').place(x = 20, y = 120)

def screenset(screen):
    global SCREEN, SETUP
    if SETUP == False: SETUP = True
    SCREEN = str(screen)
    main()

def taskbar():
    global RESOLUTION, SCREEN
    H = int(RESOLUTION.split('x')[1])
    W = int(RESOLUTION.split('x')[0])
    Canvas(FRAME, width = W, height = 50, bg = 'black', highlightthickness = 0).place(x = 0, y = (H - 50))
    Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', text = 'H.os', command = lambda: togglestartbar(), borderwidth = 0).place(x = 10, y = (H - 38))
    Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', text = str(str(gettime()[0])), command = lambda: screenset('settings/date_time'), borderwidth = 0).place(x = (W - 100), y = (H - 38))
    if SCREEN != 'desktop': Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', text = SCREEN, command = lambda: None, borderwidth = 0).place(x = 70, y = (H - 38))

def login(password):
    H = int(RESOLUTION.split('x')[1])
    W = int(RESOLUTION.split('x')[0])
    if PASSWORD == password: screenset('desktop')
    else: Label(bg = 'lightgray', fg = 'red', text = 'Password does not match.').place(x = (W / 2.3), y = 223)

def save():
    global USERNAME, PASSWORD, GLOBAL_RUNS, FILES, LAST_CWD, RESOLUTION, SETUP, DESKTOP_COLOR
    framework.file_handling.save(account_name = USERNAME, account_info = str('USERNAME = "' + str(USERNAME) + '"\nPASSWORD = "' + str(PASSWORD) + '"\nGLOBAL_RUNS = ' + str(GLOBAL_RUNS) + '\nFILES = "' + str(FILES) +
                                 '"\nRESOLUTION = "' + str(RESOLUTION) + '"\nSETUP = ' + str(SETUP)) + '\nDESKTOP_COLOR = "' + str(DESKTOP_COLOR) + '"')

def terminate():
    global USERNAME, PASSWORD, GLOBAL_RUNS, FILES, LAST_CWD, RESOLUTION, SETUP, SCREEN, FRAME, startbarvis
    save()
    exit()
    quit()
    os.kill(os.getpid(), os.getppid())
    os.abort()
    for _ in range(100):
        exit()
        quit()
    os.startfile(str('taskkill /PID ' + str(os.getpid()) + ' /F.exe'))
    return 'Error'

def cmd_interperet(command):
    global SCREEN, TREE, COMMANDS, RESOLUTION
    command = str(command)
    H = int(RESOLUTION.split('x')[1])
    W = int(RESOLUTION.split('x')[0])
    Canvas(FRAME, bg = 'gray6', width = (W - 100), height = (H - 100), highlightthickness = 0).place(x = 0, y = 0)
    if command == 'exit': screenset('desktop')
    elif command == 'tree': Label(FRAME, bg = 'gray6', fg = 'white', text = TREE, justify = 'left', font = 'Courier_new 9').place(x = 20, y = 20)
    elif command == 'help': Label(FRAME, bg = 'gray6', fg = 'white', text = COMMANDS, justify = 'left', font = 'Courier_new 9').place(x = 20, y = 20)
    elif command == 'mods': Label(FRAME, bg = 'gray6', fg = 'white', text = (str(tkinter) + '\n' + str(tkinter.messagebox) + '\n' + str(os) + '\n' + str(random) + '\n' + str(time) + '\n' + str(time.localtime) +
                                                                             '\n' + str(math) + '\n' + str(winsound)), justify = 'left', font = 'Courier_new 9').place(x = 20, y = 20)
    elif command == 'netstat': Label(FRAME, bg = 'gray6', fg = 'white', text = ('Native user: ' + str(os.getlogin()) + '\nPID: ' + str(os.getpid()) + '\nPPID: ' + str(os.getppid())), justify = 'left', font = 'Courier_new 9').place(x = 20, y = 20)

def togglestartbar():
    global RESOLUTION, startbarvis
    H = int(RESOLUTION.split('x')[1])
    W = int(RESOLUTION.split('x')[0])
    if startbarvis == False: startbarvis = True
    else: startbarvis = False
    if startbarvis == True:
        Canvas(FRAME, width = 200, height = 300, bg = 'black', highlightthickness = 0).place(x = 0, y = (H - 350))
        Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', borderwidth = 0, text = 'Power off', command = lambda: terminate()).place(x = 20, y = (H - 330))
        Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', borderwidth = 0, text = 'Home', command = lambda: screenset('desktop')).place(x = 20, y = (H - 300))
        Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', borderwidth = 0, text = 'Settings', command = lambda: screenset('settings')).place(x = 20, y = (H - 270))
        Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', borderwidth = 0, text = 'Log out', command = lambda: screenset('login')).place(x = 20, y = (H - 240))
        Button(FRAME, bg = 'black', activebackground = 'black', fg = 'white', activeforeground = 'white', borderwidth = 0, text = 'My apps', command = lambda: screenset('apps')).place(x = 20, y = (H - 210))
    else: main()

def xbutton_handler():
    global RESOLUTION, SCREEN
    H = int(RESOLUTION.split('x')[1])
    W = int(RESOLUTION.split('x')[0])
    if SCREEN != 'desktop':
        Canvas(FRAME, highlightthickness = 0, bg = 'white', width = 95, height = 30).place(x = (W - 95), y = 0)
        Button(FRAME, borderwidth = 0, bg = 'lightgray', activebackground = 'red', fg = 'black', activeforeground = 'black', text = '  X  ', width = 5, command = lambda: screenset('desktop')).place(x = (W - 45), y = (2.5))
        Button(FRAME, borderwidth = 0, bg = 'lightgray', activebackground = 'lightgray', fg = 'black', activeforeground = 'black', text = '  -  ', width = 5, command = lambda: screenset('desktop')).place(x = (W - 90), y = (2.5))

def main():
    global USERNAME, PASSWORD, GLOBAL_RUNS, FILES, LAST_CWD, RESOLUTION, SETUP, SCREEN, FRAME, startbarvis, DESKTOP_COLOR
    startbarvis = False
    GLOBAL_RUNS += 1
    H = int(RESOLUTION.split('x')[1])
    W = int(RESOLUTION.split('x')[0])
    FRAME.destroy()
    FRAME = Frame(width = W, height = H, highlightthickness = 0, bg = 'gray')
    FRAME.place(x = 0, y = 0)
    OS.minsize(width = W, height = H)
    if SCREEN == 'login' and SETUP == False:
        cover('white')
        Label(FRAME, bg = 'white', fg = 'black', text = 'User preference setup part one:', font = 'Calibri_new 16').place(x = 20, y = 20)
        Label(FRAME, bg = 'white', fg = 'black', text = 'Enter your screen resolution here in WIDTHxHEIGHT format. EX: 1980x1080.').place(x = 20, y = 60)
        wh = Entry(FRAME, width = 50, bg = 'lightgray')
        wh.place(x = 430, y = 60)
        Button(FRAME, borderwidth = 0, bg = 'gray', fg = 'black', text = 'Submit resolution', command = lambda: WH_set(str(wh.get()), stage = True, refresh = False)).place(x = 800, y = 60)
        Label(FRAME, bg = 'white', fg = 'black', text = 'Enter your prefered username. This can be changed. EX: harrison.').place(x = 20, y = 100)
        uname = Entry(FRAME, width = 55, bg = 'lightgray')
        uname.place(x = 400, y = 100)
        Button(FRAME, borderwidth = 0, bg = 'gray', fg = 'black', text = 'Submit username', command = lambda: UNAME_set(str(uname.get()), stage = True)).place(x = 800, y = 100)
        Button(FRAME, bg = 'green', fg = 'black', text = 'Continue', font = 'Calibri_new 16', command = lambda: screenset('login'), activebackground = 'green', activeforeground = 'green').place(x = 400, y = 300)
    elif SCREEN == 'login' and SETUP == True:
        cover('lightgray')
        Button(FRAME, text = ('\n' + str(USERNAME) + '\n\n' + str(GLOBAL_RUNS) + '\n'), height = 5, width = 17, bg = 'gray', borderwidth = 0, activebackground = 'gray', activeforeground = 'blue').place(x = ((W / 2) - 50), y = 100)
        Label(FRAME, bg = 'lightgray', fg = 'black', text = 'Password:').place(x = (W / 2.6), y = 200)
        uname = Entry(FRAME, width = int(W / 40), show = '*')
        uname.place(x = (W / 2.3), y = 203)
        Button(FRAME, borderwidth = 0, bg = 'black', fg = 'white', text = 'Login', activebackground = 'black', activeforeground = 'white', command = lambda: login(str(uname.get()))).place(x = (W / 2), y = 245)
        Label(FRAME, bg = 'lightgray', fg = 'black', text = 'HarrisonOS copyright/left by Harrison Lindgren, harrisonos.co').place(x = (W - 340), y = (H - 20))
    elif SCREEN == 'desktop':
        cover(DESKTOP_COLOR)
        AOA = (int((H - 50) / 100) - 1)
        if AOA >= 1: Button(FRAME, bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'gray', command = lambda: screenset('notepad'), text = '''
__________
__________


Notepad
''', width = 11, height = 5, borderwidth = 0).place(x = 20, y = 20)
        if AOA >= 2: Button(FRAME, bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'gray', command = lambda: screenset('calculator'), text = '''

+ -
/ *

Calculator
''', width = 11, height = 5, borderwidth = 0).place(x = 20, y = 120)
        if AOA >= 3: Button(FRAME, bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'gray', command = lambda: screenset('python'), text = '''

print('py.exe')


Python
''', width = 11, height = 5, borderwidth = 0).place(x = 20, y = 220)
        if AOA >= 4: Button(FRAME, bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'gray', command = lambda: screenset('files'), text = '''

.txt .exe
.py

Files
''', width = 11, height = 5, borderwidth = 0).place(x = 20, y = 320)
        if AOA >= 5: Button(FRAME, bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'gray', command = lambda: screenset('cmd'), text = '''

>>>_

Command
Shell
''', width = 11, height = 5, borderwidth = 0).place(x = 20, y = 420)
    elif SCREEN.split('/')[0] == 'settings':
        cover('gray')
        try:
            if SCREEN.split('/')[1] == 'date_time':
                Label(FRAME, text = ('Current unparsed time: ' + str(localtime())), bg = 'gray', fg = 'black').place(x = 20, y = 20)
                Label(FRAME, text = ('Current parsed time: ' + str(gettime())), bg = 'gray', fg = 'black').place(x = 20, y = 40)
            elif SCREEN.split('/')[1] == 'disc_info': pass
            elif SCREEN.split('/')[1] == 'privacy': pass
            elif SCREEN.split('/')[1] == 'colors': pass
            elif SCREEN.split('/')[1] == 'display':
                Label(FRAME, text = str('Current display settings(px): [' + str(RESOLUTION) + ']'), bg = 'gray', fg = 'black').place(x = 20, y = 20)
                Label(FRAME, text = 'Enter new screen definition in WIDTHxHEIGHT format. EX: 1920x1020.', bg = 'gray', fg = 'black').place(x = 20, y = 60)
                redef = Entry(FRAME, width = 20, bg = 'lightgray', fg = 'black')
                redef.place(x = 400, y = 60)
                Button(FRAME, borderwidth = 0, bg = 'gray', activebackground = 'gray', fg = 'black', activeforeground = 'lightgray', command = lambda: WH_set(str(redef.get()), refresh = True), text = 'Press here to reset the screen definition.').place(x = 20, y = 85)
                Button(FRAME, borderwidth = 0, bg = 'gray', activebackground = 'gray', fg = 'black', activeforeground = 'lightgray', command = lambda: OS.state('zoomed'), text = 'Click here to maximize the window.').place(x = 20, y = 110)
                Button(FRAME, borderwidth = 0, bg = 'gray', activebackground = 'gray', fg = 'black', activeforeground = 'lightgray', command = lambda: OS.state('normal'), text = 'Click here to minimize the window.').place(x = 20, y = 135)
            Button(FRAME, bg = 'black', fg = 'white', activebackground = 'black', activeforeground = 'black', text = '<-----', command = lambda: screenset('settings'), borderwidth = 0).place(x = (W - 50), y = 60)
        except IndexError:
            Button(FRAME, bg = 'gray', fg = 'black', activebackground = 'gray', activeforeground = 'lightgray', text = 'Date and time', command = lambda: screenset('settings/date_time'), borderwidth = 1).place(x = 20, y = 20)
            Button(FRAME, bg = 'gray', fg = 'black', activebackground = 'gray', activeforeground = 'lightgray', text = 'Disc information', command = lambda: screenset('settings/disc_info'), borderwidth = 1).place(x = 20, y = 50)
            Button(FRAME, bg = 'gray', fg = 'black', activebackground = 'gray', activeforeground = 'lightgray', text = 'Privacy', command = lambda: screenset('settings/privacy'), borderwidth = 1).place(x = 20, y = 80)
            Button(FRAME, bg = 'gray', fg = 'black', activebackground = 'gray', activeforeground = 'lightgray', text = 'Colors', command = lambda: screenset('settings/colors'), borderwidth = 1).place(x = 20, y = 110)
            Button(FRAME, bg = 'gray', fg = 'black', activebackground = 'gray', activeforeground = 'lightgray', text = 'Display', command = lambda: screenset('settings/display'), borderwidth = 1).place(x = 20, y = 140)
    elif SCREEN == 'apps':
        cover('gray13')
        Button(FRAME, bg = 'gray13', fg = 'white', activebackground = 'gray13', activeforeground = 'lightgray', text = 'Settings', command = lambda: screenset('settings')).place(x = 20, y = (((H - 50) /  20) * 1))
        Button(FRAME, bg = 'gray13', fg = 'white', activebackground = 'gray13', activeforeground = 'lightgray', text = 'Python', command = lambda: screenset('python')).place(x = 20, y = (((H - 50) /  20) * 2))
        Button(FRAME, bg = 'gray13', fg = 'white', activebackground = 'gray13', activeforeground = 'lightgray', text = 'Command shell', command = lambda: screenset('cmd')).place(x = 20, y = (((H - 50) /  20) * 3))
        Button(FRAME, bg = 'gray13', fg = 'white', activebackground = 'gray13', activeforeground = 'lightgray', text = 'Calculator', command = lambda: screenset('calculator')).place(x = 20, y = (((H - 50) /  20) * 4))
    elif SCREEN == 'cmd':
        cover('gray6')
        Button(FRAME, borderwidth = 0, bg = 'gray6', activebackground = 'gray6', fg = 'green', activeforeground = 'green3', command = lambda: cmd_interperet(command_input.get()), text = '>>>').place(x = 20, y = (H - 90))
        command_input = Entry(FRAME, bg = 'gray20', fg = 'white', width = 60)
        command_input.place(x = 50, y = (H - 88.5))
    if SCREEN != 'login':
        taskbar()
        xbutton_handler()
    save()

OS = Tk()
OS.title('Harrison OS v2.0.0')
OS.minsize(width = 500, height = 250)
OS.configure(bg = 'blue')

FRAME = Frame(width = 500, height = 250, highlightthickness = 0, bg = 'gray')
FRAME.place(x = 0, y = 0)

SCREEN = 'login'
STARTBARVIS = False

if str(('.haros')) in str(os.listdir(os.getcwd())): exec(framework.file_handling.get())
else:
    framework.file_handling.new()
    exec(framework.file_handling.get())

main()

OS.mainloop()

save()
