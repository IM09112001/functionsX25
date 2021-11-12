#Определите, можно ли вычеркнуть из данного массива одно число так, 
#чтобы оставшиеся числа оказались упорядоченными по возрастанию.

array=[]

n=int(input("Введите количество элементов: "))
print("Введите элементы массивов:")
for i in input().split():
    array.append(int(i))
check1=True
check2=False
def quantity(i, k=1): return array[i]>array[i+k]
for i in range(len(array)-2):
    if quantity(i):
        if check2 or quantity(i, 2):
            check1=False
            break
        else: check2=True
if check1==True:
    print('Да')
else: print('Нет')


