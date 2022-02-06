import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__+" took "+str((end-start)*1000)+" ms")
        return result
    return wrapper

@time_it        
def calculate_square(l):
    result = []
    for i in l:
        result.append(i*i)
    return result

@time_it
def calculate_cube(l):
    result = []
    for i in l:
        result.append(i*i*i)
    return result

def dec(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return "**"+res[:2]+"**"
    return wrapper

@dec
def test(l):
    result = ""
    return result.join(list(map(str, l)))



###CHAINING DECORATORS##
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


#printer("Hello")


##DECORATOR Using CLASS
class Logging: 
  
    def __init__(self, function): 
        self.function = function 
  
    def __call__(self, *args, **kwargs):
      print(f'Before {self.function.__name__}')
      self.function(*args, **kwargs)
      print(f'After {self.function.__name__}')
  
  
@Logging
def sum(x, y):
  #print(x + y)

#sum(5,2)


##Iterator



#l = range(1,100000)

#l_itr = iter(l)
#for i in range(len(l_itr))):
    #print(next(l_itr))



#print(l)
#d1 = Demo(l)
#print(d.count_number_of_occurance())
#calculate_square(l)
#calculate_cube(l)
#print(test(l))



class Demo:
    def __init__(self, argv*):
        print(argv*)




d = Demo(input())


 
    
    
    
    
    
    
    
    

