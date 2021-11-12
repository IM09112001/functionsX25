#Найдите сумму нечетных чисел массива, которые не превосходят 11.
array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

def sumOfHalfElems(a=[],sum=0):
    for elem in a:
        if elem%2!=0 and elem<11:
            sum+=elem
    return sum
print("сумма нечетных чисел массива, которые не превосходят 11:",sumOfHalfElems(array))


