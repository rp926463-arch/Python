class Solution:
    def __init__(self):
        self.a3 = []
    
    def merge(self, a1, a2, n1, n2):
        pa1 = 0
        pa2 = 0
        
        while True:
            if a1[pa1] < a2[pa2]:
                self.a3.append(a1[pa1])
                pa1 = pa1 + 1
            else:
                self.a3.append(a2[pa2])
                pa2 = pa2 + 1 
            if pa1 >= len(a1) or pa2 >= len(a2):
                break
        for i in range(pa1, len(a1)):
            self.a3.append(a1[i])
            
        for j in range(pa2, len(a2)):
            self.a3.append(a2[j])
        
        return self.a3


n1 = int(input())
#a1 = [int(i) for i in input().split()]
a1 = list(map(int, input().strip().split()))
n2 = int(input())
#a2 = [int(i) for i in input().split()]
a2 = list(map(int, input().strip().split()))

s = Solution()
print(s.merge(a1, a2, n1, n2))
