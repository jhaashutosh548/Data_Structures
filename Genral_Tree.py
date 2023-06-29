class treenode:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None
    
    def addchild(self, c):
        c.parent = self
        self.child.append(c)


root = treenode('class')

class1 = treenode('class1')
class1.addchild(treenode('arjun'))
class1.addchild(treenode('raj'))
class1.addchild(treenode('riya'))

class2 = treenode('class2')
class2.addchild(treenode('arun'))
class2.addchild(treenode('rajesh'))
class2.addchild(treenode('reva'))

root.addchild(class1)
root.addchild(class2)



