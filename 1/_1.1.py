#есть список a=[1,1,2,3,5,13,21,34,55,89].
#Выведите все элементы, которые <5
a=[1,1,2,3,5,13,21,34,55,89]
def CheckForEquals(array=[]):
    for elem in a:
        if elem<5:
            print(elem)
CheckForEquals(a)
