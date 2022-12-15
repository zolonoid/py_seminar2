import random
from pathlib import Path
from itertools import accumulate

# Перемешать список в случайном порядке
def MixList(srcList):
    dstList = []
    for i in range(len(srcList)):
        index = random.randint(0, len(srcList)-1)
        dstList.append(srcList.pop(index))
    return dstList

# Получить позиции из файла
def GetPositionsFromFile(file):
    lines = Path(file).read_text().split('\n')
    positions = list(int(x) for x in lines)
    return positions


N = 10

print("Произведение элементов списка, находящихся на указанных в файле позициях.")
print(f"Задан список из {N} элементов, заполненный числами из промежутка [-{N},{N}]:")
try:
    result = 1
    nums = MixList(list(range(-N, N+1)))[0:N]
    positions = GetPositionsFromFile("file4.txt")
    print(nums)
    for pos in positions:
        if pos < 0 or pos >= len(nums):
            continue
        result *= nums[pos]
    print(f"Произвдение элементов {positions} равно {result}")
except:
    print("Что-то пошло не так...")
