#Given array a and sum k check for pair in a with sum k

def check_pair(a,sum, l, r):
    while l<r:
        if a[l]+a[r] == sum:
            return (a[l], a[r])
        elif a[l]+a[r] < sum:
            l = l+1
        else:
            r = r-1
    return None

a = [0, -1, 2, -3, 1]
sum = -2
l = 0
r = len(a)-1
a = sorted(a)
print(check_pair(a,sum, l, r))
