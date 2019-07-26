import datetime;
import calendar;

today = datetime.datetime.now();
y= datetime.datetime(2015,1,1);
y1 = datetime.datetime(2017, 1,1);
cal1= calendar.calendar(2019)
print(cal1);
print(y.strftime("%x"));
print(y1 > y)


def a():
    return 10, 20


print(a())

x = lambda x , y : print("hello");



class B:
    pass;

v = B();
v.b = x;

v.b(1,2)