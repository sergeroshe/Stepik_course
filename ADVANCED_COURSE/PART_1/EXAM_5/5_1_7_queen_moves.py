CHESS_BOARD_SIZE = 8
X_COORD_SHIFT = ord('a')

MOVE = 1
STAY = 0
QUEEN_POSITION_MARK = 'Q'
FILLING_CHAR = '.'
POSSIBLE_MOVE_MARK = '*'
MTRX_COL_WIDTH = 3


def mtrx_fill(mtrx_size, filling_char):
    mtrx = [list(filling_char * mtrx_size) for _ in range(CHESS_BOARD_SIZE)]
    return mtrx


def queen_moves(y, x, mtrx):

    for i in range(CHESS_BOARD_SIZE):
        mtrx[y][i] = POSSIBLE_MOVE_MARK
        mtrx[i][x] = POSSIBLE_MOVE_MARK

    i = 0
    y_move = y + i
    x_move = x + i
    while 0 <= y_move <= CHESS_BOARD_SIZE - 1\
            and 0 <= x_move <= CHESS_BOARD_SIZE - 1:
        mtrx[y_move][x_move] = POSSIBLE_MOVE_MARK
        y_move += 1
        x_move += 1

    y_move = y + i
    x_move = x + i
    while 0 <= y_move <= CHESS_BOARD_SIZE - 1\
            and 0 <= x_move <= CHESS_BOARD_SIZE - 1:
        mtrx[y_move][x_move] = POSSIBLE_MOVE_MARK
        y_move -= 1
        x_move -= 1
    y_move = y + i
    x_move = x + i
    while 0 <= y_move <= CHESS_BOARD_SIZE - 1\
            and 0 <= x_move <= CHESS_BOARD_SIZE - 1:
        mtrx[y_move][x_move] = POSSIBLE_MOVE_MARK
        y_move += 1
        x_move -= 1

    y_move = y + i
    x_move = x + i
    while 0 <= y_move <= CHESS_BOARD_SIZE - 1\
            and 0 <= x_move <= CHESS_BOARD_SIZE - 1:
        mtrx[y_move][x_move] = POSSIBLE_MOVE_MARK
        y_move -= 1
        x_move += 1


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end='')
        print()


def main():
    matrix = mtrx_fill(CHESS_BOARD_SIZE, FILLING_CHAR)

    position = 'f5'
    # position = input()
    queen_x = ord(position[0]) - X_COORD_SHIFT
    queen_y = CHESS_BOARD_SIZE - int(position[-1])
    queen_moves(queen_y, queen_x, matrix)

    matrix[queen_y][queen_x] = QUEEN_POSITION_MARK

    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
