#Найти количество чисел в массиве, которые делятся на 3, но не делятся на 7.


array=[]

n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

#printArray(array)

def Check(a=[]):
    count=0
    for elem in array:
        if elem%3==0 and elem%7!=0: count+=1
    return count

print("количество чисел в массиве, которые делятся на 3, но не делятся на 7:",Check(array))
