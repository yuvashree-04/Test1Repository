import datetime
now=datetime.datetime.now() #used to get current date and time

year=(lambda x:x.year)
print(year(now))

month=(lambda x:x.month)
print(month(now))

day=(lambda x:x.day)
print(day(now))