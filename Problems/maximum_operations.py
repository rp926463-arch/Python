# You are given 3 numbers a,b,c You can subtract 1 from any two numbers in one operation
# You are required to determine maximum number of operations that can be performed such that no number is negative

# Consist of 2 test cases

# 2
# 2 3 4
# 1 2 5

# 4
# 3

# 2 3 4 -> 2 2 3 -> 2 1 2 -> 1 1 1 -> 0 0 1   hence 4
# 1 2 5 -> 1 1 4 -> 1 0 3 -> 0 0 2 hence 3

def solve(a, b, c):
    l = [a,b,c]
    cnt = 0
    exit_f = False
    while True:
        #print(l, end=' -> ')
        l.sort()
        tmp = []
        tmp.append(l[0])
        flag = True
        for i in l:
            if flag:
                flag = False
                continue
            if i-1>=0:
                tmp.append(i-1)
            else:
                exit_f = True
        if exit_f:
            break
        l = tmp
        cnt = cnt + 1
    
    return cnt

T = int(input())
for _ in range(T):
    a,b,c = map(int, input().split())
    out_ = solve(a,b,c)
    #print('\n{}'.format(out_))
    print(out_)

