class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h%self.MAX
        
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, ele in enumerate(self.arr[h]):
            if len(ele)==2 and ele[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))
        #self.arr[h] = val
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]
    
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][idx]
        #self.arr[h] = None
    
t = HashMap()

t['march 6'], t['march 17'], t['march 9'] = 6,17,9
print(t.arr)
del t['march 6']
print(t.arr)

#print(t['march 17'])
#print(t['march 6'])
#print(t['march 9'])

#print(t['march 6'], t['march 17'], t['march 9'])


#print(t.get_hash('march 6'))    