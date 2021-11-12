#Есть список строк, нужно удалить из него все пустые строки
a=['qweq', 'asd', ' ', '', '  a']

def DeleteApost(array):
    return str(a).replace(" ",'')

print(DeleteApost(a))
