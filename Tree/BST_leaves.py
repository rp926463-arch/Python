class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inorder_traversal()
        
        return elements
            
    def get_leaves(self):
        
        #Iterative approach
        s1 = [] #store all elements of tree
        s2 = [] #store leaves
        s1.append(self)
        while len(s1) != 0:
            curr = s1.pop()
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)
            elif curr.left is None and curr.right is None:
                s2.append(curr.data)
        while len(s2) != 0:
            print(s2.pop(), end=" ")
        
        #Recursion approach
        '''
        if not root:
            return
        if self.left:
            self.left.get_leaves()
        if self.right:
            self.right.get_leaves()
        if self.left is None and self.right is None:
            print(self.data, end=" ")
        '''
    
    def get_internal_nodes(self):
        q = []
        q.append(self)
        while len(q):
            curr = q[0]
            q.pop(0)
            isInternal = 0
            if curr.left:
                isInternal = 1
                q.append(curr.left)
            if curr.right:
                isInternal = 1
                q.append(curr.right)
            if isInternal:
                print(curr.data, end=" ")    
        
if __name__ == '__main__':
    root = BST(1)
    root.left = BST(2)
    root.right = BST(3)
    root.left.left = BST(4)
    root.left.right = BST(5)
    root.right.left = BST(6)
    root.right.right = BST(7)
    
    #print(root.inorder_traversal())
    #root.get_leaves()
    root.get_internal_nodes()