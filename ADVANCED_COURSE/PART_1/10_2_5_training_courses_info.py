COURSE_INFO_DICT = {'CS101': '3004, Хайнс 8:00',
                    'CM241': '1411, Ли, 13:00',
                    'CS102': '4501, Альварадо, 9:00',
                    'NT110': '1244, Берк, 11:00',
                    'CS103': '6755, Рич, 10:00'
                    }
course_info_len = len(COURSE_INFO_DICT)

course_id = input()


course_info = ''

course_not_found = True

if course_id in COURSE_INFO_DICT[course_id]:
        selected_dict = COURSE_INFO_DICT[i]
        course_info = f'{course_id}: {selected_dict[course_id]}'
        course_not_found = False
    i += 1

print(course_info)