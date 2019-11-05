import read_sheet

import random

def main():
    emails = read_sheet.email_dict() # Holds { name: emails }
    
    names = read_sheet.sheet_to_list() # Holds all names in a list
    random.shuffle(names) # Names are now in a shuffled order

    return 0
    


if __name__ == "__main__":
    # execute only if run as a script
    main()