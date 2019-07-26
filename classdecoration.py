class mydecorator(object):
    def __init__(self, *func, **kwargs):
        print("inside init")
        #func();

    def __call__(self, func):
        print("inside call")
        return func;
@mydecorator(arg=1)
def myfunction():
    print("inside aFunction()")

myfunction()