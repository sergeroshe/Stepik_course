BASE = 15
HEIGHT = 8
FILL_SYM = ' '
OUT_TEMPLATE = '@*@987'
BORDER_WIDTH = len(OUT_TEMPLATE)


def draw_triangle():
    half_base = BASE // 2
    for i in range(HEIGHT):
        print((FILL_SYM * (half_base * BORDER_WIDTH - i * BORDER_WIDTH)) + OUT_TEMPLATE * (i + 1) + OUT_TEMPLATE * i)


def main():
    draw_triangle()


main()