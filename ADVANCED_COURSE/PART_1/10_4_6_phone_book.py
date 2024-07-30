NOT_FOUND_MESSAGE = 'абонент не найден'

# phone_contact_amount = int(input())
phone_contact_amount = 3

# phone_contact_dict = {phone_number: name for _ in range(phone_contact_amount)
#                       for phone_number, name in [input().lower().split()]}

phone_contact_dict = {'79184219577': 'женя', '79194249271': 'руслан', '79281234567': 'женя'}
# request_amount = int(input())
request_amount = 3

# request_name_list = [input().lower() for _ in range(request_amount)]
request_name_list = ['Руслан'.lower(), 'женя'.lower(), 'Рустам'.lower()]
request_result_dict = {}
request_result_list = []
request_result_name_list = []

for request_name in request_name_list:
    if request_name in phone_contact_dict.values():
        current_contact_phone_number = ''
        for phone_number, name in phone_contact_dict.items():
            if request_name == name:
                current_contact_phone_number += phone_number + ' '
                request_result_dict[request_name] = current_contact_phone_number
    else:
        request_result_dict[request_name] = NOT_FOUND_MESSAGE
    request_result_list.append(request_result_dict[request_name])

print(*request_result_list, sep='\n')

