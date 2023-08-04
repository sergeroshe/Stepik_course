# my version
army_list = list(range(1, int(input()) + 1))
count = int(input())

while len(army_list) != 1:
    for _ in range(count - 1):
        army_list.append(army_list.pop(army_list.index(army_list[0])))
    del army_list[0]

winner = army_list[0]

print(winner)

# the better but not my version

# army = int(input())
# victim_num = int(input())
#
# winner_idx = 0
# for i in range(1, army + 1):
#     winner_idx = (winner_idx + victim_num) % i
#
# winner = winner_idx + 1
#
# print(winner)