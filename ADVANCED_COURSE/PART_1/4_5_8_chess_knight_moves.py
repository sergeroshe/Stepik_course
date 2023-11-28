CHESS_BOARD_SIZE = 8
CHESS_KNIGHT_MOVE_RANGE = 2
STRAIGHT_MOVE = 2
TURN_MOVE = 1
A_ASCII_IDX = 97
CHESS_KNIGHT_POSITION_MARK = 'N'
FILLING_CHAR = '.'
POSSIBLE_MOVE_MARK = '*'
# position = 'f3'
position = input()

knight_x = ord(position[0]) - A_ASCII_IDX
knight_y = CHESS_BOARD_SIZE - int(position[-1])
matrix = [list(FILLING_CHAR * CHESS_BOARD_SIZE) for _ in range(CHESS_BOARD_SIZE)]
matrix[knight_y][knight_x] = CHESS_KNIGHT_POSITION_MARK

possible_move_list = [[STRAIGHT_MOVE, TURN_MOVE], [-STRAIGHT_MOVE, TURN_MOVE],
                      [STRAIGHT_MOVE, -TURN_MOVE], [-STRAIGHT_MOVE, -TURN_MOVE],
                      [TURN_MOVE, STRAIGHT_MOVE], [-TURN_MOVE, STRAIGHT_MOVE],
                      [TURN_MOVE, -STRAIGHT_MOVE], [-TURN_MOVE, -STRAIGHT_MOVE]]
for el in possible_move_list:
    move_y = knight_y + el[0]
    move_x = knight_x + el[1]
    if 0 <= move_x <= CHESS_BOARD_SIZE - 1 and 0 <= move_y <= CHESS_BOARD_SIZE - 1:
        matrix[move_y][move_x] = POSSIBLE_MOVE_MARK

for row in matrix:
    print(*row)
