RESULT_STRING = '{rouble_cost} р. {copeck_cost} коп.'

input_string = input()
input_string_len = len(input_string)
rouble_cost = (input_string_len * 60) // 100
copeck_cost = (input_string_len * 60) % 100
result_message = RESULT_STRING.format(rouble_cost=rouble_cost, copeck_cost=copeck_cost)

print(result_message)



