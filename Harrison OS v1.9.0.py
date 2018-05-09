import tkinter, random, os, sys, time, winsound
from tkinter import messagebox
from time import localtime
from tkinter import *

OS = Tk()
OS.title('Harrison OS v1.9.0')
OS.minsize(width = 1580, height = 800)
OS.maxsize(width = 1580, height = 800)

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

def disc(mode = 'c', write = ''):
    global SCREENS, USERNAME, RUNS_GLOBAL, RUNS_LOCAL, VERSION, INVALID_FILE_LETTERS, FILES, DATE_DISC_CREATED
    if mode == 'c':
        dir_c = str(os.getcwd())
        if ('Harrison OS v1.9.0 log.txt' in str(os.listdir(dir_c))) == True: return True
        if ('Harrison OS v1.9.0 log.txt' in str(os.listdir(dir_c))) == False:
            if messagebox.askquestion('HarrisonOS', 'There is no log script, create one?') == 'yes':
                FILES = ''
                for _ in range(100): FILES = str(FILES) + '/type|name|contents|'
                file = open('Harrison OS v1.9.0 log.txt', 'w')
                file.write(']00:00:00:00:00:00]0]' + str(FILES) + ']' + '1.9.0]' + ']y]python(v3.5.0). tcl/tkinter is required!]' + str(str((gettime())).split("'")[1]) + ']')
                #username]last_runtime]runs_global]global_runs]files]version]password]first_time_usage]python_version]
                file.close()
                OS.destroy()
                os.startfile('Harrison OS v1.9.0.py')
            else:
                quit()
                exit()
                os.abort()
    elif mode == 'w':
        file = open('Harrison OS v1.9.0 log.txt', 'w')
        file.write(str(write))
        file.close()
    elif mode == 'r':
        file = open('Harrison OS v1.9.0 log.txt', 'r')
        a = str(file.read())
        file.close()
        return str(a)
    elif mode == ':fill:':
        file = open('Harrison OS v1.9.0 log.txt', 'w')
        a = str(str(USERNAME) + ']' + str((gettime())[0]) + ']' + str(RUNS_GLOBAL) + ']' + str(FILES) + ']' + str(VERSION) + ']' + str(PASSWORD) + ']' + str(FIRST_TIME_SETUP) + ']' + str(PYTHON_VERSION_REQUIRED) + ']' + str(DATE_DISC_CREATED) + ']')
        file.write('')
        file.write(str(a))
        file.close()

disc(mode = 'c')

try:
    USERNAME = str(disc(mode = 'r')).split(']')[0]
    PASSWORD = str(disc(mode = 'r')).split(']')[5]
    RUNS_GLOBAL = int(str(disc(mode = 'r')).split(']')[2])
    RUNS_LOCAL = 0
    VERSION = str(disc(mode = 'r')).split(']')[4]
    INVALID_FILE_LETTERS = '/|]'
    SCREENS = ['login', 'desktop', 'files', 'settings', 'applications']
    FILES = str(disc(mode = 'r')).split(']')[3]
    LAST_COMPUTER_USAGE = str(disc(mode = 'r')).split(']')[1]
    SCREEN = 'login'
    FIRST_TIME_SETUP = str(disc(mode = 'r')).split(']')[6]
    STARTBARVIS = False
    PYTHON_VERSION_REQUIRED = str(disc(mode = 'r')).split(']')[7]
    DATE_DISC_CREATED = str(disc(mode = 'r')).split(']')[8]
except:
    messagebox.showwarning('Oh noes!', 'HarrisonOS local drive is corrupt!')
    disc(mode = 'c')
    os.remove('Harrison OS v1.9.0 log.txt')

def screenset(screen):
    global SCREEN
    SCREEN = str(screen)
    main()

def power_off(fcb):
    disc(mode = ':fill:')
    if fcb == True:
        quit()
        exit()
        os.abort()
    else:
        canvas(BG = 'black', BW = 0, HEIGHT = 800, WIDTH = 1580, X = 0, Y = 0)
        button(BW = 2, TEXT = 'Shut off', COMMAND = lambda: power_off(True), WIDTH = len('Shut off'), X = 700, Y = 400)
        button(BW = 2, TEXT = 'Cancel', COMMAND = lambda: exec('''
screenset('desktop')
taskbar(True)
main()
main()
'''), WIDTH = len('Cancel'), X = 700, Y = 430)

def label(ROOT = OS, BG = 'gray', FG = 'black', TEXT = '', X = 0, Y = 0): Label(ROOT, bg = BG, fg = FG, text = TEXT).place(x = X, y = Y)
def canvas(ROOT = OS, WIDTH = 50, HEIGHT = 50, BG = 'green', BW = 2, X = 0, Y = 0): Canvas(ROOT, bg = BG, highlightthickness = BW, width = WIDTH, height = HEIGHT).place(x = X, y = Y)
def cover(BG): Canvas(OS, width = 1580, height = 750, highlightthickness = 0, bg = BG).place(x = 0, y = 0)
def button(ROOT = OS, AFG = 'white', ABG = 'black', WIDTH = 2, HEIGHT = 1, BG = 'black', FG = 'white', TEXT = '', COMMAND = 'None', BW = 0, X = 0, Y = 0): Button(ROOT, activebackground = ABG, activeforeground = AFG, width = WIDTH, height = HEIGHT, bg = BG, fg = FG, text = TEXT, command = COMMAND, borderwidth = BW).place(x = X, y = Y)

def startbarvistoggle():
    global STARTBARVIS
    if STARTBARVIS == False: STARTBARVIS = True
    else: STARTBARVIS = False
    if STARTBARVIS == True:
        canvas(BG = 'black', BW = 0, WIDTH = 200, HEIGHT = 300, X = 0, Y = 450)
        button(COMMAND = lambda: power_off(False), TEXT = 'Power off', X = 10, Y = 460, WIDTH = 10)
        button(COMMAND = lambda: screenset('desktop'), TEXT = 'Home screen', X = 10, Y = 490, WIDTH = 12)
        button(COMMAND = lambda: screenset('settings'), TEXT = 'Settings', X = 10, Y = 520, WIDTH = 8)
        button(COMMAND = lambda: disc(mode = ':fill:'), TEXT = 'Save', X = 10, Y = 550, WIDTH = 6)
        button(COMMAND = lambda: screenset('applications'), TEXT = 'Applications', X = 10, Y = 580, WIDTH = 12)
    else: main()

def taskbar(co):
    if co == True:
        label(TEXT = str(gettime()).split("'")[1], X = 1470, Y = 762.5, BG = 'black', FG = 'white')
    else:
        canvas(BG = 'black', BW = 0, WIDTH = 1580, HEIGHT = 50, X = 0, Y = 750)
        button(COMMAND = lambda: startbarvistoggle(), BG = 'black', FG = 'white', WIDTH = 5, TEXT = 'OS', X = 10, Y = 763)
        button(COMMAND = lambda: screenset('files1'), TEXT = 'Files', WIDTH = 20, BG = 'black', FG = 'white', X = 70, Y = 763)
        label(TEXT = str(gettime()).split("'")[1], X = 1470, Y = 762.5, BG = 'black', FG = 'white')

def validate_password_entry(password_entered, username_entered):
    global SCREEN, PASSWORD, USERNAME
    password_entered = str(password_entered)
    username_entered = str(username_entered)
    if password_entered != PASSWORD or username_entered != USERNAME: label(BG = 'gray65', FG = 'red', TEXT = 'Invalid username or password', X = 745, Y = 460)
    elif password_entered == PASSWORD and username_entered == USERNAME:
        screenset('desktop')
        taskbar(False)
        main()
        main()
        winsound.MessageBeep(10)

def sys_win_not(TYPE = 'n', HEADING = 'Notification', NOTIFY = 'This is a notification', OP1 = 'Yes', OP2 = 'No', OP1C = 'print("a")', OP2C = 'print("b")', NOTIFBUTTONTEXT = 'Ok'):
    if TYPE == 'n' or TYPE == 'e':
        roots = [random.randint(0, 1000), random.randint(0, 400)]
        canvas(WIDTH = 400, HEIGHT = 200, BG = 'gray', BW = 2, X = roots[0], Y = roots[1])
        canvas(WIDTH = 400, BW = 0, HEIGHT = 22, BG = 'darkgray', X = (roots[0] + 2), Y = (roots[1] + 2))
        label(BG = 'darkgray', TEXT = HEADING, X = (roots[0] + 2), Y = (roots[1] + 2), FG = 'black')
        label(BG = 'gray', TEXT = NOTIFY, FG = 'black', X = (roots[0] + 70), Y = (roots[1] + 60))
        if TYPE == 'n': button(BG = 'lightgray', FG = 'black', TEXT = NOTIFBUTTONTEXT, BW = 2, COMMAND = lambda: main(), WIDTH = len(NOTIFBUTTONTEXT), X = (roots[0] + 150), Y = (roots[1] + 100))
        elif TYPE == 'e':
            button(BG = 'lightgray', FG = 'black', TEXT = OP1, BW = 2, COMMAND = lambda: exec(OP1C), WIDTH = len(OP1), X = (roots[0] + 100), Y = (roots[1] + 100))
            button(BG = 'lightgray', FG = 'black', TEXT = OP2, BW = 2, COMMAND = lambda: exec(OP2C), WIDTH = len(OP2), X = (roots[0] + 180), Y = (roots[1] + 100))

class files():
    def init(filename, filetype, contents):
        global FILES
        filename = str(filename)
        filetype = str(filetype)
        contents = str(contents)
        found = ''
        NEW = ''
        for _ in range(100):
            if FILES.split('/')[_] == 'type|name|contents|' and found == '': found = int(_)
        for ___ in range(found):
            NEW = str(NEW) + str(FILES.split('/')[___]) + '/'
        I = filetype + '|' + filename + '|' + contents
        NEW = str(NEW) + str(I)
        for __ in range((found + 1), 100): NEW = str(NEW) + '/' + str(FILES.split('/')[__])
        NEW
        FILES = str(NEW)
        FILES = str(FILES[0:(len(FILES) + 1)])
    def open(fileno):
        global FILES
        fileno = int(fileno)
        file = str(FILES.split('/')[(fileno)])
        filetype = file.split('|')[0]
        filename = file.split('|')[1]
        contents = file.split('|')[2]
        try:
            if filetype == '.exe': exec(contents)
            elif filetype == '.txt':
                cover('tan')
                button(BG = 'tan', ABG = 'tan2', FG = 'black', AFG = 'black', TEXT = 'Return to files', WIDTH = len('Return to files'), COMMAND = lambda: screenset('files1'), BW = 2, X = 30, Y = 30)
                Label(OS, text = contents, bg = 'tan', fg = 'black').place(x = 30, y = 80)
        except: return False

def filepage(up_dn):
    global SCREEN
    if up_dn == 'd':
        if SCREEN == 'files1': SCREEN = 'files2'
        elif SCREEN == 'files2': SCREEN = 'files3'
        elif SCREEN == 'files3': SCREEN = 'files4'
        elif SCREEN == 'files4': SCREEN = 'files5'
        elif SCREEN == 'files5': SCREEN = 'files1'
    if up_dn == 'u':
        if SCREEN == 'files1': SCREEN = 'files5'
        elif SCREEN == 'files5': SCREEN = 'files4'
        elif SCREEN == 'files4': SCREEN = 'files3'
        elif SCREEN == 'files3': SCREEN = 'files2'
        elif SCREEN == 'files2': SCREEN = 'files1'
    main()

def sb(COMMAND, TEXT, X, Y): Button(OS, command = lambda: exec(COMMAND), text = TEXT, bg = 'white', activebackground = 'white', fg = 'black', activeforeground = 'black', width = 200).place(x = X, y = Y)

def reset_disc_item(item, rto):
    global PASSWORD, USERNAME
    if item == 'u': USERNAME = str(rto)
    elif item == 'p': PASSWORD = str(rto)
    disc(mode = ':fill:')
    main()

def main():
    global SCREENS, USERNAME, RUNS_GLOBAL, RUNS_LOCAL, VERSION, INVALID_FILE_LETTERS, FILES, PASSWORD, LAST_COMPUTER_USAGE, SCREEN, STARTBARVIS, DATE_DISC_CREATED
    RUNS_GLOBAL += 1
    RUNS_LOCAL += 1
    STARTBARVIS = False
    if SCREEN == 'login':
        canvas(BG = 'gray65', BW = 0, X = 0, Y = 0, WIDTH = 1580, HEIGHT = 800)
        button(WIDTH = 8, HEIGHT = 4, TEXT = str('User:\n\n' + str(USERNAME)), X = 800, Y = 300)
        uname_entry = Entry(OS, width = 50, bg = 'white', fg = str(random.choice(['black', 'purple', 'blue'])))
        uname_entry.place(x = 700, y = 400)
        label(BG = 'gray65', FG = 'black', TEXT = 'Username:', X = 630, Y = 400)
        pwd_entry = Entry(OS, width = 50, bg = 'white', fg = str(random.choice(['black', 'purple', 'blue'])))
        pwd_entry.place(x = 700, y = 430)
        label(BG = 'gray65', FG = 'black', TEXT = 'Password:', X = 630, Y = 430)
        button(TEXT = 'Login', BW = 2, COMMAND = lambda: validate_password_entry(pwd_entry.get(), uname_entry.get()), X = 800, Y = 500, WIDTH = 6)
    elif SCREEN == 'desktop':
        cover('green')
    elif SCREEN == 'files1':
        cover('tan')
        for A in range(1, 20):
            try: sb(str('files.open(' + str(A) + ')'), (str(FILES.split('/')[(A)]).split('|')[1] + str(FILES.split('/')[(A)]).split('|')[0]), 20, (30 * (A + 1)))
            except: None
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('u'), X = 1500, Y = 30, TEXT = 'Page up', WIDTH = 7)
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('d'), X = 1500, Y = 60, TEXT = 'Page dn', WIDTH = 7)
        label(BG = 'tan', FG = 'black', TEXT = 'Files 1 - 19', X = 1500, Y = 90)
    elif SCREEN == 'files2':
        cover('tan')
        for B in range(20, 40):
            try: sb(str('files.open(' + str(B) + ')'), (str(FILES.split('/')[(B)]).split('|')[1] + str(FILES.split('/')[(B)]).split('|')[0]), 20, (30 * (B + 1 - 20)))
            except: None
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('u'), X = 1500, Y = 30, TEXT = 'Page up', WIDTH = 7)
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('d'), X = 1500, Y = 60, TEXT = 'Page dn', WIDTH = 7)
        label(BG = 'tan', FG = 'black', TEXT = 'Files 20 - 39', X = 1500, Y = 90)
    elif SCREEN == 'files3':
        cover('tan')
        for C in range(40, 60):
            try: sb(str('files.open(' + str(C) + ')'), (str(FILES.split('/')[(C)]).split('|')[1] + str(FILES.split('/')[(C)]).split('|')[0]), 20, (30 * (C + 1 - 40)))
            except: None
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('u'), X = 1500, Y = 30, TEXT = 'Page up', WIDTH = 7)
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('d'), X = 1500, Y = 60, TEXT = 'Page dn', WIDTH = 7)
        label(BG = 'tan', FG = 'black', TEXT = 'Files 40 - 59', X = 1500, Y = 90)
    elif SCREEN == 'files4':
        cover('tan')
        for D in range(60, 80):
            try: sb(str('files.open(' + str(D) + ')'), (str(FILES.split('/')[(D)]).split('|')[1] + str(FILES.split('/')[(D)]).split('|')[0]), 20, (30 * (D + 1 - 60)))
            except: None
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('u'), X = 1500, Y = 30, TEXT = 'Page up', WIDTH = 7)
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('d'), X = 1500, Y = 60, TEXT = 'Page dn', WIDTH = 7)
        label(BG = 'tan', FG = 'black', TEXT = 'Files 60 - 79', X = 1500, Y = 90)
    elif SCREEN == 'files5':
        cover('tan')
        for E in range(80, 100):
            try: sb(str('files.open(' + str(E) + ')'), (str(FILES.split('/')[(E)]).split('|')[1] + str(FILES.split('/')[(E)]).split('|')[0]), 20, (30 * (E + 1 - 80)))
            except: None
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('u'), X = 1500, Y = 30, TEXT = 'Page up', WIDTH = 7)
        button(BG = 'tan', ABG = 'tan1', FG = 'black', AFG = 'black', BW = 2, COMMAND = lambda: filepage('d'), X = 1500, Y = 60, TEXT = 'Page dn', WIDTH = 7)
        label(BG = 'tan', FG = 'black', TEXT = 'Files 80 - 99', X = 1500, Y = 90)
    elif SCREEN == 'settings':
        cover('gray')
        button(TEXT = 'Disc status', WIDTH = len('Disc status'), COMMAND = lambda: screenset('settings/disc'), X = 30, Y = 30, BG = 'darkgray', ABG = 'gray', FG = 'BLACK', AFG = 'BLACK', BW = 2)
        button(TEXT = 'System diagnostics', WIDTH = len('System diagnostics'), COMMAND = lambda: screenset('settings/diag'), X = 30, Y = 60, BG = 'darkgray', ABG = 'gray', FG = 'BLACK', AFG = 'BLACK', BW = 2)
    elif SCREEN == 'settings/disc':
        exec('''
try:
    USERNAME = str(disc(mode = 'r')).split(']')[0]
    PASSWORD = str(disc(mode = 'r')).split(']')[5]
    RUNS_GLOBAL = int(str(disc(mode = 'r')).split(']')[2])
    RUNS_LOCAL = 0
    VERSION = str(disc(mode = 'r')).split(']')[4]
    INVALID_FILE_LETTERS = '/|]'
    SCREENS = ['login', 'desktop', 'files', 'settings']
    FILES = str(disc(mode = 'r')).split(']')[3]
    LAST_COMPUTER_USAGE = str(disc(mode = 'r')).split(']')[1]
    SCREEN = 'login'
    FIRST_TIME_SETUP = str(disc(mode = 'r')).split(']')[6]
    STARTBARVIS = False
    PYTHON_VERSION_REQUIRED = str(disc(mode = 'r')).split(']')[7]
    DATE_DISC_CREATED = str(disc(mode = 'r')).split(']')[8]
except:
    messagebox.showwarning('Oh noes!', 'HarrisonOS local drive is corrupt!')
    disc(mode = 'c')
    os.remove('Harrison OS v1.9.0 log.txt')
disc(mode = ':fill:')
''')
        cover('gray')
        canvas(BG = 'white', BW = 0, WIDTH = 600, HEIGHT = 500, X = 30, Y = 30)
        label(BG = 'white', FG = 'black', TEXT = 'Disc readings:', X = 30, Y = 30)
        label(BG = 'white', FG = 'black', TEXT = ('Username on disc = ' + str(USERNAME)), X = 30, Y = 60)
        label(BG = 'white', FG = 'black', TEXT = ('Global run count on disc = ' + str(RUNS_GLOBAL)), X = 30, Y = 80)
        label(BG = 'white', FG = 'black', TEXT = ('Harrison OS version on disc = ' + str(VERSION)), X = 30, Y = 100)
        label(BG = 'white', FG = 'black', TEXT = ('Last computer usage on disc = ' + str(LAST_COMPUTER_USAGE)), X = 30, Y = 120)
        label(BG = 'white', FG = 'black', TEXT = ('First time setup on disc = ' + str(FIRST_TIME_SETUP)), X = 30, Y = 140)
        label(BG = 'white', FG = 'black', TEXT = ('Python version required on disc = ' + str(PYTHON_VERSION_REQUIRED)), X = 30, Y = 160)
        label(BG = 'white', FG = 'black', TEXT = ('Password on disc = ' + str(PASSWORD)), X = 30, Y = 180)
        label(BG = 'white', FG = 'black', TEXT = ('Time of disc creation = ' + str(DATE_DISC_CREATED)), X = 30, Y = 200)
        canvas(BG = 'white', BW = 0, WIDTH = 600, HEIGHT = 500, X = 830, Y = 30)
        label(BG = 'white', FG = 'black', TEXT = 'Disc options:', X = 830, Y = 30)
        button(TEXT = 'Reset disc', WIDTH = len('Reset disc'), COMMAND = lambda: exec("""
if messagebox.askquestion('Harrison OS', 'Reset disc?') == 'yes':
    messagebox.showwarning('Oh noes!', 'HarrisonOS local drive is corrupt!')
    disc(mode = 'c')
    os.remove('Harrison OS v1.9.0 log.txt')
    exit()
    quit()
"""), BG = 'red', ABG = 'red', FG = 'white', AFG = 'red', BW = 2, X = 840, Y = 60)
        button(TEXT = 'Reset password to:', WIDTH = len('Reset password to:'), COMMAND = lambda: reset_disc_item('p', p.get()), BG = 'gray', ABG = 'gray', FG = 'black', AFG = 'black', BW = 2, X = 840, Y = 90)
        p = Entry(width = 50, bg = 'lightgray', fg = 'blue')
        p.place(x = 990, y = 92.5)
        button(TEXT = 'Reset username to:', WIDTH = len('Reset username to:'), COMMAND = lambda: reset_disc_item('u', u.get()), BG = 'gray', ABG = 'gray', FG = 'black', AFG = 'black', BW = 2, X = 840, Y = 120)
        u = Entry(width = 50, bg = 'lightgray', fg = 'blue')
        u.place(x = 990, y = 122.5)
        button(TEXT = 'Open disc', WIDTH = len('Open disc'), COMMAND = lambda: os.startfile('Harrison OS v1.9.0 log.txt'), BG = 'gray', ABG = 'gray', FG = 'black', AFG = 'black', BW = 2, X = 840, Y = 150)
        button(TEXT = '<-----', WIDTH = 6, COMMAND = lambda: screenset('settings'), BG = 'gray', FG = 'black', ABG = 'gray', AFG = 'gray', BW = 0, X = 10, Y = 720)
    elif SCREEN == 'settings/diag':
        cover('gray')
        button(TEXT = '<-----', WIDTH = 6, COMMAND = lambda: screenset('settings'), BG = 'gray', FG = 'black', ABG = 'gray', AFG = 'gray', BW = 0, X = 10, Y = 720)
    elif SCREEN == 'applications':
        cover('gray20')
        button(WIDTH = 10, HEIGHT = 4, TEXT = 'Files', FG = 'white', AFG = 'gray20', BG = 'black', ABG = 'gray20', COMMAND = lambda: screenset('files1'), X = 30, Y = 30)
    if SCREEN != 'login': taskbar(True)
    
if RUNS_GLOBAL == 0:
    files.init('EXE_TEST', '.exe', 'sys_win_not(TYPE = "n", HEADING = "EXE_TEST.exe", NOTIFY = "This executable program worked!")')
    files.init('TXT_TEST', '.txt', 'Hello, this is a text document!\n1\n2\n3\n4\n5\nThis document was succsessfully displayed.')

main()
main()
main()
OS.mainloop()
disc(mode = ':fill:')
