seq_size = 10
cur_el, next_el, after_next_el = 1, 1, 1
for i in range(seq_size):
    print(cur_el)
    cur_el, next_el, after_next_el = next_el, after_next_el, cur_el + next_el + after_next_el
