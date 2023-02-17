#Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

curr = datetime.now()
tmrw = curr + timedelta(days=1)

diff = (curr - tmrw).total_seconds()
print(diff)