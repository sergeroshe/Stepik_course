BASE = 15
HEIGHT = 8
FILL_SYM = ' '
OUT_TEMPLATE = '*'
BORDER_WIDTH = len(OUT_TEMPLATE)


def draw_triangle(half_base):
    for i in range(HEIGHT):
        result_output = (FILL_SYM * BORDER_WIDTH * (half_base - i) + OUT_TEMPLATE * ((i + 1) + i))
        print(result_output)


def main():
    half_base = BASE // 2
    draw_triangle(half_base)


main()