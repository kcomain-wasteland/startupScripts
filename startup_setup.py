from colorama import Fore as fo
from colorama import Style as st
blackc = fo.BLACK
dangerc = fo.RED
successc = fo.GREEN
warningc = fo.YELLOW
primaryc = fo.BLUE
infoc = fo.CYAN
r = fo.RESET

global cfg
cfg = "{\n"
print('Welcome to the startup json setup.\n')
print('Please fill in all the informations as they are all compulsory.')

def addEntry():
    n = input('Name: ')
    wd = input('Working Directory: ')
    fi = input('File Name: ')
    temp = ""
    temp += '    "{}": {}\n'.format(n,'{')
    temp += '        "working": "{}",\n'.format(wd)
    temp += '        "file": "{}"\n'.format(fi)
    temp += '    }'
    print(temp)
    return temp

def danger(textd):
    print(dangerc+textd+r)

def success(textd):
    print(successc+textd+r)

def warning(textd):
    print(warningc+textd+r)

def info(textd):
    print(infoc+textd+r)


cfg += addEntry()
while True:
    yn = input('Any more startup processes?[Y/N]: ')
    print('yn: ' + yn)
    if yn == 'y' or 'Y':
        print('yes')
        cfg += ',\n'
        cfg += addEntry()
    elif yn == 'n' or 'N':
        break
    else:
        print('breaking')
        break

    yn = ''

cfg += '\n}'
print(cfg)
jfile = open("autostartup.json", "w")
jfile.write(cfg)
print(jfile)
jfile.close()
exit(0)