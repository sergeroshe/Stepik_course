# Определение принадлежности точки кругу с центром в начале координат
# Вводятся координаты (x;y) точки и радиус круга (r).
# Определить принадлежит ли данная точка кругу, если его центр находится в начале координат.

Y_ANSWER = 'Точка принадлежит окружности данного радиуса'
N_ANSWER = 'Точка не принадлежит окружности данного радиуса'
X_COORDINATE_PROMPT = 'Введите число - координату "x" для заданной точки:\n'
Y_COORDINATE_PROMPT = 'Введите число - координату "y" для заданной точки:\n'
RADIUS_PROMPT = 'Введите число - радиус окружности:\n'


def does_point_belong_to_circle(x, y, r):
    result = (x ** 2 + y ** 2) < r ** 2
    return result


def main():
    x_coordinate, y_cordinate, radius = float(input(X_COORDINATE_PROMPT)),\
                                        float(input(Y_COORDINATE_PROMPT)),\
                                        float(input(RADIUS_PROMPT))
    answer = N_ANSWER
    if does_point_belong_to_circle(x_coordinate, y_cordinate, radius):
        answer = Y_ANSWER
    print(answer)


main()
