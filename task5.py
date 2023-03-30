# number = int(input('Введите любое целое число меньше 100 000: '))
# for i in range(2, number):
#     sum_del_i = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum_del_i += j
#     for m in range(2, i):
#         sum_del_m = 0
#         for a in range(1, m):
#             if m % a == 0:
#                 sum_del_m += a
#         if sum_del_i == m and sum_del_m == i and i != m:
#             print(i, m)


######################################################################

def sumDividers(n):
    return sum(x for x in range(1, n // 2 + 1) if not n % x)

number = int(input('input k: '))

for i in range(1, number + 1):
    friendlyDigits = sumDividers(i)
    if i < friendlyDigits and i == sumDividers(friendlyDigits):
        print(i, friendlyDigits)