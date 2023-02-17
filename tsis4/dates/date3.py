#Write a Python program to drop microseconds from datetime.

from datetime import datetime, timedelta

curr = datetime.now()
curr = curr.replace(microsecond=0)

print(curr)