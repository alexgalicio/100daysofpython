import datetime as dt
import smtplib
import random

my_email = "jishooktt@gmail.com"
password = "uczafatyqaofqhza"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Motivational Quote\n\n{quote}")
