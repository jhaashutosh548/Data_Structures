class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class clinklist:
    def __init__(self):
        self.head = None
 
    def add(self, data):
        new = node(data)
        temp = self.head
        if(self.head != None):
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new
        else:
            self.head = new
        new.next = self.head

    def display(self):
        print('------------------')
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp = temp.next
                if (temp.next == self.head):
                    print(temp.data)
                    break
    
    # delete the data in the linklist
    def delete(self,value):
        temp = self.head
        while(temp):
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
            if (temp == self.head):
                break
        prev.next = temp.next

    #search the data 
    def search(self,x):
        temp = self.head
        while(temp!=None):
            if (temp.data == x):
                return True
            temp = temp.next
            if (temp == self.head):
                return False
        return False
    
     #sorting the ll
    def sort(self):
        temp = self.head
        a = []
        while(temp):
            a.append(temp.data)
            temp = temp.next
            if temp == self.head : 
                break
        a.sort()
        x = clinklist()
        for i in a:
            x.add(i)
        return x




item = clinklist()
item.add(20)
item.display()
item.add(30)
item.display()
item.add(40)
item.display()
item.add(50)
item.add(60)
item.add(70)
item.add(80)
item.display()


item.delete(50)
item.display()
item.delete(60)
item.display()
print(item.search(40))
print(item.search(50))
item.add(20)
item.add(45)
item.display()
item = item.sort()
item.display()


