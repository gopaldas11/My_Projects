import smtplib
import datetime as dt
import random
MY_EMAIL = 'gopalloverkishor@gmail.com'
PASSWORD = 'kwoz abak tjby yqpf'
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quot_file:
        all_quotes = quot_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="gopaldas535251@gmail.com",
        msg=f"Subject: Hello! Today's Motivational Quote.\n\n{quote}")
