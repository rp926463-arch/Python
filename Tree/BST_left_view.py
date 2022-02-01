class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class view: 
    def __init__(self):
        self.maxLevel = 0
    
    def left_view(self, root, level):
        if root is None:
            return
        
        if self.maxLevel < level:
            print(root.data)
            self.maxLevel = level
        
        self.left_view(root.left, level+1)
        self.left_view(root.right, level+1)

if __name__ == '__main__':
    root = BST(1)
    root.left = BST(2)
    root.right = BST(3)
    root.right.right = BST(6)
    
    v = view()
    v.left_view(root,1)


'''
            1
        2       3
                    6

o/p : 1 2 6
'''