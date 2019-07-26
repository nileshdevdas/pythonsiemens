a = 10;
b = 20;

def printdata():
    print(globals());
    abc = 20 ;
    print(locals())
    def p2():
        print("########### p2 ##################")
        a1 = 10;
        print(locals())
        print(globals())
    p2();

printdata();
print("#######################")
locals();

print(globals().get('a'))