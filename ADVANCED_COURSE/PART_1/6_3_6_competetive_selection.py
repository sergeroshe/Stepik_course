pupil_number = int(input())
pupil_list = [tuple(input().split()) for _ in range(pupil_number)]
# pupil_number = 3
# pupil_list = ['Гуев 3', 'Чаниев 5', 'Барсуков 2']
for pupil in pupil_list:
    print(*pupil)

print()

for pupil in pupil_list:
    if int(pupil[-1]) > 3:
        print(*pupil)
