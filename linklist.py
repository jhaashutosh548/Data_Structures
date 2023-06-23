print('------------------------------------------')
# creating linklist
class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class linklist:
    def __init__(self, head = None):
        self.head = head
    
    # fuction to add data at the end of the list
    def add(self, data,):
        new = node(data)
        if (self.head):
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new
        else:
            self.head = new

    
    # function display the data list
    def display(self, first=None):
        self.first = first
        first = self.head
        print('------------')
        while(first):
            # print('data')
            print(first.data, end = ' ')
            # print('address')
            # print(first.next)
            first= first.next
        print('------------')

    # add data at the start of the linklist
    def insert(self,new = None):
        self.new = new
        newnode = node(new) 
        newnode.next = self.head
        self.head = newnode 


    # add data at the middle of the linklist
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
    
    # delete the data in the linklist
    def delete(self,value):
        temp = self.head
        while(temp!= None):
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    #search the data 
    def search(self,x):
        temp = self.head
        while(temp!=None):
            if (temp.data == x):
                return True
            temp = temp.next
        return False
    
    #sorting the ll
    def sort(self):
        temp = self.head
        a = []
        while(temp):
            a.append(temp.data)
            temp = temp.next 
        a.sort()
        x = linklist()
        for i in a:
            x.add(i)
        return x




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

item.delete(55)
item.display()

print('searching 55 in ll ',item.search(40))

item.add(5)
item.add(34)
item.display()

item = item.sort()
item.display()








