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
for i, _ in enumerate(possible_move_list):
    move_y = knight_y + possible_move_list[i][0]
    move_x = knight_x + possible_move_list[i][1]
    if 0 <= move_x <= CHESS_BOARD_SIZE - 1 and 0 <= move_y <= CHESS_BOARD_SIZE - 1:
        matrix[move_y][move_x] = POSSIBLE_MOVE_MARK

for row in matrix:
    print(*row)



#
#
#
# # 1
# if knight_y + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
#         knight_x + 1 <= CHESS_BOARD_SIZE - 1:
#     matrix[knight_y + CHESS_KNIGHT_MOVE_RANGE][knight_x + 1] = POSSIBLE_MOVE_MARK
# # 2
# if knight_y + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
#         knight_x - 1 >= 0:
#     matrix[knight_y + CHESS_KNIGHT_MOVE_RANGE][knight_x - 1] = POSSIBLE_MOVE_MARK
# # 3
# if knight_y - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
#         knight_x + 1 <= CHESS_BOARD_SIZE - 1:
#     matrix[knight_y - CHESS_KNIGHT_MOVE_RANGE][knight_x + 1] = POSSIBLE_MOVE_MARK
# # 4
# if knight_y - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
#         knight_x - 1 >= 0:
#     matrix[knight_y - CHESS_KNIGHT_MOVE_RANGE][knight_x - 1] = POSSIBLE_MOVE_MARK
# # 5
# if knight_x + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
#         knight_y + 1 <= CHESS_BOARD_SIZE - 1:
#     matrix[knight_y + 1][knight_x + CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK
# # 6
# if knight_x + CHESS_KNIGHT_MOVE_RANGE <= CHESS_BOARD_SIZE - 1 and \
#         knight_y - 1 >= 0:
#     matrix[knight_y - 1][knight_x + CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK
# # 7
# if knight_x - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
#         knight_y + 1 >= 0:
#     matrix[knight_y + 1][knight_x - CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK
# # 8
# if knight_x - CHESS_KNIGHT_MOVE_RANGE >= 0 and \
#         knight_y - 1 >= 0:
#     matrix[knight_y - 1][knight_x - CHESS_KNIGHT_MOVE_RANGE] = POSSIBLE_MOVE_MARK
