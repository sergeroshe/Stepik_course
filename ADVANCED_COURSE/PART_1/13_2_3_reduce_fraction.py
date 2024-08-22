from fractions import Fraction

numerator, denominator = [int(input()) for _ in range(2)]
# numerator, denominator = [3, 6]
reduced_fraction = Fraction(numerator, denominator)
is_dividing = True
i = 1
while is_dividing:
    if not numerator % i and not denominator % i:
        is_dividing = False
    numerator //= i
    denominator //= i
    i += 1
reduced_fraction = Fraction(numerator, denominator)
print(reduced_fraction)
