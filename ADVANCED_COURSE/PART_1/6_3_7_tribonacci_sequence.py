# seq_size = 10
seq_size = int(input())
cur_el, next_el, after_next_el = 1, 1, 1
seq = []
for _ in range(seq_size):
    seq.append(cur_el)
    cur_el, next_el, after_next_el = next_el, after_next_el, cur_el + next_el + after_next_el

print(*seq, sep=' ')
