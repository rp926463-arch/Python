class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
class LL:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        node.prev = itr
        itr.next = node
        
    
    def create_DLL_from_list(self, lst):
        for i in lst:
            self.insert_at_end(i)
        
    def print_forward(self):
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '<-->'
            itr = itr.next
        print(lstr)
    
    def print_backward(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        lstr = ''
        while itr:
            lstr += str(itr.data) + '<-->' 
            itr = itr.prev
        print(lstr)
        
        
if __name__=='__main__':
    lst = LL()
    #lst.insert_at_end(1)
    #lst.insert_at_end(2)
    lst.create_DLL_from_list([1,2,3,4,5])
    lst.print_forward()
    lst.print_backward()