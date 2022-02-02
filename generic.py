#Given a binary string, count number of substrings that start and end with 1.
'''
def countSubStr(st,n):
    count = 0
    for i in range(n):
        if st[i]=='1':
            for j in range(i+1,n):
                if st[j]=='1':
                    count += 1 
    return count

st = "00100101";
list(st)
n= len(st)
print(countSubStr(st, n), end="")

'''
#Merge Overlapping Intervals
'''
def mergeIntervals(arr):
        arr.sort(key = lambda x: x[0])
        m = []
        s = -10000
        max = -100000
        for i in range(len(arr)):
            a = arr[i]
            print(a)
            if a[0] > max:
                if i != 0:
                    m.append([s,max])
                max = a[1]
                s = a[0]
            else:
                if a[1] >= max:
                    max = a[1]
		
		#'max' value gives the last point of
		# that particular interval
		# 's' gives the starting point of that interval
		# 'm' array contains the list of all merged intervals
        if max != -100000 and [s, max] not in m:
            m.append([s, max])
        print("The Merged Intervals are :", end = " ")
        for i in range(len(m)):
            print(m[i], end = " ")

arr = [[9, 18], [1, 3], [2, 4], [4, 7]]
mergeIntervals(arr)
'''
#STACK & QUEUE Implementation
'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0)


class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

if __name__=='__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    #print(q.queue)
    #print("dequeued {}".format(q.dequeue()))
    #print(q.queue)
    #print("dequeued {}".format(q.dequeue()))
    #print(q.queue)
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    #print(s.stack)
    #print("Popped {}".format(s.pop()))
    #print(s.stack)
    #print("Popped {}".format(s.pop()))
    #print(s.stack)
    
'''

#Alice has an even number of N beads, and each bead has a number from 1 to N painted on it. 
#She would like to make a necklace out of all the beads, with a special requirement: 
#any two beads next to each other on the necklace must sum to a prime number. 
#Alice needs your help to calculate how many ways it is possible to do so.
'''
For example:

N = 4

There are two possible ways to build the necklace. Note that the last bead connects to the first bead.

1 2 3 4
1 4 3 2

Note: The necklace should be unique. For example: 1 2 3 4 is the same as 2 3 4 1 and 3 4 1 2 and 4 1 2 3.


from itertools import permutations
n = int(input())
l = [int(i) for i in range(1,n+1)]
p = list(permutations(l))

li=[]
for i in p[:fact(len(l)-1)]:
    flag = 0
    for j in range(1,len(i)):
        s = i[j-1] + i[j]
        if not is_prime(s):
            flag=1
            break
    if flag==0:
        li.append(i)
        
print(li)
    
'''
'''
a = 'Hacker'
#print(a[::-1])
#print(a[::-4])

l = [1,2,3,4,5,6,7,8,9]
l = l[::-4]

l = l[-5-5:3]

l = l[0:-1+2]

#print(l[-2::])

t = [(2,1),(1,1),(2,4),(2,6),(7,5),(6,4)]
res = {}
for i,j in t:
    res.setdefault(j,[]).append(i)
print(res)
'''

'''
def MainCount(f):
    def progFirst(*agrs,**kwargs):
        progFirst.calls += 1
        return f(*agrs,**kwargs)
    progFirst.calls = 0
    return progFirst
   
@MainCount
def progSecond(i):
    return i+1
    
@MainCount
def Count(i=0, j=1):
        return i*j + 1
print(progSecond.calls)

for n in range(5):
    progSecond(n)

Count(j=0, i=1)
print(Count.calls)
'''
'''
def myFun(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    #print("args: ", args)
	#print("kwargs: ", kwargs)


myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")
'''
'''
import requests
import os
from pathlib import Path

url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'

response = requests.get(url)

#Create Direcctory if not exist
Path(os.path.join(os.getcwd()+'\\tmp')).mkdir(parents=True, exist_ok=True)

path = os.path.join(os.getcwd(), 'tmp','metadata.pdf')
with open(path, 'wb') as f:
    f.write(response.content)
'''
#import pandas as pd

#df = pd.read_parquet(r'C:\Users\rosha\Downloads\Seattle.parquet', engine='pyarrow')
#print(df.head())
'''
import os
import threading
def print_cube(n):
    print(n*n*n)
    print('PID for t1 = {}'.format(os.getpid()))
    
def print_square(n):
    print(n*n)
    print('PID for t2 = {}'.format(os.getpid()))
    
if __name__ == '__main__':
    t1 = threading.Thread(target=print_cube, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))
    print('PID for main = {}'.format(os.getpid()))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print('Done')
    
'''

# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "public var"
        self._c = "protected var"
        self.__b = "Private var"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._c)
        #print("Calling private member of base class: ")
        #print(self.__b)


# Driver code
obj1 = Derived()
obj2 = Base()
#print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class


