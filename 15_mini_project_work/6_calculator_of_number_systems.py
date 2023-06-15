from math import sqrt

total = 88
APPLE_TREE = 32
PEAR_TREE = 22
PLUM_TREE = 16
CHERRY_TREE = 17


def number_sys_calc():
    tree_list = [APPLE_TREE, PEAR_TREE, PLUM_TREE, CHERRY_TREE]
    n_list = []

    for tree in tree_list:
        for dig in str(tree)[::-1]:
            n = sqrt(int(dig)) / tree
            n_list.append(n)

    return n_list


def main():
    n = number_sys_calc()
    print(n)


main()
