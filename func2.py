def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner(func):
        print("Inside inner function")
        print("I like", kwargs['like'])
        return func

    return inner


@decorator(like="geeksforgeeks")
def func():
    print("Inside actual function")


func()