#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

current = datetime.now()
yesterday = current - timedelta(days=1)
tomorrow = current + timedelta(days=1)

print("yesterday", yesterday.strftime("%Y-%m-%d"))
print("current", current.strftime("%Y-%m-%d"))
print("tomorrow", tomorrow.strftime("%Y-%m-%d"))