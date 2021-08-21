
string = input()
key = int(input())
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista1 =[]
def caesarCipherEncryptor(string, key):
    for i in string:
        if i in lista:
            if lista.index(i)+1+key > len(lista):
                x = (lista.index(i)+1+key) - len(lista)
                y = lista[x-1]
                lista1.append(y)
            else:
                lista1.append(lista[((lista.index(i))+key)])
    return "".join(map(str,lista1))
print(caesarCipherEncryptor(string, key))
