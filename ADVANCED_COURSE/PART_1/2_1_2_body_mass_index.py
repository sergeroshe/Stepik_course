OPTIMAL_WEIGHT = 'Оптимальная масса'
UNDERWEIGHT = 'Недостаточная масса'
OVERWEIGHT = 'Избыточная масса'

weight = float(input())
height = float(input())
body_mass_idx = weight / (height ** 2)
body_mass = OVERWEIGHT

if 18.5 <= body_mass_idx <= 25:
    body_mass = OPTIMAL_WEIGHT
elif body_mass_idx < 18.5:
    body_mass = UNDERWEIGHT


print(body_mass)