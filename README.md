# g(O)rilla(SINT)
Gorillasint automates dehashed.py, crosslinked, and output from phonebook.cz into separate files that can be used for password spraying and other attacks. This includes emails, possible usernames, hashes separated from dehashed output, cleartext passwords from dehashed, etc. 

# Prerequisites
- Dehashed https://github.com/sm00v/Dehashed/tree/master
- Crosslinked https://github.com/m8sec/CrossLinked
- Phonebook.cz subscription
  

# Setup 
Write all emails collected from phonebook.cz to `phonebook.txt` 
Update line 46 of gorillasint to include the absolute location of dehashed.py, and dehashed.py must have the API key hardcoded into the file. 

# Usage
```sh
python3 gorillasint.py -phonebook phonebook.txt -crosslinked "{first}.{last}@company.com" "Company Name from Linkedin" crosslinked_output -d company.com -whois -pymeta -amass -dehashed
```

# Credit
The big credit goes to those that made dehashed, crosslinked, and phonebook.cz. This is just a simple automation I've been looking for during externals.
