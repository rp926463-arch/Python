a = [1, 2, 3, 4, 5]

def min_from_rotatedArray(a):
    n = len(a)
    i = n-1
    while a[i] > a[i-1]:
        i = i-1
    return a[i]

print(min_from_rotatedArray(a))