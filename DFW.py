#!/usr/bin/env python3

import os
import sys
from fpdf import FPDF
from datetime import datetime
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

class DoxingFramework:
    def __init__(self):
        self.clear_screen()
        self.version = "2.1"
        self.author = "Revanced by ASx"

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        print(Fore.CYAN + r"""
  ____            _                   _____                       __        __         _
 |  _ \  _____  _(_)_ __   __ _      |  ___| __ __ _ _ __ ___   __\ \      / /__  _ __| | __
 | | | |/ _ \ \/ / | '_ \ / _` |_____| |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
 | |_| |  __/>  <| | | | | (_| |_____|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 |____/ \___/_/\_\_|_| |_|\__, |     |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
                          |___/""")
        print(Fore.YELLOW + "=" * 80)
        print(Fore.GREEN + f"[#] Doxing Framework v{self.version} - {self.author}")
        print(Fore.RED + "[!] For educational/legal use only. Do not misuse.")
        print(Fore.YELLOW + "=" * 80 + Style.RESET_ALL)

    def print_menu(self):
        print(Fore.MAGENTA + "\n" + "=" * 35 + " MENU " + "=" * 35)
        print(Fore.CYAN + "[1]. Create Personal Profile")
        print("[2]. Create Company Profile")
        print("[3]. Generate PDF from TXT")
        print(Fore.RED + "[4]. Exit")
        print(Fore.MAGENTA + "=" * 76 + Style.RESET_ALL)

    def run(self):
        self.print_banner()
        while True:
            self.print_menu()
            choice = input(Fore.GREEN + "\n[?] Select an option [1-4]: " + Style.RESET_ALL).strip()
            
            if choice == "1":
                from personaldox import PersonalDox
                PersonalDox().run()
            elif choice == "2":
                from companydox import CompanyDox
                CompanyDox().run()
            elif choice == "3":
                self.txt_to_pdf()
            elif choice == "4":
                print(Fore.YELLOW + "\n[+] Exiting DFW. Goodbye!" + Style.RESET_ALL)
                sys.exit(0)
            else:
                input(Fore.RED + "\n[!] Invalid choice. Press Enter to continue..." + Style.RESET_ALL)
                self.clear_screen()

    def txt_to_pdf(self):
        txt_file = input(Fore.CYAN + "\n[?] Enter TXT filename (e.g., 'profile.txt'): " + Style.RESET_ALL).strip()
        if not os.path.exists(txt_file):
            print(Fore.RED + "[!] File not found!" + Style.RESET_ALL)
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open(txt_file, 'r') as f:
            for line in f:
                pdf.cell(200, 10, txt=line.strip(), ln=True)

        pdf_output = f"{os.path.splitext(txt_file)[0]}.pdf"
        pdf.output(pdf_output)
        print(Fore.GREEN + f"[+] PDF saved as '{pdf_output}'" + Style.RESET_ALL)

if __name__ == "__main__":
    DoxingFramework().run()