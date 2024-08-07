ACCESS_DENIED_MESSAGE = 'Access denied'
ACCESS_PERMITTED_MESSAGE = 'OK'
ACCESS_CHAR_DICT = {'write': 'W', 'read': 'R', 'execute': 'X'}

file_amount = int(input())
file_description_list = [input() for _ in range(file_amount)]
file_description_dict = {file_name: permit for file_name, *permit in [file_description.split()
                                                                      for file_description in file_description_list]}
query_amount = int(input())
query_list = [input() for _ in range(query_amount)]

respond_list = []
for query in query_list:
    for command, name in [query.split()]:
        answer = ACCESS_PERMITTED_MESSAGE
        if ACCESS_CHAR_DICT[command] not in file_description_dict[name]:
            answer = ACCESS_DENIED_MESSAGE
        respond_list.append(answer)

print(*respond_list, sep='\n')