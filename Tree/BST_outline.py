class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.maxLevel = 0
    
    def left_view(self, root, level, arr):
        if root is None:
            return
        if level > self.maxLevel:
            arr.append(root.data)
            self.maxLevel = level
        self.left_view(root.left, level+1, arr)

    def right_view(self, root, level, arr):
        if root is None:
            return
        if level > self.maxLevel:
            arr.append(root.data)
            self.maxLevel = level
        self.right_view(root.right, level+1, arr)

if __name__ == '__main__':
    root = BST(1)
    root.left = BST(2)
    root.right = BST(3)
    root.left.left = BST(4)
    root.left.right = BST(5)
    root.right.left = BST(7)
    root.right.right = BST(8)

    arr = []
    
    t = Tree()
    t.left_view(root.left,1,arr)
    arr.reverse()
    t.maxLevel = 0
    t.right_view(root,1,arr)
    
    print(arr)
    
'''
            1
        2       3
    4     5  7     8
    
o/p : 4 2 1 3 8

'''