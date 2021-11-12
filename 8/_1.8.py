#Найти количество четных чисел в массиве.
q=[]
def printArray(array=[]):
    n=int(input("Введите количество элементов: "))
    print("Введите элементы массивов:")
    for i in input().split():
        array.append(int(i))
def count(a=[]):
    count=0
    for elem in a:
        if elem%2==0: count+=1
    return count
printArray(q)
print("количество четных чисел в массиве:",count(q))