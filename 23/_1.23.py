#Найдите количество различных элементов данного массива.
from itertools import groupby
array=[]
array1=[]

n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))


def count():
    array.sort()
    array1=[el for el, _ in groupby(array)]
    k=0
    for elem in array1:
        k+=1
    print(k)
count()

















#Определите, есть ли в массиве повторяющиеся элементы.




#Определите, можно ли вычеркнуть из данного массива одно число так, 
#чтобы оставшиеся числа оказались упорядоченными по возрастанию.
