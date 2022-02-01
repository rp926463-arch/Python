class Number:
    def catlanNo(self, n):
        n1, n2, sum = 0,0,0
        if n==1 or n==0:
            return 1
        
        for i in range(1, n+1):
            n1 = self.catlanNo(i-1)
            n2 = self.catlanNo(n-i)
            
            sum += n1*n2
        
        return sum
        
if __name__ == '__main__':
    c = Number()
    print(c.catlanNo(6))