#Сформировать возрастающий массив из четных чисел от 100 до 150
a=[]
leftSide=int(input("Введите левую часть: "))
rightSide=int(input("Введите правую часть: "))
def IncreaseElem(array=[], start=0, end=0):
    for elem in range(start, end, 2):   
        array.append(elem)
    print(array)
IncreaseElem(array=a, start=leftSide, end=rightSide)