class node:
    def __init__(self,data,left =None,right= None):
        self.data = data
        self.right = right
        self.left=left

    def addnode(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.addnode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.addnode(data)
        else:
            self.data = data
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end = ' ')
        if self.right:
            self.right.inorder()
        
    def preorder(self):
        print(self.data, end= ' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end= ' ')
    
    def search(self,value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                if self.left.data:
                    return self.left.search(value)
        if value > self.data:
            if self.right:
                if self.right.data:
                    return self.right.search(value)
        return False
    
    def get_min(self):
        if self.left is None:
            return self.data
        return self.left.get_min()
    
    def get_max(self):
        if self.right is None:
            return self.data
        return self.right.get_max()
    
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right.delete(value)
        else: 
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            temp = self.right.get_min() 
            self.data = temp
            self.right = self.right.delete(temp)
        return self       
        



root  = node(50)
root.addnode(42)
root.addnode(78)
root.addnode(67)
root.addnode(34)
root.addnode(45)
root.inorder()
print(" ")
root.preorder()
print(" ")
root.postorder()
print(" ")
print(root.search(42))
print(" ")
print(root.get_max())
print(" ")
print(root.get_min())
root.delete(42)
root.inorder()
print(" ")


from binarytree import Node , tree, bst ,build 

root = Node(50)
root.left = Node(40)
root.right = Node(60)
print(Node)



