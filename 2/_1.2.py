#Даны списки:
# a=[1,1,2,3,5,8,13,21,34,55,89];
#b=[1,2,3,4,5,6,7,8,9,10,11].
#Нужно вернуть списоок который состоит из элементовб общих для этих двух списков
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11]
c=[]
def MultiplyArrars(array1=[], array2=[]):
    for elem1 in array1:
        for elem2 in array2:
            if elem1==elem2:
                c.append(elem1)

def MulWithRepeat():
    MultiplyArrars(a, b)
    print("Объединение с повторением: ")
    print(list(c))
def MulWithoutRepeat():
    MultiplyArrars(a, b)
    print("Объединение без повторения: ")
    print(list(set(c)))

MulWithRepeat()

MulWithoutRepeat()