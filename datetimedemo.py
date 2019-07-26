import datetime;
import calendar;

date = datetime.datetime.now();
print(date);
print(date.year)
print(date.month)
print(date.day)
d1 = datetime.datetime(2015, 1, 1, 0, 0)
d2 = datetime.datetime(2017, 1, 1, 0, 0)
print(d2 > d1);

print(d1.strftime("%x %X"))
print(d1.strftime("%c"))

print(calendar.calendar(theyear=2019, w=2, l=1, c=6, m=1))