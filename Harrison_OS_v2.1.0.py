'''
TODO:
[+] -Make a dict that can be parsed into a .json file for storing all system data. (_presets)
[+] -Make the clock
[-] -Make it so that the screen widget(desktopWindow) deletes itself and respawns every time main() is called in order to preserve memory.
[-] -Make different screens.
[-] -Actually use iterative loops like I should and stop retyping 5 line long sequences multiple times.
'''

import PyQt5, _thread
import os as _os
import time as _time
import sys as _sys
from PyQt5.QtWidgets import *
from time import localtime as _localtime
import asyncio as _asyncio

application = QApplication(_sys.argv)

window = QWidget()

def gettime():
    OLD = str(_localtime())
    YEAR = str((OLD.split(',')[0]).split('=')[1])
    MONTH = str((OLD.split(',')[1]).split('=')[1])
    DAY = str((OLD.split(',')[2]).split('=')[1])
    HOUR = str((OLD.split(',')[3]).split('=')[1])
    MINUTE = str((OLD.split(',')[4]).split('=')[1])
    SECOND = str((OLD.split(',')[5]).split('=')[1])
    if len(str(MINUTE)) == 1: MINUTE = '0' + str(MINUTE)
    NEW = [(MONTH + '/' + DAY + '/' + YEAR), (HOUR + ':' + MINUTE + ':' + SECOND)]
    return NEW

_presets = {
    'colors':{
        'applicationColorScheme':{
            'myapps':'white','desktop':'#4d4d4d',
        },
        'windowBackground':'#4d4d4d','windowForeground':'white','taskbarButtonBackgroundColor':'black','taskbarButtonForegroundColor':'white','taskbarBackgroundColor':'#404040',
        'taskbarButtonBackgroundColorHover':'dimgray','taskbarButtonForegroundHover':'white',
    },
    'window':{
        'lastSize':[window.width(), window.height()],'title':'Harrison OS v2.1.0 (BETA)','inWindowScreen':'desktop','username':'admin','startingWidth':800,'startingHeight':500,'minimumWidth':500,'minimumHeight':300,
    },
    'system_data':{
        'runs':0,'lasttime':gettime(),'screen':'desktop',
    }
}

def main():
    global _presets, desktopWindow, window
    _presets['system_data']['runs'] += 1
    '''
    desktopWindow = QWidget(window)
    desktopWindow.setStyleSheet('QWidget{background-color:white;border:none;}')
    desktopWindow.move(0, 40)'''
    refbutton1.setText(('REFRESH:' + str(_presets['system_data']['runs'])))
    backgroundColor = 'transparent'
    try:
        backgroundColor = _presets['colors']['applicationColorScheme'][str(_presets['system_data']['screen'])]
    except KeyError:
        pass
    desktopWindow.setStyleSheet(('QWidget{background-color:' + str(backgroundColor) + ';border:none;}'))
    desktopWindow.resize(window.width(), (window.height() - 80))
    _presets['system_data']['runs'] += 1
    taskbar_button_1.move(0, (window.height() - taskbar_button_1.height()))
    taskbar_button_2.move((taskbar_button_1.x() + taskbar_button_1.width() + 1), (window.height() - taskbar_button_2.height()))
    taskbar_button_3.move((taskbar_button_2.x() + taskbar_button_2.width() + 1), (window.height() - taskbar_button_3.height()))
    currentOpenAppButton.move((taskbar_button_3.x() + taskbar_button_3.width() + 1), (window.height() - currentOpenAppButton.height()))
    taskbar_timebutton.move((window.width() - taskbar_timebutton.width()), (window.height() - taskbar_button_3.height()))
    taskbar_background.move(0, (window.height() - taskbar_background.height()))
    taskbar_background.resize(window.width(), 41)


def thread_checkResizeThread():
    global _presets, window
    while (1):
        if ([window.width(), window.height()] != _presets['window']['lastSize']):
            main()
        _presets['window']['lastSize'] = [window.width(), window.height()]

def thread_timesetThread():
    global _presets
    while (1):
        _asyncio.sleep(1)
        if (_presets['system_data']['lasttime'] != gettime()):
            taskbar_timebutton.setText(gettime()[0] + '\n' + gettime()[1])
        _presets['system_data']['lasttime'] = gettime()

def registerclickcase(case, debug = False):
    global _presets
    case = str(case)
    case_id = str(case.split(':')[0])
    case_info = str(case.split(':')[1])
    if (case_id == 'setscreen'):
        print ('Attempting to set screen to: ' + case_info)
        _presets['system_data']['screen'] = case_info
        main()
    if (debug):
        print ('Case handled')

refbutton1 = QPushButton(window)
refbutton1.setStyleSheet('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['windowBackground']) + ';color:' + str(_presets['colors']['windowForeground']) + ';border:1px solid black;border-radius:3px;}')
refbutton1.setText('REFRESH')
refbutton1.resize(110, 20)
refbutton1.move(0, 0)
refbutton1.clicked.connect(lambda: main())
refbutton2 = QPushButton(window)
refbutton2.setStyleSheet('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['windowBackground']) + ';color:' + str(_presets['colors']['windowForeground']) + ';border:1px solid black;border-radius:3px;}')
refbutton2.setText('EXIT')
refbutton2.resize(110, 20)
refbutton2.move(0, 20)
refbutton2.clicked.connect(lambda: exit())

taskbar_background = QWidget(window)
taskbar_background.resize(window.width(), 41)
taskbar_background.setStyleSheet('QWidget{background-color:' + str(_presets['colors']['taskbarBackgroundColor']) + ';}')
taskbar_button_1 = QPushButton(window)
taskbar_button_1.setStyleSheet('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColor']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundColor']) + ';border:1px solid black;border-radius:3px;}\n' +
'QPushButton:hover{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColorHover']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundHover']) + ';border:1px solid black;border-radius:3px;}')
taskbar_button_1.setText('H.os')
taskbar_button_1.resize(40, 40)
taskbar_button_1.clicked.connect(lambda: registerclickcase('setscreen:desktop'))
taskbar_button_2 = QPushButton(window)
taskbar_button_2.setStyleSheet('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColor']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundColor']) + ';border:1px solid black;border-radius:3px;}\n' +
'QPushButton:hover{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColorHover']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundHover']) + ';border:1px solid black;border-radius:3px;}')
taskbar_button_2.setText('Files')
taskbar_button_2.resize(100, 40)
taskbar_button_2.clicked.connect(lambda: registerclickcase('taskbarbutton2:none'))
taskbar_button_3 = QPushButton(window)
taskbar_button_3.setStyleSheet('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColor']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundColor']) + ';border:1px solid black;border-radius:3px;}\n' +
'QPushButton:hover{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColorHover']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundHover']) + ';border:1px solid black;border-radius:3px;}')
taskbar_button_3.setText('Settings')
taskbar_button_3.resize(100, 40)
taskbar_button_3.clicked.connect(lambda: registerclickcase('taskbarbutton3:'))

currentOpenAppButton = QPushButton(window)
currentOpenAppButton.setStyleSheet('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColor']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundColor']) + ';border:1px solid black;border-radius:3px;}\n' +
'QPushButton:hover{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColorHover']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundHover']) + ';border:1px solid black;border-radius:3px;}')
('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColor']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundColor']) + ';border:1px solid black;border-radius:3px;}')
currentOpenAppButton.setText('My Apps')
currentOpenAppButton.resize(100, 40)
currentOpenAppButton.clicked.connect(lambda: registerclickcase('setscreen:myapps'))

taskbar_timebutton = QPushButton(window)
taskbar_timebutton.setStyleSheet('QPushButton{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColor']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundColor']) + ';border:1px solid black;border-radius:3px;}\n' +
'QPushButton:hover{font-family:Verdana;font-size:13px;background-color:' + str(_presets['colors']['taskbarButtonBackgroundColorHover']) + ';color:' + str(_presets['colors']['taskbarButtonForegroundHover']) + ';border:1px solid black;border-radius:3px;}')
taskbar_timebutton.setText('N/A\nN/A')
taskbar_timebutton.resize(100, 40)
taskbar_timebutton.clicked.connect(lambda: registerclickcase('taskbarbuttontime:'))

desktopWindow = QWidget(window)
desktopWindow.setStyleSheet('QWidget{background-color:transparent;border:none;}')
desktopWindow.move(0, 40)
desktopWindow.resize(window.width(), (window.height() - 80))

window.setWindowTitle(str(_presets['window']['title']))
window.setStyleSheet(('QWidget{background-color:' + str(_presets['colors']['windowBackground']) + ';}'))
window.show()
window.resize(int(_presets['window']['startingWidth']), int(_presets['window']['startingHeight']))
window.setMinimumSize((int(_presets['window']['minimumWidth'])), (int(_presets['window']['minimumHeight'])))

#_thread.start_new_thread(thread_checkResizeThread, ())
_thread.start_new_thread(thread_timesetThread, ())

main()
main()

window.resizeEvent = main #this doesnt work ;-;

application.exec_()