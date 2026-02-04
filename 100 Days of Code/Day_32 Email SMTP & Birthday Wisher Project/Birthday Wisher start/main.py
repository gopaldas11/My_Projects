
# Trying to send email using python. Basics .

import smtplib

my_email = "gopalloverkishor@gmail.com"
password = "kwoz abak tjby yqpf"

with smtplib.SMTP("smtp.gmail.com") as server:
    server.starttls()
    server.login(user=my_email,password=password)
    server.sendmail(from_addr=my_email,to_addrs="gopaldas535251@gmail.com",
                    msg="Subject: Hello\n\nIs this SMTP Email Working?")
