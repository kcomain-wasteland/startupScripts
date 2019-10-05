import subprocess as sp
import os
import json
from colorama import Fore as fo
from colorama import Style as st

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
black = fo.BLACK
danger = fo.RED
success = fo.GREEN
warning = fo.YELLOW
primary = fo.BLUE
info = fo.CYAN
r = fo.RESET

def danger(textd):
    print(dangerc+textd+r)

def success(textd):
    print(successc+textd+r)

def warning(textd):
    print(warningc+textd+r)

def info(textd):
    print(infoc+textd+r)

# Load json File.
try:
    json = open("C:\startup.json")
except FileNotFoundError:
    print('No file found. Create one using startup_setup.py.')
    print('Press enter to exit.')
    void = input()
    exit(0)
except:
    print('Something else went wrong. DM the developer (Kenny_#2763) on discord with the log(copy and paste the thing in the console.).')
    print('Press enter to exit.')
    void = input()
    exit(0)


json.close()