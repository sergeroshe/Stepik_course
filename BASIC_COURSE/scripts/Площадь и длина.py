from math import pi


def get_circle(radius):
    circle_length = 2 * pi * radius
    circle_area = pi * (radius ** 2)

    return circle_length, circle_area


def main():
    r = float(input())

    length, square = get_circle(r)

    print(length, square)


main()
