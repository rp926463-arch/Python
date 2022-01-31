class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [(0,0) for i in range(self.MAX)]
        
    def getHash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum%self.MAX
    
    def __setitem__(self, key, val):
        h = self.getHash(key)
        count = 0
        while self.arr[h][0] and count!=len(self.arr):
            h = (h+1)%self.MAX
            count += 1
        if count==len(self.arr):
            print("Increase size of hash table")
        else:
            self.arr[h] = (key, val)
        
        
    def __getitem__(self, key):
        h = self.getHash(key)
        count = 0
        while self.arr[h][0] != key and count!=len(self.arr):
            h = (h+1)%self.MAX
            count += 1
        if count==len(self.arr):
            return "Not found"
        else:
            return self.arr[h][1]

    def __delitem__(self, key):
        h = self.getHash(key)
        count = 0
        while self.arr[h][0] != key and count!=len(self.arr):
            h = (h+1)%self.MAX
            count += 1
        if count==len(self.arr):
            return "Not found"
        else:
            del self.arr[h]
        

t = HashMap()

t['march 6'], t['march 17'], t['march 9'], t['march 4'] = 6,17,9,4

print(t.arr)
del t['march 6']
print(t.arr)


#print(t.arr)
#print(t.getHash('march 6'))
#print(t.getHash('march 17'))
#print(t.getHash('march 9'))
'''