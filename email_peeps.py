import smtplib
import email

import consts

def send(send_to, sent_to_email, their_person):
    print(send_to + " got " + their_person) # For testing

    email_text = """\
From: %s
To: %s
Subject: %s
Dear %s,
    
You are %s's Secret Santa this year. Get them something nice, or not, I'm not your mom.

Love,
HoHoHoItsRyan
    """ % (consts.host_email, sent_to_email, consts.subject, send_to, their_person)
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
    except:
        print("There was an error connecting to the server.")
        return 1
    try:
        server.login(consts.host_email, consts.host_password)
    except:
        print("There was an error authenticating.")
        return 1
    try:
        server.sendmail(consts.host_email, sent_to_email, email_text)
    except:
        print("There was an error sending the email.")
        return 1

    server.quit()
    return 0