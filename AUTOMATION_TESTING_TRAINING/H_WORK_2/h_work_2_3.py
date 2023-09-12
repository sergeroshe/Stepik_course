# Task 3*. Напишите декоратор который выводит имя и список аргументов функции.


def my_decorator(func):
    def wrapper(y, x):
        print(func.__name__)
        func(y, x)
        print(y, x)
        return func(y, x)
    return wrapper


@my_decorator
def get_quotient(x, y):
    return x / y


decorated_func = my_decorator(get_quotient)
print(decorated_func(9, 3))
# print(get_odd_num_dict(9, 3))
