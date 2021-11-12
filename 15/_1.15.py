#Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.
array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

count=0
def countDiff(count, array=[]):
    for i in range(n):
        if array[i]<=(max(array)*0.1):
            count+=1

    print(count)
countDiff(count, array)

