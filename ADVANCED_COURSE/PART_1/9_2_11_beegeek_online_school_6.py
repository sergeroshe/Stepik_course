lesson_amount = int(input())

general_attendance_list = []
all_lessons_presented_student_list_set = set()

for _ in range(lesson_amount):
    current_lesson_attendance_list_set = {input() for _ in range(int(input()))}
    general_attendance_list.append(current_lesson_attendance_list_set)
    all_lessons_presented_student_list_set = general_attendance_list[0]
    if general_attendance_list:
        all_lessons_presented_student_list_set &= current_lesson_attendance_list_set

print(*sorted(all_lessons_presented_student_list_set), sep='\n')
