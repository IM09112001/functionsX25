#Определите, есть ли в массиве повторяющиеся элементы.
from itertools import groupby
array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))
def test():
    array.sort()
    array1=[el for el, _ in groupby(array)]
    k=len(array)-len(array1)
    if k!=0:
        print("В массиве есть повторяющиеся элементы")
    else: print("В массиве нет повторяющихся элементов")
test()






















#Определите, можно ли вычеркнуть из данного массива одно число так, 
#чтобы оставшиеся числа оказались упорядоченными по возрастанию.

