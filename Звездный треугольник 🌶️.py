BASE = 15
HEIGHT = 8
FILL_SYM = ' '
OUT_TEMPLATE = '*'
BORDER_WIDTH = len(OUT_TEMPLATE)


def draw_triangle():
    half_base = BASE // 2
    for i in range(HEIGHT):
        print((FILL_SYM * BORDER_WIDTH * (half_base - i) + OUT_TEMPLATE * ((i + 1) + i)))


def main():
    draw_triangle()


main()