import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper
@start_end_decorator
def add6(Kansas_City_Chiefs):
    return Kansas_City_Chiefs + 6
#print_name = start_end_decorator(print_name)
result = add6(0)
print(result)
def adduser(x):
    return x+1
print(help(adduser))
print(add6.__name__)
