import random
import getpass

import read_sheet
import email_peeps
import config

def main():
    names, emails  = read_sheet.sheet_to_list() # Holds all names in a list
    random.shuffle(names) # Names are now in a shuffled order

    try:
        pass_prompt = "Password for {}: ".format(config.host_email)
        host_password = getpass.getpass(prompt=pass_prompt)
    except Exception as error: 
        print('ERROR', error)

    for i in range(len(names)):
        if i == (len(names) - 1): # Case for last name
            email_peeps.send(names[i], emails[names[i]], names[0], host_password)
            return 0 # End here
        else: # The rest of them
            email_peeps.send(names[i], emails[names[i]], names[i + 1], host_password)
    
    return 1 # You shouldn't get here

    
if __name__ == "__main__":
    # execute only if run as a script
    main()