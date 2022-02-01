
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

class Solution:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def build_tree(self, arr):
        r = Node(arr[0])
        for i in range(1, len(arr)):
            self.insert(r, arr[i])
        #self.inorder(r)
        print(self.sum_tree(r))
        #print(self.count_nodes(r))
    
    def sum_tree(self,root):
        if root.right is None and root.left is None:
            return root.val
        return self.sum_tree(root.left) + root.val + self.sum_tree(root.right)
        
    def count_nodes(self, root):
        if root.left is None and root.right is None:
            return 1
        return self.count_nodes(root.left)+1+self.count_nodes(root.right)
        
if __name__ == '__main__':
    arr = [50,30,20,40,70,60,80]
    s = Solution()
    s.build_tree(arr)
    