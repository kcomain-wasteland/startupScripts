from colorama import Fore as fo
# from colorama import Style as st
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
blackc = fo.BLACK
dangerc = fo.RED
successc = fo.GREEN
warningc = fo.YELLOW
primaryc = fo.BLUE
infoc = fo.CYAN 
r = fo.RESET

def danger(textd):
    print(dangerc+'[×] '+textd+r)

def success(textd):
    print(successc+'[✓] '+textd+r)

def warning(textd):
    print(warningc+'[!] '+textd+r)

def info(textd):
    print(infoc+'[i] '+textd+r)

def primary(textd):
    print(primaryc+'[*] '+textd+r)

def tester():
    danger('Tester text')
    success('Tester text')
    warning('Tester text')
    info('Tester text')
    primary('Tester text')

danger('Startup Test')
success('Startup Test')
warning('Startup Test')
info('Startup Test')
primary('Startup Test')
print('\n\n')
info('Thank you for using this simple module.\n    Made by Kenny(Discord:Kenny_#2763)')
primary('This script is distributed using the MIT license.')
info('Module should be properly imported after this text.')