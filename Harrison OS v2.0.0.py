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

COLORS  =['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


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
                                                                             '\n' + str(math)), justify = 'left', font = 'Courier_new 9').place(x = 20, y = 20)
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

def set_color(for_what, color, error_stage):
    global COLORS, DESKTOP_COLOR
    error_stage = str(error_stage)
    color = str(color)
    for_what = str(for_what)
    if for_what == 'desktop':
        if color in COLORS:
            DESKTOP_COLOR = color
        else:
            if error_stage == '':
                None

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
            elif SCREEN.split('/')[1] == 'disc_info':
                Label(FRAME, text = 'Direct reading off of the disc:', bg = 'gray', fg = 'black').place(x = 20, y = 20)
                try:
                    Label(FRAME, text = str(open(str(USERNAME + '.haros')).read()), bg = 'gray', fg = 'black', font = 'Courier_new 8', justify = 'left').place(x = 20, y = 50)
                except:
                    Label(FRAME, text = ('Error reading disc under the name of ') + str(USERNAME), bg = 'gray', fg = 'black').place(x = 20, y = 50)
            elif SCREEN.split('/')[1] == 'privacy': pass
            elif SCREEN.split('/')[1] == 'colors':
                color_desktop = Entry(width = 20)
                color_desktop.place(x = 250, y = 20)
                Button(activebackground = 'gray', activeforeground = 'black', borderwidth = 0, text = 'Press here to set the desktop color to: ', bg = 'gray', fg = 'black', command = lambda: set_color('desktop', str(color_desktop.get()))).place(x = 20, y = 20)
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
