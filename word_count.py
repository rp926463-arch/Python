from collections import Counter
from itertools import chain

class Test:
    def __init__(self):
        self.d = {}
    
    def get_word_count(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    try:
                        self.d[word] += 1
                    except KeyError:
                        self.d[word] = 1
        return self.d
    
    def sorted_dict(self, d):
        return {k:v for k,v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
                
if __name__ == '__main__':
    filename = r'C:\Users\rosha\OneDrive\Desktop\poem.txt'
    t = Test()
    print(t.sorted_dict(t.get_word_count(filename)))     