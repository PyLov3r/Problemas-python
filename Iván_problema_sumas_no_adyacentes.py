array =  [1000, 2000, 20, 4001, 5000, 7000]


def maximaSuma(array):
    if not len(array):
        return 0
    elif len(array)==1:
        return array[0]
    suma = array[:]
    print("suma = ", suma)
    suma[1] = max(array[0], array[1])
    print("El máximo de", array[0],"y",array[1] ,"es",suma[1])
    print()
    for i in range(2, len(array)):
        suma[i] = max(suma[i-1], suma[i-2]+array[i])
        print("El máximo de ",suma[i-1],"y la suma de (",suma[i-2],"+",array[i],") que es "
        ,suma[i-2]+array[i],"es ",suma[i] )
    print(suma[-1])

maximaSuma(array)

