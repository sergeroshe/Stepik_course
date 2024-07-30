NOT_FOUND_MESSAGE = 'абонент не найден'

phone_contact_amount = int(input())

phone_contact_dict = {}
for _ in range(phone_contact_amount):
    phone_number, name = input().lower().split()
    phone_contact_dict.setdefault(name, []).append(phone_number)

request_amount = int(input())
request_name_list = [input().lower() for _ in range(request_amount)]

request_result_list = []

for name in request_name_list:
    request_result_list.append(phone_contact_dict.get(name, [NOT_FOUND_MESSAGE]))

for request_result in request_result_list:
    print(*request_result)