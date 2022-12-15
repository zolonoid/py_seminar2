# Получить сумму цифр в числе
def GetNumSum(val):
    sum = 0
    for num in str(val):
        if num in "0123456789":
            sum += int(num)
    return sum


print("Нахождение суммы цифр в числе.")
inp = input("Введите число...\n").replace(',', '.')
try:
    value = float(inp)
    print("В числе {0} сумма всех цифр {1}".format(value, GetNumSum(value)))
except:
    print("Это не число")
