CHESS_BOARD_SIZE = 8
CHESS_KNIGHT_POSITION_MARK = 'N'
FILLING_CHAR = '.'
POSSIBLE_MOVE_MARK = '*'
CHESS_KNIGHT_MOVE_RANGE = 2
# matrix = []
position = 'b6'
# position = input()
knight_x = ord(position[0]) - 97
knight_y = CHESS_BOARD_SIZE - int(position[-1])
print(knight_y, knight_x)

matrix = [list(FILLING_CHAR * CHESS_BOARD_SIZE) for _ in range(CHESS_BOARD_SIZE)]
matrix[knight_y][knight_x] = CHESS_KNIGHT_POSITION_MARK
# 1
if knight_y + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
        knight_x + 1 <= CHESS_BOARD_SIZE - 1:
    matrix[knight_y + CHESS_KNIGHT_MOVE_RANGE][knight_x + 1] = POSSIBLE_MOVE_MARK
# 2
if knight_y + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
        knight_x - 1 >= 0:
    matrix[knight_y + CHESS_KNIGHT_MOVE_RANGE][knight_x - 1] = POSSIBLE_MOVE_MARK
# 3
if knight_y - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
        knight_x + 1 <= CHESS_BOARD_SIZE - 1:
    matrix[knight_y - CHESS_KNIGHT_MOVE_RANGE][knight_x + 1] = POSSIBLE_MOVE_MARK
# 4
if knight_y - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
        knight_x - 1 >= 0:
    matrix[knight_y - CHESS_KNIGHT_MOVE_RANGE][knight_x - 1] = POSSIBLE_MOVE_MARK
# 5
if knight_x + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
        knight_y + 1 <= CHESS_BOARD_SIZE - 1:
    matrix[knight_y + 1][knight_x + CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK
# 6
if knight_x + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
        knight_y - 1 >= 0:
    matrix[knight_y - 1][knight_x + CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK
# 7
if knight_x - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
        knight_y + 1 >= 0:
    matrix[knight_y + 1][knight_x - CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK
# 8
if knight_x - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
        knight_y - 1 >= 0:
    matrix[knight_y - 1][knight_x - CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK


for row in matrix:
    print(*row)
