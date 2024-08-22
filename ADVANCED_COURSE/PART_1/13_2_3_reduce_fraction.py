from fractions import Fraction

numerator, denominator = [int(input()) for _ in range(2)]
reduced_fraction = Fraction(numerator, denominator)

print(reduced_fraction)