class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    count = 0

    def __init__(self):
        self.head = None

    #INSERTION
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        itr = self.head
        
        while itr.next:
            itr = itr.next
        
        itr.next = node
    
    def insert_at_index(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        node = Node(data)
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        ctr = 0 
        while ctr < index-1:
            itr = itr.next
            ctr += 1
        
        node.next = itr.next
        itr.next = node
    
    def insert_after_value(self, value, data):
        #search for first occ of value and insert new data after that value
        node = Node(data)
        itr = self.head
        while itr.data != value:
            itr = itr.next
        node.next = itr.next
        itr.next = node
    
    def convert_list_to_ll(self, l):
        for i in l:
            self.insert_at_end(i)
    
    
    #DELETION
    def delete_from_begining(self):
        temp = self.head
        self.head = temp.next
        return temp.data
    
    def delete_from_end(self):
        itr1 = self.head
        itr2 = self.head
        while itr1.next:
            itr2 = itr1
            itr1 = itr1.next
        itr2.next = None
        return itr1.data
        
    def delete_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        ctr = 0 
        while ctr < index-1:
            itr = itr.next
            ctr += 1
        temp = itr.next
        itr.next =  itr.next.next
        return temp.data
    
    def delete_by_value(self, value):
        #remove first node that contains data 
        itr1 = itr2 = self.head
        while itr1.data != value:
            itr2 = itr1
            itr1 = itr1.next
        itr2.next = itr1.next
        return itr1.data
        
        
    #OTHER OPERATIONS
    def get_length(self):
        itr = self.head
        while itr:
            self.count += 1
            itr = itr.next
        return self.count
        
    def display(self):
        if self.head is None:
            print("LL is empty")
            return
        
        itr = self.head
        lstr = ""
        
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print(lstr)
        
if __name__ == '__main__':
    lst = LinkedList()
    #lst.insert_at_beginning(5)
    #lst.insert_at_beginning(89)
    #lst.insert_at_end(5)
    #lst.insert_at_end(89)
    lst.convert_list_to_ll([1,2,3,4])
    #lst.insert_at_index(100, 4)
    lst.display()
    #lst.insert_after_value(9,100)
    print(lst.delete_by_value(3))
    #lst.delete_at_index(4)
    #print(lst.delete_from_begining())
    #print(lst.get_length())
    #print(lst.delete_from_end())
    lst.display()
    
        