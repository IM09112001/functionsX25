#Создать массив, каждый элемент которого равен квадрату своего индекса
n=int(input("Введите количество элементов массива: "))
array=[]
def pow2(k, a=[]):
    for i in range(k):    
        a.append(i*i)
pow2(n, array)
for elem in array:
    print(elem)
