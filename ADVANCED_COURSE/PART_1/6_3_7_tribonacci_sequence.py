seq_size = int(input())
N_CCI = 3

len_seq = (1,) * N_CCI

for i in range(N_CCI, seq_size):
    len_seq += (sum(len_seq[i - N_CCI:i]), )

print(*len_seq[:seq_size])
