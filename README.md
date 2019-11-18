# Secret Santa Bot
Secret Santa is a gift giving activity where a group of people are assigned one other person in the group. On a certain date, they present their randomly chosen person with their gift.

This bot utilizes Python and its email package to read the contents of an Excel sheet (made from a roster) and anonymously email each person their assignment.

This bot was originally made for UCLA's Kyodo Taiko as they run a Secret Santa every year, but feel free to use this with your own friends.

# Running the Bot
Make sure your files are correctly configured. If you are unsure what to change, refer to the "Files" section of the readme.

To run the bot, make sure you have Pip3 and Python3 installed on your matchine. Then run the following.
> pip3 install xlrd

> pip3 install smtplib

> python3 main.py


# Files
### main.py
This is the file which contains your "main" function. There isn't much in there, but you will call this script to run the bot.

### config.py
Holds all the configuration values. If you change a file, this one will be it. The first few values effect the input while the ones at the end effect the email parameters. I have added comments to specify which is which.

### read_sheet.py
Contains all the logic to read in the input sheet. The only function in there returns a tuple which include a list of the people from the input as well as a dictionary which maps names to emails.

### email_peeps.py
Contains all the logic to email a person their assignment. Feel free to change the email_text variable as that one is what gets sent to everyone.