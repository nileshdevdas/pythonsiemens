import os;


print(os.path.curdir)
print(os.path.sep)
print(os.path.join("x", "c"))
print(os.path.exists("d:/inputData"))
x = os.listdir("d:/inputData")
print(x);
print(os.environ.get("APPDATA"))