CHESS_BOARD_SIZE = 8
STRAIGHT_MOVE = 2
TURN_MOVE = 1
X_COORD_SHIFT = ord('a')
CHESS_KNIGHT_POSITION_MARK = 'N'
FILLING_CHAR = '.'
POSSIBLE_MOVE_MARK = '*'

position = input()

knight_x = ord(position[0]) - X_COORD_SHIFT
knight_y = CHESS_BOARD_SIZE - int(position[-1])
matrix = [list(FILLING_CHAR * CHESS_BOARD_SIZE) for _ in range(CHESS_BOARD_SIZE)]
matrix[knight_y][knight_x] = CHESS_KNIGHT_POSITION_MARK

shift_list = [[STRAIGHT_MOVE, TURN_MOVE], [-STRAIGHT_MOVE, TURN_MOVE],
              [STRAIGHT_MOVE, -TURN_MOVE], [-STRAIGHT_MOVE, -TURN_MOVE],
              [TURN_MOVE, STRAIGHT_MOVE], [-TURN_MOVE, STRAIGHT_MOVE],
              [TURN_MOVE, -STRAIGHT_MOVE], [-TURN_MOVE, -STRAIGHT_MOVE]]
for shift in shift_list:
    move_y = knight_y + shift[0]
    move_x = knight_x + shift[1]
    if 0 <= move_x <= CHESS_BOARD_SIZE - 1 and 0 <= move_y <= CHESS_BOARD_SIZE - 1:
        matrix[move_y][move_x] = POSSIBLE_MOVE_MARK

for row in matrix:
    print(*row)
