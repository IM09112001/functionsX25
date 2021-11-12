#Среди элементов с нечетными индексами найдите наибольший элемент массива, который делится на 3.

array=[]
array1=[]
n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))
def mod3(a=[], a1=[]): 
    for i in range(n):
        if a[i]%3==0 and i%2==1:
           a1.append(a[i])
           
    print(max(a1))
mod3(array, array1)


