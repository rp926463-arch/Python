
class test:
    def __init__(self, dict):
        self.dict = dict

    def display(self):
        print(self.dict)

    def opt1(self):
        print(dict["February"]-dict["January"])
        print(dict["February"]+dict["January"]+dict["March"])
        print([k for k,v in dict.items() if v==2000])
        dict["June"] = 1980
        print(dict)
        dict["April"] = dict["April"]+200 
        print(dict)
        
dict = {"January":2200, 
                "February":2350,
                "March":2600,
                "April":2130,
                "May":2190
            }    
t1 = test(dict)
#t1.display()
#t1.opt1()

#if we define variable inside init() & inside class it is instance variable
#if we define variable outside init() & inside class it is Class/Static variable i.e for all objects value will be same


#Methods
'''
1)instance method : def opt1(self)

2)Static method : 

@classmethod
def opt2(cls):
    pass

3)Class method

@staticmethod
def opt3():
    pass
    
'''
heros=['spider man','thor','hulk','iron man','captain america']

print(heros)

heros.append('black panther1')

print(heros)

heros.remove('black panther1')

print(heros)

def get_index(s):
    for i in range(len(heros)):
        if heros[i] == s:
            return int(i)

heros.insert(int(get_index('hulk'))+1, 'black panther1')

print(heros)

heros[get_index('thor'):get_index('hulk')+1] = ['doctor Strange']

print(heros)

heros.sort()

print(heros)


class new:
    @classmethod
    def odd(cls, max_num):
        return [i for i in range(max_num) if i%2!=0]
            
max_num = int(input())
print(new.odd(max_num))