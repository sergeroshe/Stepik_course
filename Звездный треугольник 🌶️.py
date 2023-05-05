BASE = 15
HEIGHT = 8
FILL_SYM = ' '
OUT_TEMPLATE = '*'
BORDER_WIDTH = len(OUT_TEMPLATE)


def draw_triangle(base, fill_sym, border_width, out_template, height):
    half_base = base // 2
    for i in range(height):
        result_output = (fill_sym * border_width * (half_base - i) + out_template * (2 * i + 1))
        print(result_output)


def main():
    draw_triangle(BASE, FILL_SYM, BORDER_WIDTH, OUT_TEMPLATE, HEIGHT)


main()
