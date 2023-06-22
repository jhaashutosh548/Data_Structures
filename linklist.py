print('------------------------------------------')
class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class linklist:
    def __init__(self, head = None):
        self.head = head
    
    def add(self, data,):
        new = node(data)
        if (self.head):
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new
        else:
            self.head = new

    def display(self, first=None):
        self.first = first
        first = self.head
        while(first):
            print('data')
            print(first.data)
            print('address')
            print(first.next)
            first= first.next

    def insert(self,new = None):
        self.new = new
        newnode = node(new) 
        newnode.next = self.head
        self.head = newnode 

    def insertmid(self, data, x):
        self.data = data
        self.x = x
        temp = self.head
        newnode = node(data)
        while(temp):
            if(temp.data == x):
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next


print('craeteinga ll')
item = linklist()
print('adding 20 to the list')
item.add(20)
item.add(30)
item.add(40)
item.display()
print(item.head.data)
print('add data in the start ')
item.insert(10)
item.display()
item.insertmid(55,30)
item.display()



