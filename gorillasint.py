import argparse
import subprocess
import re
import os
import sys
import threading
import time
import shutil

def print_ascii_art():
    art = """

        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠛⠳⢤⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⣡⣶⣧⣤⣤⣌⢷⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣞⣫⣾⣿⣿⣿⣿⣿⣿⣞⡇⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠶⠶⠶⠶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠿⣿⣄⡀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣟⢦⣬⡽⠃⠀
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠀⢠⣾⣿⣿⡿⠛⠋⠀⠉⠉⠙⠻⣿⣿⣦⣿⣿⠿⠿⠛⠋⢙⣷⠀
       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠀⠀⣾⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣶⢀⣠⣭⣽⡆
        ⠀⠀⠀⠀⠀⠀⣠⣶⠶⠷⠿⠾⠶⠶⠶⠶⠶⠶⠿⠛⠁⠀⠀⠀⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢳⢿⣿⣿⣿⡟⠁⣼⠇⠀
        ⠀⠀⠀⠀⣠⡾⠋⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⣀⠀⠀⢸⡎⣿⣿⣿⣿⣛⡛⣻⠇
        ⠀⠀⠀⣰⠟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⡇⢹⣿⣿⡿⠿⠿⠋⠀
        ⠀⠀⢠⡟⣠⣾⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⣷⠈⠁⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡻⣿⣿⣿⣿⣿⣿⣿⣿⠘⣇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⣿⣧⡹⣦⡀⠀⠀⠀⠀⠀
        ⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⢸⣿⣿⣿⣿⡛⠓⠉⠉⠈⠻⣦⠀⠀⠀⠀
        ⠀⢰⡟⢻⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⣿⣿⣿⣿⣦⡀⠀⠀⠀⢿⡆⠀⠀⠀
        ⢠⡿⠁⠈⣿⣿⣿⣿⣿⣿⡇⢘⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣿⣿⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⣆⠀⠀⠸⣧⠀⠀⠀
        ⣿⡀⠀⠀⠸⣿⣿⣿⣿⣿⠁⠈⣿⣶⣶⣿⣿⣿⣿⣿⡿⠛⠛⠛⠉⣡⣾⣿⣿⣿⣿⣿⠃⠀⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⣿⡄⠀⠀
        ⢸⣿⣷⣤⣠⣬⣿⣿⣿⡟⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡄⠀⢹⡇⠀⠀
        ⠀⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣧⠀⢸⣷⠀⠀    
          ⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⡄⢸⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣤⣴⡿⠃⠀
           ________         _ _ _          _______ _____ _   _ _________  
          / / __ \ \       (_) | |        / / ____|_   _| \ | |__   __\ \ 
   __ _  | | |  | | |  _ __ _| | | __ _  | | (___   | | |  \| |  | |   | |
  / _` | | | |  | | | | '__| | | |/ _` | | |\___ \  | | | . ` |  | |   | |
 | (_| | | | |__| | | | |  | | | | (_| | | |____) |_| |_| |\  |  | |   | |
  \__, | | |\____/| | |_|  |_|_|_|\__,_| | |_____/|_____|_| \_|  |_|   | |
   __/ |  \_\    /_/                      \_\                         /_/ 
  |___/                                                                   
by 0xHarambehacks
    """
    print(art)

print_ascii_art()

#Usage: python3 gorillasint.py -phonebook -crosslinked "{first}.{last}@company.com" "Company Name from Linkedin" crosslinked_output -d company.com -whois -pymeta -amass -dehashed -enum_users
# Set the file locations for dehashed.py and pymeta.py and phonebook.py
DEHASHED_SCRIPT_PATH = "/path/to/dehashed.py"  # Set the path to dehashed.py
PYMETA_SCRIPT_PATH = "/path/to/pymeta.py"  # Set the path to pymeta.py
PHONEBOOK_SCRIPT_PATH = "/path/to/phonebook.py" # Set the path to phonebook.py

# Spinner Class
class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor

    def __init__(self, message):
        self.spinner_generator = self.spinning_cursor()
        self.message = message

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(f"\r{self.message} {next(self.spinner_generator)}")
            sys.stdout.flush()
            time.sleep(self.delay)

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        sys.stdout.write(f"\r{self.message} Done!\n")
        sys.stdout.flush()

def run_dehashed(domain, base_output_file):
    """Run dehashed.py with the provided domain and return the cracked and hash output files."""
    spinner = Spinner("Running dehashed...")
    spinner.start()
    
    command = f"python3 {DEHASHED_SCRIPT_PATH} -d {domain} -o {base_output_file}"
    subprocess.run(command, shell=True)
    
    spinner.stop()

    cracked_file = f"{base_output_file}_cracked.txt"
    hashes_file = f"{base_output_file}_hashes.txt"

    if not os.path.exists(cracked_file):
        raise FileNotFoundError(f"Dehashed cracked file '{cracked_file}' was not created. Check if dehashed.py ran correctly.")
    
    if not os.path.exists(hashes_file):
        raise FileNotFoundError(f"Dehashed hash file '{hashes_file}' was not created. Check if dehashed.py ran correctly.")

    return cracked_file, hashes_file

def run_crosslinked(format_str, company_name, output_file):
    """Run crosslinked with the provided format and company name."""
    spinner = Spinner("Running crosslinked...")
    spinner.start()

    output_file_with_ext = output_file if output_file.endswith(".txt") else output_file + ".txt"
    command = f'crosslinked -f "{format_str}" "{company_name}" -o {output_file}'
    subprocess.run(command, shell=True)

    spinner.stop()

    if not os.path.exists(output_file_with_ext):
        raise FileNotFoundError(f"Crosslinked output file '{output_file_with_ext}' was not created. Check if crosslinked ran correctly.")
    
    return output_file_with_ext

def run_whois(domain):
    """Run whois on the given domain and save output to whois_results.txt."""
    spinner = Spinner("Running whois...")
    spinner.start()

    with open("whois_results.txt", "w") as outfile:
        subprocess.run(f"whois {domain}", shell=True, stdout=outfile)

    spinner.stop()

def run_amass(domain):
    """Run amass on the given domain and save output to amass_results.txt."""
    spinner = Spinner("Running amass...")
    spinner.start()

    with open("amass_results.txt", "w") as outfile:
        subprocess.run(f"amass enum -d {domain}", shell=True, stdout=outfile)

    spinner.stop()

def run_pymeta(domain):
    """Run pymeta.py on the given domain and save output to pymeta_results.txt."""
    spinner = Spinner("Running pymeta.py...")
    spinner.start()

    with open("pymeta_results.txt", "w") as outfile:
        subprocess.run(f"python3 {PYMETA_SCRIPT_PATH} -d {domain}", shell=True, stdout=outfile)

    spinner.stop()

def extract_emails_from_file(file_path):
    """Extracts all emails from the given file."""
    emails = set()  # Use a set for deduplication
    with open(file_path, 'r') as f:
        for line in f:
            emails_in_line = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', line)
            emails.update(emails_in_line)
    return emails

def extract_usernames(emails):
    """Extract usernames by removing domain part from email."""
    usernames = set()
    for email in emails:
        username = email.split('@')[0]  # Get the part before the '@'
        usernames.add(username)
    return usernames

def extract_passwords_and_hashes(cracked_file, hashes_file):
    """Extracts passwords from the cracked file and only raw hashes from the hashes file."""
    passwords = set()
    hashes = set()

    with open(cracked_file, 'r') as f:
        for line in f:
            passwords.add(line.strip())

    with open(hashes_file, 'r') as f:
        for line in f:
            parts = re.split(r'[\s,:]', line.strip())
            raw_hash = max(parts, key=len)
            hashes.add(raw_hash)

    return passwords, hashes

def run_phonebook(domain):
    """ Run phonebook.py with the provided domain and save output to file. """
    spinner = Spinner("Running phonebook.py...")
    spinner.start()

    with open("phonebook.txt", "w") as outfile:
        command = f"python3 {PHONEBOOK_SCRIPT_PATH} -e -u {domain}"
        subprocess.run(command, shell=True, stdout=outfile)

    spinner.stop()

def run_trevorspray(domain):
    """Run trevorspray on the domain using emails.txt and enumerate valid users."""
    spinner = Spinner("Running trevorspray...")
    spinner.start()

    command = f"trevorspray --recon {domain} -u emails.txt --threads 10"
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input="onedrive\n")

    spinner.stop()

    if process.returncode != 0:
        print(f"Error running trevorspray: {stderr}")
    else:
        print("onedrive_enum success!")

        source_path = os.path.expanduser("~/.trevorspray/existent_users.txt")
        destination_path = "valid_emails.txt"

        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"Valid emails saved to {destination_path}.")
        else:
            print("Error: Existent users file not found.")






def save_to_file(data, file_path):
    """Save data to a file, one item per line."""
    with open(file_path, 'w') as f:
        for item in sorted(data):  
            f.write(f"{item}\n")

def main():
    parser = argparse.ArgumentParser(description="Combine OSINT tool outputs into a single file.")
    
    parser.add_argument('-d', required=True, help="Domain to be used with the tools")
    parser.add_argument('-phonebook', action='store_true', help="Run phonebook.py on the domain")
    parser.add_argument('-crosslinked', nargs=3, help="Arguments for crosslinked: format_str, company_name, output_file")
    parser.add_argument('-dehashed', action='store_true', help="Run dehashed.py on the domain")
    parser.add_argument('-whois', action='store_true', help="Run whois on the domain")
    parser.add_argument('-amass', action='store_true', help="Run amass on the domain")
    parser.add_argument('-pymeta', action='store_true', help="Run pymeta.py on the domain")
    parser.add_argument('-enum_users', action='store_true', help="Run trevorspray to enumerate valid users and emails")

    args = parser.parse_args()

    domain = args.d

    all_emails = set()
    all_usernames = set()
    all_passwords = set()
    all_hashes = set()


    if args.crosslinked:
        format_str, company_name, crosslinked_output = args.crosslinked
        crosslinked_file = run_crosslinked(format_str, company_name, crosslinked_output)
        crosslinked_emails = extract_emails_from_file(crosslinked_file)
        all_emails.update(crosslinked_emails)

    if args.dehashed:
        cracked_file, hashes_file = run_dehashed(domain, "dehashed_output")
        dehashed_emails = extract_emails_from_file(cracked_file)
        all_emails.update(dehashed_emails)

        passwords, hashes = extract_passwords_and_hashes(cracked_file, hashes_file)
        all_passwords.update(passwords)
        all_hashes.update(hashes)

    if args.whois:
        run_whois(domain)
    
    if args.amass:
        run_amass(domain)

    if args.pymeta:
        run_pymeta(domain)
    
    if args.phonebook:
        phonebook_file = "phonebook.txt"
        run_phonebook(domain)
        phonebook_emails = extract_emails_from_file(phonebook_file)
        all_emails.update(phonebook_emails)

    all_usernames = extract_usernames(all_emails)
    save_to_file(all_emails, "emails.txt")
    save_to_file(all_passwords, "passwords.txt")
    save_to_file(all_hashes, "hashes.txt")

    if args.enum_users:
        if os.path.exists("emails.txt"):
            run_trevorspray(domain)
        else:
            raise FileNotFoundError("emails.txt not found. Ensure the script generates emails.txt")


    print("OSINT data processing completed. Files saved: emails.txt, usernames.txt, passwords.txt, hashes.txt")
    print("Additional results saved to: whois_results.txt, amass_results.txt, pymeta_results.txt, phonebook.txt, valid_emails.txt (if applicable).")

if __name__ == "__main__":
    main()
