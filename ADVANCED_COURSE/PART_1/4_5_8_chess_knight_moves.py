CHESS_BOARD_SIZE = 8
CHESS_KNIGHT_POSITION_MARK = 'N'
FILLING_CHAR = '.'
POSSIBLE_MOVE_MARK = '*'
CHESS_KNIGHT_MOVE_RANGE = 2
# matrix = []
position = 'a1'
# position = input()
knight_x = ord(position[0]) - 97
knight_y = CHESS_BOARD_SIZE - int(position[-1])

matrix = [list(FILLING_CHAR * CHESS_BOARD_SIZE) for _ in range(CHESS_BOARD_SIZE)]
matrix[knight_y][knight_x] = CHESS_KNIGHT_POSITION_MARK

for i in range(CHESS_BOARD_SIZE):
    row = []
    for j in range(CHESS_BOARD_SIZE):
        if abs(knight_y - i) * abs(knight_x - j) == CHESS_KNIGHT_MOVE_RANGE:
            matrix[i][j] = POSSIBLE_MOVE_MARK

for row in matrix:
    print(*row)
