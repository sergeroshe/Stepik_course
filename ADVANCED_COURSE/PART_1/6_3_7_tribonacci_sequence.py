seq_size = int(input())
cur_el, next_el, next_next_el = 1, 1, 1
seq = []
for _ in range(seq_size):
    print(cur_el, end=' ')
    cur_el, next_el, next_next_el = next_el, next_next_el, cur_el + next_el + next_next_el

