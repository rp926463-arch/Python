class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, index):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        #print(self.children)
        for child in self.children:
            if child.get_level() <= index: 
                child.print_tree(index)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def buid_tree():

    root = TreeNode("Global")
    india = TreeNode("India")
    usa = TreeNode("USA")
    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karnataka")
    new_jersey = TreeNode("New Jersey")
    california = TreeNode("California")
    
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysor"))
    
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))
    
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))
    
    india.add_child(gujarat)
    india.add_child(karnataka)
    
    usa.add_child(new_jersey)
    usa.add_child(california)
    
    root.add_child(india)
    root.add_child(usa)
    
    
    return root

        
if __name__ == '__main__':
    root = buid_tree()
    print("Enter level")
    index = int(input())
    root.print_tree(index)