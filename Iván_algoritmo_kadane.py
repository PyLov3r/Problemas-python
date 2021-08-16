a = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

def kadane(a):
    max_momento = max_global = a[0]
    for i in range(1,len(a)):
        max_momento = max(a[i],max_momento + a[i])
        if max_momento > max_global:
            max_global = max_momento
    return max_global

print(kadane(a))