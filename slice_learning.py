# print(len(password_num))
# print(password_num[:half_len])
# print(password_num[half_len + len(password_num) % 2:][::-1])
# # str = str[::-1]
password_num = '71'
half_len = len(password_num) // 2
value = True
for j in range(2, half_len + 2):
    if int(password_num) % j == 0:
        value = False
        break

print(value)
