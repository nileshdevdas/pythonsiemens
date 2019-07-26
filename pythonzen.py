
import datetime;

def checkauth(*args, **kwargs):
    def inner(func):
        print("before......." , kwargs)
        # process your code
        return func;
    return inner;

@checkauth(a=10, b=20, c=30)
def myapp(a):
    print('1');
    print("2")

myapp(1);



x = lambda  a,b : print("hello")

x(1,2);