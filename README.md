# gorillasint
Gorillasint automates dehashed.py, crosslinked, and output from phonebook.cz into separate files that can be used for password spraying and other attacks.
# Setup 
Crosslinked and dehashed.py are required for gorillasint to work. Write all emails collected from phonebook.cz to `phonebook.txt` 
Update line 46 of gorillasint to include the absolute location of dehashed.py, and dehashed.py must have the API key hardcoded into the file. 

# Usage
```sh
python3 gorillasint.py -phonebook phonebook_output.txt -crosslinked "{first}.{last}@company.com" "Company Name" crosslinked_output.txt -dehashed company.com
```
