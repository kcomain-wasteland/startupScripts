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
    print(dangerc+textd+r)

def success(textd):
    print(successc+textd+r)

def warning(textd):
    print(warningc+textd+r)

def info(textd):
    print(infoc+textd+r)

def primary(textd):
    print(primaryc+textd+r)

def e(ecode):
    exit(ecode)

def tester(txtd):
    danger(txtd)
    success(txtd)
    warning(txtd)
    info(txtd)
    primary(txtd)
# Main
tester('Startup Test...')