CHESS_BOARD_SIZE = 8
X_COORD_SHIFT = ord('a')
QUEEN_POSITION_MARK = 'Q'
FILLING_CHAR = '.'
POSSIBLE_MOVE_MARK = '*'
MTRX_COL_WIDTH = 3


def mtrx_fill(mtrx_size, filling_char):
    mtrx = [list(filling_char * mtrx_size) for _ in range(CHESS_BOARD_SIZE)]
    return mtrx


def queen_hor_move(mtrx, y, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        mtrx[y][i] = filling_char


def queen_vert_move(mtrx, x, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        mtrx[i][x] = filling_char


def queen_main_diag(mtrx, queen_x, queen_y, filling_char):
    mtrx_size = len(mtrx)
    diag_start_y = (queen_y - queen_x) if queen_y - queen_x >= 0 else 0
    diag_start_x = (queen_x - queen_y) if queen_x - queen_y >= 0 else 0
    mtrx[diag_start_y][diag_start_x] = filling_char

    move_range = (queen_y - diag_start_y) + (mtrx_size - 1 - queen_y)\
        if diag_start_x == 0\
        else (queen_y - diag_start_y) + mtrx_size - 1 - queen_x

    j = diag_start_x + 1
    for i in range(diag_start_y + 1, diag_start_y + move_range + 1):
        mtrx[i][j] = filling_char
        j += 1


def queen_sec_diag(mtrx, queen_x, queen_y, filling_char):
    mtrx_size = len(mtrx)
    diag_start_x = queen_x + queen_y if queen_x + queen_y <= mtrx_size - 1\
        else mtrx_size - 1
    diag_start_y = 0 if queen_x + queen_y < mtrx_size\
        else queen_y - (mtrx_size - 1 - queen_x)
    move_range = (queen_y - diag_start_y) + (mtrx_size - 1 - queen_y)\
        if diag_start_x == mtrx_size - 1 \
        else (queen_y - diag_start_y) + queen_x

    mtrx[diag_start_y][diag_start_x] = filling_char

    j = diag_start_x - 1
    for i in range(diag_start_y + 1, diag_start_y + move_range + 1):
        mtrx[i][j] = filling_char
        j -= 1


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end='')
        print()


def main():
    mtrx = mtrx_fill(CHESS_BOARD_SIZE, FILLING_CHAR)

    # position = 'd5'
    position = input()

    queen_x = ord(position[0]) - X_COORD_SHIFT
    queen_y = CHESS_BOARD_SIZE - int(position[-1])

    queen_hor_move(mtrx, queen_y, POSSIBLE_MOVE_MARK)
    queen_vert_move(mtrx, queen_x, POSSIBLE_MOVE_MARK)
    queen_main_diag(mtrx, queen_x, queen_y, POSSIBLE_MOVE_MARK)
    queen_sec_diag(mtrx, queen_x, queen_y, POSSIBLE_MOVE_MARK)
    mtrx[queen_y][queen_x] = QUEEN_POSITION_MARK

    mtrx_print(mtrx, MTRX_COL_WIDTH)


main()
