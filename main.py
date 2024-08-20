##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_date = now.day
today_month = now.month
# print(today_date, today_month)

df = pd.read_csv("birthdays.csv")
# print(df["month"][0], df["day"][0])
# print(len(df))
birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in df.iterrows()}


if (today_month, today_date) in birthday_dict:
    birthday_person = birthday_dict[(today_month, today_date)]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    letter_number = random.randint(1,3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        # print(letter)
        original_letter = letter.read()
        # print(data)
        edited_letter = original_letter.format(name=birthday_person["name"])
        # print(type(data))
        # print(edited_letter)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user="concord.blast@gmail.com", password="acea ykib tigc eems")
            conn.sendmail(from_addr="concord.blast@gmail.com",
                          to_addrs=birthday_person["email"],
                          msg=f"subject: Happy Birthday!\n\n{edited_letter}")






