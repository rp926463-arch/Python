from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()
        
    def enqueue(self,val):
        self.container.appendleft(val)
        
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container)==0
     
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.container.pop()
        
    def front(self):
        return self.container[-1]

def generate_binary(n):
    q = Queue()
    q.enqueue('1')
    
    for i in range(n):
        frnt = q.front()
        q.enqueue(frnt+'0')
        q.enqueue(frnt+'1')
        
        print(q.dequeue())
    
        
if __name__ == '__main__':
    generate_binary(10)