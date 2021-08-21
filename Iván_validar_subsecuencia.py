
array =    [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 25, 6, -1, 8, 10]

#Solución 1
num=0
lista = []
def isValidSubsequence(array, sequence):
    num=0
    for i in array:
        if i in sequence:
            num+=1
            lista.append(sequence.index(i))
    for i in lista:
        if lista[i] != lista[-1]:
            if lista[i]>lista[i+1]: 
                return False
    if num == len(sequence):
        return True
    else:
        return False
print(isValidSubsequence(array, sequence))


 #Solución 2
def isValidSubsequence(array, sequence):
    arrIdx=0
	seqIdx=0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx +=1
		arrIdx+=1
	return seqIdx == len(sequence)

