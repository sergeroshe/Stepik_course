def solve(a, b, c):
    from math import pow

    root_list = []

    dis = pow(b, 2) - 4 * a * c
    root_1 = (-b + dis ** 0.5) / (2 * a)
    root_2 = (-b - dis ** 0.5) / (2 * a)

    root_list.append(root_1)
    root_list.append(root_2)
    root_list.sort()

    return root_list


def main():
    a, b, c = int(input()), int(input()), int(input())
    root_1, root_2 = solve(a, b, c)
    print(root_1, root_2)


main()