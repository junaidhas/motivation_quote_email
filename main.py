import datetime as dt
import smtplib
#smtplib (simple mail transfer protocol) library
import random

EMAIL = "learnerpython97@gmail.com"
PASSWORD = "password"
# Need to use APP password instead to login to avoid SMTP authentication error 

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5 :
  #weekday are integers 0 to 6 for monday to sunday, monday is 0, tuesday is 1,... friday is 4 
    with open("quotes.txt") as quotes_file:
      #openng quotes.txt file and readlines() to read each line and create a list.
        quotes_list = quotes_file.readlines()
        #list of motvational quotes
        quote = random.choice(quotes_list)

    print(quote)  

    with smtplib.SMTP("smtp.gmail.com") as connection:
      #setting up SMTP connection, "smtp.gmail.com" is common SMTP server address for all google accounts
        connection.starttls()
        # start tls protocol (Transport layer security)
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"subject: Motivation quote \n\n{quote}"
            #\n\n to seperate subject and contents
        )

    #when using for the first time you will get smtplib.SMTPAuthenticationError
    # to avoid it activate two step verifaction in the google account
    # then search for APP password in the search bar, select other app --> then copy the pwd and paste in place of the password here
