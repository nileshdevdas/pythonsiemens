

a = [1,2,3,4,5,6]
x = iter(a)
done = object();
# nx = next(x,done);
# while(nx  is not done):
#     print(nx);
#     nx = next(x,done);
for elem in x:
    print(elem)
