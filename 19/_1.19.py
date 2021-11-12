#Дан массив. Найдите три последовательных элемента в массиве, сумма которых максимальна.array=[]
array=[]
array1=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

def sumOf3():
    for i in range(n-2):
        array1.append(array[i]+array[i+1]+array[i+2])
    print(min(array1))
sumOf3()