from datetime import datetime
import random
import smtplib
import pandas

email = "jishooktt@gmail.com"
password = "uczafatyqaofqhza"

today = datetime.now()
month_day = (today.month, today.day)

data = pandas.read_csv("birthday.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if month_day in birthday_dict:
    birthday_person = birthday_dict[month_day]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as lt:
        contents = lt.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
