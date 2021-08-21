
string = "AAAAAAAAAAAAABBCCCCDD"

lista1 = []
[lista1.append(i) for i in string]
lista2 = []
for i in lista1:
    if i in lista2:
        continue
    else:
        lista2.append(i)
resultado =[]
lista3 =[]
def pasada(num1):
    num=0
    num2=0
    for i in lista1:
        if lista2[num1] == i:
            if num >= 9:
                num2+=1
            elif num<9:
                num+=1
    if num2>0:
        resultado.append(str(num)+str(lista2[num1])+str(num2)+str(lista2[num1]))
    else:
        resultado.append(str(num)+str(lista2[num1]))
    return resultado
for i in range(len(lista2)):
    lista3.append(pasada(i))
print("".join(map(str,lista3[-1])))


#Solución 2 
def runLengthEncoding(string):
    encodedStringCharacters = []
	currentRunLength = 1
	
	for i in range(1, len(string)):
		currentCharacter = string[i]
		previousCharacter = string[i - 1]
		
		if currentCharacter != previousCharacter or currentRunLength == 9:
			encodedStringCharacters.append(str(currentRunLength))
			encodedStringCharacters.append(previousCharacter)
			currentRunLength = 0
		
		currentRunLength +=1
	
	encodedStringCharacters.append(str(currentRunLength))
	encodedStringCharacters.append(string[len(string)-1])
	
	return "".join(encodedStringCharacters)
