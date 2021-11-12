#Дан массив и число p. Найдите два различных числа в массиве, сумма которых наиболее близка к p
array=[]
array1=[]
array2=[]
p=int(input("Введите число: "))
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))
def testElems():
    sumMin()
    q=min(array1)+p
    for i in range(n):
        for j in range(n):       
            k=array[i]+array[j]
            if k==q: 
                array2.append({array[i], array[j]})
    print(array2)
    
def sumMin(): 
    for i in range(n):
        for j in range(n):       
            k=array[i]+array[j]-p
            if k<0: k*=-1
#            print(k)
            array1.append(k)
testElems() 







