# how to declare a lambda



#x = lambda x, y : statements
# var = lambda param1,param2 : statement
def execute(x):
    print(globals())
    x = globals().get('v');

x = lambda p1 :  execute(p1);
# to invoke a lambda
x(1);
print(type(x));

class ABC:
    pass;
v = ABC();
v.myfn = x;
v.users = ['x','y', 'z'];
v.myfn(1);





