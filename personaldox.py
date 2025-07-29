#!/usr/bin/env python3

import os
from datetime import datetime
from doxclear import clear, space
from colorama import Fore, Style
from textwrap import fill
from fpdf import FPDF

class PersonalDox:
    def __init__(self):
        self.clear = clear
        self.fields = {
            "Personal Information": {
                "Name": "Full name",
                "Mugshot": "Mugshot photo URL",
                "Occupation": "Current occupation",
                "Race": "Race",
                "Ethnicity": "Ethnicity",
                "Gender": "Gender",
                "Sexuality": "Sexuality",
                "Relationship Status": "Relationship status",
                "D.O.B": "Date of birth (DD/MM/YYYY)",
                "Age": "Current age",
                "Mobile Phone": "Mobile phone number",
                "Home Phone": "Home phone number",
                "Direct Address": "Full physical address",
                "Country": "Country of residence",
                "State": "State/Province",
                "City": "City",
                "Town": "Town/Village",
                "ZIP": "Postal/ZIP code",
                "Information Link": "Any relevant information link"
            },
            "Online Presence": {
                "Online Alias": "Primary online alias",
                "Steam ID": "Steam profile URL/ID",
                "PSN ID": "PlayStation Network ID",
                "Xbox Gamertag": "Xbox Live gamertag",
                "Snapchat": "Snapchat username",
                "ooVoo": "ooVoo username",
                "Skype": "Skype username",
                "Email": "Primary email address",
                "Facebook": "Facebook profile URL",
                "Twitter": "Twitter profile URL",
                "YouTube": "YouTube channel URL",
                "Twitch": "Twitch channel URL",
                "Instagram": "Instagram profile URL",
                "Tumblr": "Tumblr blog URL",
                "Reddit": "Reddit username",
                "SoundCloud": "SoundCloud profile URL",
                "Website": "Personal website URL"
            },
            "IP Information": {
                "IP Address": "Current IP address",
                "Hostname": "Associated hostname",
                "Reverse DNS": "Reverse DNS record",
                "DNS Server": "DNS server information",
                "ASN Number": "Autonomous System Number",
                "ISP": "Internet Service Provider",
                "IP Range/Subnet": "Network range/subnet",
                "Registry": "IP registry information",
                "WHOIS Info": "WHOIS registration details"
            },
            "Family Members": {
                "Mother - Name": "Mother's full name",
                "Mother - Age/DOB": "Mother's age or birth date",
                "Mother - Mugshot": "Mother's photo URL",
                "Mother - Address": "Mother's address",
                "Mother - Phone": "Mother's phone number",
                "Mother - Facebook": "Mother's Facebook profile",
                
                "Father - Name": "Father's full name",
                "Father - Age/DOB": "Father's age or birth date",
                "Father - Mugshot": "Father's photo URL",
                "Father - Address": "Father's address",
                "Father - Phone": "Father's phone number",
                "Father - Facebook": "Father's Facebook profile",
                
                "Sibling - Name": "Sibling's full name",
                "Sibling - Age/DOB": "Sibling's age or birth date",
                "Sibling - Mugshot": "Sibling's photo URL",
                "Sibling - Address": "Sibling's address",
                "Sibling - Phone": "Sibling's phone number",
                "Sibling - Facebook": "Sibling's Facebook profile",
                
                "Partner - Name": "Partner's full name",
                "Partner - Age/DOB": "Partner's age or birth date",
                "Partner - Mugshot": "Partner's photo URL",
                "Partner - Address": "Partner's address",
                "Partner - Phone": "Partner's phone number",
                "Partner - Facebook": "Partner's Facebook profile"
            },
            "Residence Information": {
                "Property Address": "Full property address",
                "Floors": "Number of floors",
                "Rooms": "Total number of rooms",
                "Area (sqft)": "Property area in square feet",
                "Bedrooms": "Number of bedrooms",
                "Bathrooms": "Number of bathrooms",
                "Garage": "Garage information",
                "Condition": "Property condition",
                "Rent": "Monthly rent amount",
                "Property Value": "Estimated property value",
                "Property Photo": "Property photo URL",
                "Property Map": "Property map URL"
            },
            "Additional Information": {
                "Notes": "Any additional notes",
                "Chat Logs": "Relevant chat logs",
                "Other Evidence": "Other supporting evidence"
            }
        }

    def get_input(self, prompt):
        return input(Fore.CYAN + f"\n[?] {prompt}\n> " + Style.RESET_ALL).strip() or "N/A"

    def run(self):
        self.clear()
        print(Fore.YELLOW + "\n\t🅿 🅴 🆁 🆂 🅾 🅽 🅰 🅻   🅳 🅾 🆇   🅿 🆁 🅾 🅵 🅸 🅻 🅴" + Style.RESET_ALL)
        
        data = {}
        for section, fields in self.fields.items():
            space()
            print(Fore.MAGENTA + f"\n[+] {section.upper()}" + Style.RESET_ALL)
            data[section] = {name: self.get_input(prompt) for name, prompt in fields.items()}

        self.save_outputs(data)

    def save_outputs(self, data):
        filename = input(Fore.CYAN + "\n[?] Save as (without extension): " + Style.RESET_ALL).strip()
        
        # Save as TXT
        self.save_txt(data, filename)
        
        # Save as PDF
        self.save_pdf(data, filename)
        
        print(Fore.GREEN + f"\n[✓] Files saved as '{filename}.txt' and '{filename}.pdf'" + Style.RESET_ALL)
        input(Fore.YELLOW + "\n[!] Press Enter to continue..." + Style.RESET_ALL)

    def save_txt(self, data, filename):
        with open(f"{filename}.txt", 'w') as f:
            f.write(f"╔{'═'*78}╗\n")
            f.write(f"║{'PERSONAL DOX PROFILE':^78}║\n")
            f.write(f"║{'Generated on " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "':^78}║\n")
            f.write(f"╚{'═'*78}╝\n\n")
            
            for section, fields in data.items():
                f.write(f"┌{'─'*78}┐\n")
                f.write(f"│ {section.upper():<77}│\n")
                f.write(f"├{'─'*78}┤\n")
                for name, value in fields.items():
                    if len(name + value) > 70:
                        wrapped_value = fill(value, width=50, subsequent_indent=' '*(len(name)+4))
                        f.write(f"│ • {name + ':':<25} {wrapped_value:<50}│\n")
                    else:
                        f.write(f"│ • {name + ':':<25} {value:<50}│\n")
                f.write(f"└{'─'*78}┘\n\n")

    def save_pdf(self, data, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_margins(left=15, top=15, right=15)
        
        # Header
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Personal Dox Profile', 0, 1, 'C')
        pdf.set_font('Arial', '', 10)
        pdf.cell(0, 10, f'Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1, 'C')
        pdf.ln(10)
        
        # Content
        pdf.set_font('Arial', '', 12)
        for section, fields in data.items():
            pdf.set_font('Arial', 'B', 14)
            pdf.cell(0, 10, section, 0, 1)
            pdf.set_font('Arial', '', 12)
            
            col_width = pdf.w - 2 * pdf.l_margin
            line_height = pdf.font_size * 2.5
            
            for name, value in fields.items():
                if not value.strip():
                    value = "N/A"
                
                # Write field name
                pdf.set_font('Arial', 'B', 12)
                pdf.cell(60, line_height, f"{name}:", border=0)
                
                # Write field value with proper wrapping
                pdf.set_font('Arial', '', 12)
                pdf.multi_cell(col_width - 60, line_height, value, border=0)
                
                # Add small space between fields
                pdf.ln(line_height / 3)
            
            # Add space between sections
            pdf.ln(line_height / 2)
        
        pdf.output(f"{filename}.pdf")

if __name__ == "__main__":
    PersonalDox().run()