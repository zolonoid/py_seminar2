from functools import reduce
from operator import add

print("Сумма чисел списка из n элементов последовательности (1 + 1/n)**n")
inp = input("Введите целое число n...\n")
try:
    n = int(inp)
    if n < 1:
        raise ValueError
    nums = [round((1+1/x)**x, 2) for x in range(1, n+1)]
    print(f"Задан список чисел: {nums}")
    sum = reduce(add, nums)
    print(f"Сумма равна {sum:.2f}")
except:
    print("Введено неправильное число")
