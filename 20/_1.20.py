#Найдите количество чисел, каждое из которых равно сумме квадратов своих соседей и
# при этом не является наибольшим в массиве.
array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))
count=0
def test():
    for i in range(1, n-1):
        if array[i]==(array[i-1]**2+array[i+1]**2) and array[i]!=max(array):
            count+=1
    print(count)
test()

