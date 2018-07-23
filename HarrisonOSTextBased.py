import os, time

class harrisonos():
    class modules():
        included = {'os':True, 'math':False, 'tkinter':False, 'winsound':False, 'random':False, 'time':True, 'socket':False, 'urllib':False}
    class vars():
        totalruns = None
    class dirs():
        cdir = os.getcwd()
        master = str(os.getcwd()) + '\\HarrisonOSTextBasedStorageRepository'
    class fileHandling():
        class folders():
            def new():
                os.makedirs(harrisonos.dirs.cdir + '\\HarrisonOSTextBasedStorageRepository')
                file = open(str(harrisonos.dirs.master + '\\System.dll'), 'w')
                file.write("TOTAL_RUNS = 0")
                file.close()
                harrisonos.fileHandling.checking.existingSaves(True)
        class dll():
            def get(path):
                return open(path, 'r').read()
            def save(path, contents):
                file = open(path, 'w')
                file.write(contents)
                file.close()
            def saveSystem():
                harrisonos.fileHandling.dll.save(str(harrisonos.dirs.master + '\\System.dll'), str('TOTAL_RUNS = ' + str(harrisonos.vars.totalruns)))
        class checking():
            def existingSaves(execute):
                if 'HarrisonOSTextBasedStorageRepository' in os.listdir(harrisonos.dirs.cdir):
                    if execute == True:
                        return harrisonos.fileHandling.dll.get(harrisonos.dirs.master + '\\System.dll')
                else:
                    harrisonos.fileHandling.folders.new()
    def main(command):
        command = str(command)
        try:
            if command == 'help':
                print ('''
exit = QUITS THE HARRISON OS SHELL
help = PRINTS A DETAILED LIST OF COMMANDS
python `<COMMAND>` = EXECUTES THE DESIGNATED PYTHON COMMAND
import <MODULE NAME> = IMPORTS THE MODULE PACKAGE
included = DISPLAYS THE MODULE COUNTER
netstat = DISPLAYS NETWORK STATISTICS
getHtml <URL> = RETRIVES THE HTML OF THE URL
ping <URL> = GETS PING STATISTICS
rundir <DIRECTORY> = PRINTS THE CONTENTS OF A DIRECTORY
cdir = PRINTS THE CURRENT DIRECTORY
rundoc `<PATH>` = PRINTS THE CONTENTS OF A FILE

FOR MORE DETAILED HELP, DO "help <COMMAND>"
''')
            elif command == 'exit':
                harrisonos.fileHandling.dll.saveSystem()
                exit()
                quit()
                os.abort()
            elif command.split(' ')[0] == 'python':
                exec(command.split('`')[1])
            elif command == 'included':
                print (harrisonos.modules.included)
            elif command.split(' ')[0] == 'import':
                try:
                    harrisonos.modules.included[str(command.split(' ')[1])] = True
                    if command.split(' ')[1] == 'all':
                        for _ in harrisonos.modules.included:
                            harrisonos.modules.included[_] = True
                except:
                    pass
            elif command == 'netstat':
                if harrisonos.modules.included['socket'] == True:
                    print (socket.getfqdn())
                else:
                    print ('------')
                if harrisonos.modules.included['os'] == True:
                    print (os.getlogin())
                    print (os.getpid())
                    print (os.getppid())
                else:
                    print ('------')
            elif command.split(' ')[0] == 'getHtml':
                if harrisonos.modules.included['urllib'] == True:
                    print (urllib.request.urlopen(command.split(' ')[1]).read())
                else:
                    print ('------')
            elif command.split(' ')[0] == 'ping':
                for _ in range(int(command.split(' ')[2])):
                    start = time.time()
                    urllib.request.urlopen(command.split(' ')[1])
                    end = time.time()
                    print (str((end - start) * 1000) + ' milliseconds')
            elif command.split(' ')[0] == 'help':
                if command.split(' ')[1] == 'ping':
                    print ('ping <URL> <COUNT>')
                elif command.split(' ')[1] == 'import':
                    print ('import <MODULE>')
                else:
                    print ('Help not available for: ' + str(command.split(' ')[1]))
            elif command.split(' ')[0] == 'rundir':
                print (os.listdir(command.split(' ')[1]))
            elif command == 'cdir':
                print (os.getcwd())
            elif command.split(' ')[0] == 'rundoc':
                print (open(command.split('`')[1]).read())
        except:
            print ('Error')
exec(harrisonos.fileHandling.checking.existingSaves(True))
harrisonos.vars.totalruns = int(TOTAL_RUNS)

print ('''
 _____       _____
/     \\     /     \\
|     |     |     |
|     |     |     |
|      -----      |
|      -----      |
|     |     |     |
|     |     |     |
\\_____/     \\_____/

HarrisonOS.inc, copyright/copyleft 2018.
Type 'help' for more information.

''')

while True:
    harrisonos.vars.totalruns += 1
    try:
        if harrisonos.modules.included['os'] == True:
            import os
        if harrisonos.modules.included['math'] == True:
            import math
            from math import *
        if harrisonos.modules.included['tkinter'] == True:
            from tkinter import *
            import tkinter
            from tkinter import messagebox
            from tkinter import PhotoImage
        if harrisonos.modules.included['winsound'] == True:
            import winsound
        if harrisonos.modules.included['random'] == True:
            import random
        if harrisonos.modules.included['time'] == True:
            import time
            from time import localtime
        if harrisonos.modules.included['socket'] == True:
            import socket
        if harrisonos.modules.included['urllib'] == True:
            import urllib, urllib.request
    except ImportError:
        print ('\nSome modules were not properly imported.\n')
    harrisonos.main(input(('\\HarrisonOSTextBasedStorageRepository> ')))
    harrisonos.fileHandling.dll.saveSystem()
