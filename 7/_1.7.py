#Создать массив, на четных местах в котором стоят единицы,
# а на нечетных местах - числа, равные остатку от деления своего номера на 5.
a=[]
k=int(input("Введите количество элементов: "))
def arithElem(n, array=[]):
    for i in range(n):
        if i%2==0:
            array.append(1)
        else: array.append(i%5)
arithElem(k, a)
for elem in a:
    print(elem)