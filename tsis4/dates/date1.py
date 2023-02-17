#Write a Python program to subtract five days from current date.

from datetime import timedelta, datetime

currdate = datetime.now()
minfive = currdate - timedelta(days=5)

print("today", currdate.strftime("%Y-%m-%d"))
print("5 days ago", minfive.strftime("%Y-%m-%d"))