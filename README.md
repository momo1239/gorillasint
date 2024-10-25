# g(O)rilla(SINT)
Gorillasint automates several OSINT tools to gather and separate information into separate files that can be used for password spraying and other attacks. This includes emails, possible usernames, hashes separated from dehashed output, cleartext passwords from dehashed, etc. 

# Prerequisites
- Dehashed - https://github.com/sm00v/Dehashed/tree/master
- Crosslinked - https://github.com/m8sec/CrossLinked
- Pymeta.py - https://github.com/m8sec/pymeta
- Phonebook.cz subscription
- Amass installed - https://github.com/owasp-amass/amass
  

# Setup 
Write all emails collected from phonebook.cz to `phonebook.txt` 
Your dehashed.py file must have the API key hard coded for this script to work

# Usage
```sh
python3 gorillasint.py -phonebook phonebook.txt -crosslinked "{first}.{last}@company.com" "Company Name from Linkedin" crosslinked_output -d company.com -whois -pymeta -amass -dehashed
```

# Credit
The big credit goes to those that made dehashed, crosslinked, pymeta, amass, and phonebook.cz. This is just a simple automation of those tools to create usable files for further attacks.
