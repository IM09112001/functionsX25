#Найдите сумму и произведение элементов массива.

array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

def sumOfElem(a=[]):
    sum=0
    for elem in array:
        sum+=elem
    print("сумма элементов массива:",sum)

def compare(a=[]):
    comp=1
    for elem in array:
        comp*=elem
    print("произведение элементов массива:",comp)
print(compare(array))
print(sumOfElem(array))
