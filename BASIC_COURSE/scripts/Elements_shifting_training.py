sides_angles_list = [1, 2, 3]

# for i in range(len(sides_angles_list)):
#     side_angle = sides_angles_list[i]
#     other_sides_sum = sides_angles_list[i - 1] + sides_angles_list[i - 2]


for i in range(len(sides_angles_list) + 1):
    print(sides_angles_list)
    sides_angles_list[i - 1] = sides_angles_list[i + 1]
# sides_angles_list[0] = 0
