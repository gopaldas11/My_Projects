import smtplib
import pandas as pd
import random
import datetime as dt

MY_EMAIL = 'gopalloverkishor@gmail.com'
MY_PASSWORD = 'kwoz abak tjby yqpf'

today = dt.datetime.today()
today_tuple = (today.month, today.day)

data = pd.read_csv('birthdays.csv')

birthday_dict = {(data_row["month"], data_row["day"]): data_row
                 for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]

    letter_number = random.randint(1, 3)
    letter_path = f"letter_templates/letter_{letter_number}.txt"

    with open(letter_path) as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content.replace("[name]", name)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,
        msg=f"Subject: Happy Birthday!\n\n{letter_content}")

    print(f"🎉 Birthday email sent to {name} ({email}) using letter_{letter_number}.txt")
else:
    print("No birthdays today 😊")

