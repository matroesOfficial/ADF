#!/usr/bin/env python3

from personaldox import PersonalDox

class CompanyDox(PersonalDox):
    def __init__(self):
        super().__init__()
        self.fields = {
            "Company Overview": {
                "Legal Name": "Official company name",
                "Phone": "Main contact number",
                "Email": "Public email address",
                "Physical Address": "Headquarters location"
            },
            "Technical Infrastructure": {
                "Domain": "Primary website URL",
                "IP Addresses": "Public IP addresses",
                "Server OS": "Detected operating systems"
            },
            "Network Analysis": {
                "Open Ports": "Discovered open ports",
                "Services": "Running services"
            },
            "Additional Intelligence": {
                "Findings": "Notable discoveries"
            }
        }

    def run(self):
        self.clear()
        print(Fore.YELLOW + "\n\t🅲 🅾 🅼 🅿 🅰 🅽 🆈   🅳 🅾 🆇   🅿 🆁 🅾 🅵 🅸 🅻 🅴" + Style.RESET_ALL)
        super().run()

if __name__ == "__main__":
    CompanyDox().run()