import monkeypatch;

def monk(self):
    print("monkeypatch")


monkeypatch.A.func = monk
obj = monkeypatch.A();
obj.func()
