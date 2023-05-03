from math import factorial

def compute_binom(n, k):
    bin_cf_val = int(factorial(n) / (factorial(k) * factorial(n - k)))
    return bin_cf_val
# считываем данные


n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))