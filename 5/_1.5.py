#Создать массив из n первых чисел Фибоначчи.
#(Тут у пользователя спрашивается сколько чисел Фибоначчи должно присутствовать в массиве,
# и далее циклом нужно вычислить каждый член этой последовательности и внести в список)
n=int(input("Введите количество числа фиб: "))
def Fib( k):
    f1=f2=1
    print(f1, f2, end=" ")
    for i in range(2,k):
        f1, f2=f2, f1+f2
        print(f2, end=" ")
Fib(n)
