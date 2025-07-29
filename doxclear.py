import os
from colorama import Fore, Style

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def space():
    print(Fore.BLUE + "=" * 80 + Style.RESET_ALL)