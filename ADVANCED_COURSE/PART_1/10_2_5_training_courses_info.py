COURSE_DICT = {'CS101': '3004, Хайнс 8:00',
               'CM241': '1411, Ли, 13:00',
               'CS102': '4501, Альварадо, 9:00',
               'NT110': '1244, Берк, 11:00',
               'CS103': '6755, Рич, 10:00'
               }

course_id = input()

course_desc = ''

course_not_found = True

if course_id in COURSE_DICT:
    course_info = COURSE_DICT[course_id]
    course_desc = f'{course_id}: {course_info}'

print(course_desc)
