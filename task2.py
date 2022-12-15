import itertools

print("Набор произведений чисел от 1 до N")
inp = input("Введите целое число N...\n")
try:
    n = int(inp)
    if n < 1:
        raise ValueError
    print(list(itertools.accumulate(range(1, n+1), lambda t, i: t*i)))
except:
    print("Введено неправильное число")
