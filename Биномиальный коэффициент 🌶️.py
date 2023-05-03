from math import factorial


def compute_binom(n, k):
    bin_coefficient = int(factorial(n) / (factorial(k) * factorial(n - k)))
    return bin_coefficient


def main():
    n = int(input())
    k = int(input())
    bin_coefficient_value = compute_binom(n, k)
    print(bin_coefficient_value)
