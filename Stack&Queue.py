from collections import deque
class Stack():
    def __init__(self):
        self.container = deque()
        
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
        
    def peek(self):
        return self.container[-1]
        
    def is_empty(self):
        return len(self.container)==0
        
    def size(self):
        return len(self.container)
        
class Queue:
    def __init__(self):
        self.container = deque()
        
    def enqueue(self, val):
        self.container.appendleft(val)
        
    def dequeue(self):
        return self.container.pop()
        

class Exercise:
    def __init__(self):
        self.rev_str = ""
        
    def reverse_string(self, st):
        s = Stack()
        [s.push(i) for i in st]
        
        while s.size()!=0:
            self.rev_str += s.pop()
        return self.rev_str
    
    def is_balanced(self, st):
        s = Stack()
        for i in st:
            if i in ['{', '[', '(']:
                s.push(i)
            elif i in ['}', ']', ')']:
                try:
                    s.pop()
                except IndexError:
                    return False
            else:
                pass
        
        return s.size()==0

if __name__ == "__main__":
        #s = Stack()
        #q = Queue()
        #s.push(5)
        #s.push(4)
        #s.push(3)
        #print(s.container)
        #s.pop()
        #print(s.container)
        
        #q.enqueue(1)
        #q.enqueue(2)
        #q.enqueue(3)
        #print(q.container)
        #q.dequeue()
        #print(q.container)
        #st = "We will conquer COVID-19"
        e = Exercise()
        #print(e.reverse_string(st))
        print(e.is_balanced("))"))