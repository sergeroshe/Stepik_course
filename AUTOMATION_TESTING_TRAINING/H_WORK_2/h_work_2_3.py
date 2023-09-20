# # Task 3*. Напишите декоратор который выводит имя и список аргументов функции.

def my_decorator(func):
    def wrapper(*args) -> int:
        print(f'The name of called function is: "{func.__name__}"')
        print(f'The arguments of called function are: {[*args]}')
        return func(*args)

    return wrapper


@my_decorator
def get_quotient(x, y) -> float:
    return x / y


def main():
    dividend = int(input())
    divisor = int(input())

    quotient = get_quotient(dividend, divisor)

    print(f'The result of division is: {quotient}')


main()

