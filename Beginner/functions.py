def hello_func():
    pass


print(hello_func)
print(hello_func())


def hi_func(greeting):
    return "{} function".format(greeting)


print(hi_func('Hi'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', name='John')


def is_leap(year):
    """Return True for leap years, False for non-leap years. """
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

