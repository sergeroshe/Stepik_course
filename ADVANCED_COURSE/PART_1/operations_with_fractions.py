from fractions import Fraction
import operator

operator_lookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

OP_LIST = ['+', '-', '*', '/']
first_frac, sec_frac = [input() for _ in range(2)]
result_list = []
for op in OP_LIST:
    result = operator_lookup[op](Fraction(first_frac), Fraction(sec_frac))
    cur_op = f'{str(first_frac)} {op} {str(sec_frac)} = {Fraction(result)}'
    result_list.append(cur_op)
print(*result_list, sep='\n')