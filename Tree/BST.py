class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
        #add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
        #add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    def inorder_traversal(self):
        elements=[]
        #visit left subtree
        if self.left:
            elements += self.left.inorder_traversal()
        #visit base node
        elements.append(self.data)
        #visit right subtree
        if self.right:
            elements += self.right.inorder_traversal()
        return elements
    
    def preorder_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()
        return elements
        
    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()
        elements.append(self.data)
        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
        
    def find_sum(self):
        left_sum = self.left.find_sum() if self.left else 0
        right_sum = self.right.find_sum() if self.right else 0
        return self.data + left_sum + right_sum
        
    def search(self, item):
        if item == self.data:
            return True
        if item < self.data:
            if self.left:
                return self.left.search(item)
            else:
                return False
        else:
            if self.right:
                return self.right.search(item)
            else:
                return False

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
    
            #USING MAX val from left subtree
            max_val = self.left.find_max()
            self.data =max_val
            self.left = self.left.delete(max_val)
            
            #USING MIN val from right subtree
            #min_val = self.right.find_min()
            #self.data = min_val
            #self.right = self.right.delete(min_val)
        return self
        
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
 

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    num_tree = build_tree(numbers)
    print(num_tree.inorder_traversal())
    num_tree.delete(9)
    print(num_tree.inorder_traversal())
    num_tree.delete(20)
    print(num_tree.inorder_traversal())
    #print(num_tree.search(18))
    #print(num_tree.find_min())
    #print(num_tree.find_max())
    #print(num_tree.find_sum())
    #print(num_tree.preorder_traversal())
    #print(num_tree.postorder_traversal())