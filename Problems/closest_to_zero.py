#You have to print number with value closest to zero.
#if there are multiple elements print the number with greater value
import sys

def solve(N, A):
    closestIndex = 0
    diff = sys.maxsize
    for i in range(len(A)):
        abs_ = abs(A[i])
        if abs_ < diff:
            closestIndex = i
            diff = abs_
        elif abs_ == diff and A[i] > 0 and A[closestIndex]<0:
            # same distance to zero but positive
            closestIndex = i
    return A[closestIndex]        
    
N = input()
A = list(map(int, input().split()))

out_ = solve(N, A)
print(out_)


# 5
# 0 2 3 4 5

# ==>0

# 100
# -99 99 -98 98 -97 97 -96 96 -95 95 -94 94 -93 93 -92 92 -91 91 -90 90 -89 89 -88 88 -87 87 -86 86 -85 85 -84 84 -83 83 -82 82 -81 81 -80 80 -79 79 -78 78 -77 77 -76 76 -75 75 -74 74 -73 73 -72 72 -71 71 -70 70 -69 69 -68 68 -67 67 -66 66 -65 65 -64 64 -63 63 -62 62 -61 61 -60 60 -59 59 -58 58 -57 57 -56 56 -55 55 -54 54 -53 53 -52 52 -51 51 -50 50

# ==>50

# 100
# 99 -99 98 -98 97 -97 96 -96 95 -95 94 -94 93 -93 92 -92 91 -91 90 -90 89 -89 88 -88 87 -87 86 -86 85 -85 84 -84 83 -83 82 -82 81 -81 80 -80 79 -79 78 -78 77 -77 76 -76 75 -75 74 -74 73 -73 72 -72 71 -71 70 -70 69 -69 68 -68 67 -67 66 -66 65 -65 64 -64 63 -63 62 -62 61 -61 60 -60 59 -59 58 -58 57 -57 56 -56 55 -55 54 -54 53 -53 52 -52 51 -51 50 -50

# ==>50