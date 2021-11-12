#Дан массив. Найдите два соседних элемента, сумма которых минимальна.
array=[]
array1=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

def sum2Min():
    for i in range(n-1):
        array1.append(array[i]+array[i+1])
    print(min(array1))
sum2Min()

