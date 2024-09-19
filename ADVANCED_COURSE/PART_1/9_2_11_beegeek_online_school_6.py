lesson_amount = int(input())

all_lessons_presented_student_set = {input() for _ in range(int(input()))}

for _ in range(lesson_amount - 1):
    current_lesson_attendance_set = {input() for _ in range(int(input()))}
    all_lessons_presented_student_set &= current_lesson_attendance_set

print(*sorted(all_lessons_presented_student_set), sep='\n')