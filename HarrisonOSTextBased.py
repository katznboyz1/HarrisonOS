import sys, os, time
import urllib.request as urlreq

def ping(url, count):
    for pings in range(count):
        try:
            start = time.time()
            urlreq.urlopen(url)
            end = time.time()
            print ('%f milliseconds.' % (end - start))
        except:
            print ('Failure.')

class config():
    error = AssertionError #error catch variable

def command(c):
    try:
        c = str(c)
        if c.lower() == 'help':
            print ('''
EXIT - EXITS THE COMMAND SHELL
HELP - PRINTS THE HELP MENU
ECHO - PRINTS THE STRING ENTERED BY THE USER
PING <url> <count> - PINGS THE DESIGNATED URL ADDRESS
CD <dir> - SETS THE CURRENT RUNTIME DIRECTORY
DIR <dir> LISTS THE CONTENTS OF THE DIRECTORY
ERROR-CATCH <errortype> - SETS THE CATCH ERROR
MKDIR <name> - MAKES A NEW FOLDER IN THE CURRENT DIRECTORY
TYPE <filename> - GETS THE CONTENTS OF A TEXT FILE
''')
        elif c.lower() == 'exit':
            quit()
            exit()
            os.kill(os.getpid(), os.getppid())
            os.abort()
            sys.exit()
        elif c.split(' ')[0].lower() == 'echo':
            print (c[5:])
        elif c.split(' ')[0].lower() == 'ping':
            if c.split(' ')[1] != '' and 'https://' in c.split(' ')[1]:
                try:
                    if c.split(' ')[2] != '':
                        try:
                            pc = int(c.split(' ')[2])
                        except ValueError:
                            print ('Invalid ping ping.count parameter.')
                except IndexError:
                    pc = 4
                ping(c.split(' ')[1], pc)
            else:
                print ('Invalid parameters for ping command.')
        elif c.split(' ')[0].lower() == 'cd':
            if len(c) > 2:
                try:
                    os.chdir(c.split(' ')[1])
                except NotADirectoryError:
                    print ('"%s" is not a valid directory name.' % c.split(' ')[1])
            else:
                print (os.getcwd())
        elif c.split(' ')[0].lower() == 'dir':
            if len(c) > 3:
                try:
                    for item in os.listdir(c.split(' ')[1]):
                        print (item)
                except NotADirectoryError:
                    print ('"%s" is not a valid directory name.' % c.split(' ')[1])
            else:
                for item in os.listdir(os.getcwd()):
                    print (item)
        elif c.split(' ')[0].lower() == 'error-catch':
            if len(c) > 11:
                try:
                    exec('config.error = %s' % c.split(' ')[1])
                except:
                    print ('Error')
            else:
                print (config.error)
        elif c.split(' ')[0].lower() == 'mkdir':
            try:
                os.mkdir(c[6:])
            except:
                print ('Error')
        elif c.split(' ')[0].lower() == 'type':
            try:
                file = open(c[5:])
                contents = str(file.read())
                file.close()
                for line in contents.split('\n'): print (line)
            except:
                print ('Error')
        elif c == '':
            pass
        else:
            try:
                os.system(c)
            except:
                print ('Error')
    except config.error:
        print ('Error')

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

HarrisonOSTextBased command line on {}. HCL version {}
Type "help" for a list of commands.

'''.format(sys.platform, '1.0.0'))

while True:
    command(str(input(str(str(os.getcwd()) + '>>> '))))
