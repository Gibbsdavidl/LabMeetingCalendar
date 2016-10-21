#!/usr/local/bin/python

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import time
import datetime 

import calendar


def sendEmail():
    print('Sending Email!')
    for ei in emails:
        eisp = ei.split(",")
        print(eisp) 
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(msgfile, 'rb')
        # Create a text/plain message
        msg = MIMEText(fp.read())
        fp.close()
        msg['Subject'] = 'Lab Meeting Update (Thurs 2pm)'
        msg['From'] = "dgibbs@systemsbiology.org"
        msg['To'] = eisp[1]
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        #s = smtplib.SMTP('smtp.gmail.com',587)
        #s.ehlo()
        #s.starttls()
        #s.login('drdavidgibbs@gmail.com', mypass)
        #s.sendmail('dgibbs@systemsbiology.org', 'gibbsdavidl@gmail.com', msg.as_string())
        #s.close()
    return(0)


def sendUpdateEmail(day):
    print('Sending Update Email!')
    msg = MIMEText("Email System Still Alive on day: " + day)
    msg['Subject'] = 'System Alive: Lab Meeting Update (Thurs 2pm)'
    msg['From'] = 'drdavidlgibbs@gmail.com'
    msg['To'] = 'gibbsdavidl@gmail.com'
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login('drdavidlgibbs@gmail.com', mypass)
    s.sendmail('drdavidgibbs@gmail.com', 'gibbsdavidl@gmail.com', msg.as_string())
    s.close()
    return(0)


# Message Contents
msgfile = "msgs/system_intro.txt"

# Email List
emails = open("dat/emailList.txt",'r').read().strip().split("\n")

# Only email once on thursdays.
wednesdayFlag = 0

# send a startup email.
sendUpdateEmail('startup')

# main loop
while 1==1:
    # sleep a while
    time.sleep(480)

    # now wake up, what time is it?
    now = datetime.datetime.now() 
    day = now.strftime("%A")  # the name of the day
    m = now.timetuple()[1]    # the month number
    d = now.timetuple()[2]    # the day number
    
    if day == 'Wednesday' and wednesdayFlag == 0:
        print('time to email!')
        thursdayFlag = 1
        # email the next four individuals on the master list
        # email the lab 

    elif day == 'Wednesday' and wednesdayFlag == 1:
        # it's still thursday but we already emailed.
        print('going to wait, it is still thursday')

    else:
        # then it's not thursday, 
        # reset the flag and go back to sleep
        wednesdayFlag = 0
        print('it is ' + day + '... going back to sleep\n')
        # popoff the last talk from the calendar list.

    sendUpdateEmail(day)
