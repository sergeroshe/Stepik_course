lesson_amount = int(input())

general_attendance_list = []
all_lessons_presented_student_set = set()

for _ in range(lesson_amount):
    current_lesson_attendance_set = {input() for _ in range(int(input()))}
    general_attendance_list.append(current_lesson_attendance_set)
    # extra calc:
    all_lessons_presented_student_set = general_attendance_list[0]
    # extra calc:
    if general_attendance_list:
        all_lessons_presented_student_set &= current_lesson_attendance_set

print(*sorted(all_lessons_presented_student_set), sep='\n')

