'''
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
'''
from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.container = deque()
        
    def enqueue(self, val):
        self.container.appendleft(val)
    
    def dequeue(self):
        if len(self.container)==0:
            print("Queue is empty")
            return
        
        return self.container.pop()
        
    def size(self):
        return len(self.container)
        
    def is_empty(self):
        return len(self.container)==0


q = Queue()

def producer(orders):
    for i in orders:
        print("Placing order for : ", i)
        q.enqueue(i)
        time.sleep(0.5)
    
def consumer():
    time.sleep(1)
    
    while not q.is_empty():
        order = q.dequeue()
        print("Now Serving : ", order)
        time.sleep(2)
        print(order, "served...")
    
    print("All orders completed")
    
if __name__ == '__main__':
    
    orders = ['pizza','samosa','pasta','biryani','burger']
    t = time.time()
    
    t1 = threading.Thread(target=producer, args=(orders,))
    t2 = threading.Thread(target=consumer)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Time taken to serve orders = ",time.time()-t)
