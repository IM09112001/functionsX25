#Найдите сумму чисел массива, которые расположены до первого четного числа массива. 
#Если четных чисел в массиве нет, то найти сумму всех чисел за исключением крайних.
array=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))

def checkMod2(count):
    for elem in array:
        if elem%2==0: count+=1
    return count
#print(checkMod2(0))
def sumElem(start1, l, array=[]):
    sum=0
    for j in range(start1, l):
                sum+=array[j]
    return sum
#print(sumElem(0, n, array))
def goTo2(a=[]):
    a.reverse()
    for i in range(n):
        while a[i]%2==0:
              k=n-i-1
              break
    a.reverse()
    return k
#print(goTo2(array))
def checkPoint(a=[]):

    count=checkMod2(0)
    sum1=sumElem(1, n-1, a)
    
    
    if count==0:
        return sum1      
    else:
        k=goTo2(a)
        sum2=sumElem( 0, k, a)
        return sum2
        

    
print("сумма чисел массива:", checkPoint(array))



