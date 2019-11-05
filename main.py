import random

import read_sheet
import email_peeps

def main():
    emails = read_sheet.email_dict() # Holds { name: emails }
    
    names = read_sheet.sheet_to_list() # Holds all names in a list
    random.shuffle(names) # Names are now in a shuffled order

    for i in range(len(names)):
        if i == (len(names) - 1): # Case for last name
            email_peeps.send(names[i], names[0])
            return 0 # End here
        else: # The rest of them
            email_peeps.send(names[i], names[i + 1])
    
    return 1 # You shouldn't get here

    
if __name__ == "__main__":
    # execute only if run as a script
    main()