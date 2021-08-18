#Lograr que una función cheque si un String es Palindrome (se escriba igual normal o de reversa)

#Solución 1

string = input()
lista = []
lista1 = []
def isPalindrome(string):
    num = 1
    while num <= len(string):
        lista.append(string[-(num)])
        lista1.append(string[num-1])
        num += 1     
    if lista == lista1:
        return True
    else:
        return False
print(isPalindrome(string))

#Solución 2

def isPalindrome(string):
    reversedString = ""
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string == reversedString