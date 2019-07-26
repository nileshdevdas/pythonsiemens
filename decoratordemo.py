
def calculate(func):
    def inner1(*arg, **kwargs):
        print("xxxxxxxxx")
        func();
        print("yyyyy")
    return inner1;

@calculate
def abc():
    print("abc")


abc();