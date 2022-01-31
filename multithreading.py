import time
import threading

def cal_square(numbers):
    for n in numbers:
        time.sleep(0.1)
        print('Square', n*n)
    
def cal_cube(numbers):
    for n in numbers:
        time.sleep(0.1)
        print('Cube', n*n*n)

arr = [1,2,3,4,5]

t = time.time()

t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Time taken=", time.time()-t)



'''
import time

def cal_square(numbers):
    for n in numbers:
        time.sleep(0.1)
        print('Square', n*n)
    
def cal_cube(numbers):
    for n in numbers:
        time.sleep(0.1)
        print('Cube', n*n*n)

arr = [1,2,3,4,5]

t = time.time()

cal_square(arr)
cal_cube(arr)

print("Time taken=", time.time()-t)

'''