#Найдите сумму чисел массива, которые стоят на нечетных местах и при этом превосходят сумму крайних элементов массива.
array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

sum=0
def sumCheck(sum, array=[]):
    for i in range(n):
        if i%2!=0 and (array[i]>array[0]+array[n-1]):
             sum+=array[i]
    return sum

print("сумма чисел массива:",sumCheck(sum, array))

