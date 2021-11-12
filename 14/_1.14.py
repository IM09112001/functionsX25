#Найдите сумму наибольшего и наименьшего элементов массива.
array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

def findMin(a=[]):return min(a)
def findMax(a=[]):return max(a)

print(findMin(array)+findMax(array))


