BASE = 15
HEIGHT = 8
FILL_SYM = ' '
OUT_TEMPLATE = '*'
BORDER_WIDTH = len(OUT_TEMPLATE)


def draw_triangle(half_base, fill_sym, border_width, out_template, height):
    for i in range(height):
        result_output = (fill_sym * border_width * (half_base - i) + out_template * ((i + 1) + i))
        print(result_output)


def main():
    half_base = BASE // 2
    draw_triangle(half_base, FILL_SYM, BORDER_WIDTH, OUT_TEMPLATE, HEIGHT)


main()