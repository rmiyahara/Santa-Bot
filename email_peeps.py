import smtplib
from email.message import EmailMessage

import consts

def send(send_to, sent_to_email, their_person):
    print(send_to + " got " + their_person) # For testing
    
    body = """\
    Dear %s,
    
    You are %s's Secret Santa this year. Get them something nice, or not, I'm not your mom.

    Love,
    HoHoHoItsRyan
    """ % (send_to, their_person)
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (consts.host_email, ", ".join(sent_to_email), consts.subject, body)
    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        s.login(consts.host_email, consts.host_password)
        s.sendmail(consts.host_email, sent_to_email, email_text)
        s.close()
    except:
        print("There was an error with the server")
        return 1

    return 0