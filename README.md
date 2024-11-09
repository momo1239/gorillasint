# g(O)rilla(SINT)
Gorillasint automates several OSINT tools to gather and separate information into separate files that can be used for password spraying and other attacks. This includes emails, possible usernames, hashes separated from dehashed output, cleartext passwords from dehashed, etc. 

# Prerequisites
- Dehashed - https://github.com/sm00v/Dehashed/tree/master
- Crosslinked - https://github.com/m8sec/CrossLinked
- Pymeta.py - https://github.com/m8sec/pymeta
- Phonebook - https://github.com/AD2011/phonebook.cz_scrapper
- Amass installed - https://github.com/owasp-amass/amass
- Trevorspray installed - https://github.com/blacklanternsecurity/TREVORspray
  

# Setup 
Your dehashed.py and phonebook.py file must have the API key hard coded for this script to work

# Usage
```sh
python3 gorillasint.py -phonebook -crosslinked "{first}.{last}@company.com" "Company Name from Linkedin" crosslinked_output -d company.com -whois -pymeta -amass -dehashed -enum_users
```

# Credit
The big credit goes to those that made dehashed, crosslinked, trevorspray, onedrive_enum, pymeta, amass, and phonebook.cz. This is just a simple automation of those tools to create usable files for further attacks.
