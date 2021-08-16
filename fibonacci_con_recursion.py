

num = int(input())

global a1
a1 = []

def fibonacci(num):
  a = 0
  a1.append(a)
  b= 1
  a1.append(b)
  c= a + b
  a1.append(c)

  for i in range(num):
      a = c + b
      a1.append(a)
      b = a + c
      a1.append(b)
      c = b + a
      a1.append(c)
      
  #print(a1)
  count = 0
  for i in a1:
    if i == num:
      break
    else:
      if count == num:
        break
      else:
        print(a1[count])  #Estaopción es para sacar toda la lista de números
        count = count + 1
  print(a1[num-1])
  


fibonacci(num)

#Con recursión

def getNthFib(n):
    if n == 2:
      return 1
    elif n == 1:
      return 0
    else: 
      return getNthFib(n-1) + getNthFib(n-2)











    
