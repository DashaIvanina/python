#1
import re

def email_parse(email):
    try:
        USERNAME = re.compile((r'(^\w+)?[@]'))
        DOMAIN = re.compile(r'[a-z]+\.[a-z]+$')
        my_dict = {}
        my_dict['username'] = USERNAME.findall(email)[0]
        my_dict['doomain'] = DOMAIN.findall(email)[0]
        return my_dict
    except:
        raise ValueError

print(email_parse('dashachernyh1@gmail.com'))

#3
from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrap(*args):
        for arg in args:
            print(f'{func.__name__} ({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrap

@type_logger
def calc_cube(*args):
    return (list(map(lambda x: x ** 3, args)))

x = calc_cube(8, 9, 11)
print(x)
