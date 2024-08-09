from random import randint

ticket_set = set()

while len(ticket_set) < 101:
    cur_ticket = []
    for j in range(7):
        cur_ticket.append(str(randint(1, 9)))
    ticket_set.add(''.join(cur_ticket))

print(*ticket_set, sep='\n')