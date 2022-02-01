class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self, index=2):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        if index!=2:
            print(prefix + self.data[index].strip("()"))
        else:
            print(prefix + ' '.join(self.data))
        for i in self.children:
            i.print_tree(index)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
      
      
def build_tree():
    root = TreeNode(["Nilupul", "(CEO)"])
    chinmay = TreeNode(["Chinmay", "(CTO)"])
    gels = TreeNode(["Gels", "(HR Head)"])
    vishwa = TreeNode(["Vishwa", "(Infrastructure Head)"])
    aamir = TreeNode(["Aamir", "(Application Head)"])
    
    vishwa.add_child(TreeNode(["Dhaval", "(Cloud Manager)"]))
    vishwa.add_child(TreeNode(["Abhijeet", "(App Manager)"]))
    gels.add_child(TreeNode(["Peter", "(Recruitment Manager)"]))
    gels.add_child(TreeNode(["Waqas", "(Policy Manager)"]))
    
    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)
    root.add_child(chinmay)
    root.add_child(gels)
    
    #print(chinmay.get_level())
    
    return root
    

    
if __name__ == '__main__':
    root = build_tree()
    print("Press 0 --> Name Tree\nPress 1 --> Designation Tree\nPress 2 --> Name&Designation Tree")
    index = int(input())
    root.print_tree(index)
    #print(root.get_level())
    
    