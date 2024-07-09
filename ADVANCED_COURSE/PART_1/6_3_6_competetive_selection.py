pupil_number = int(input())
pupil_list = [input().split() for _ in range(pupil_number)]

int_pupil_list = [(pupil[:-1], int(pupil[-1])) for pupil in pupil_list]

for pupil in pupil_list:
    print(*pupil)

print()

for pupil in int_pupil_list:
    if pupil[-1] > 3:
        print(*pupil[0], pupil[-1])