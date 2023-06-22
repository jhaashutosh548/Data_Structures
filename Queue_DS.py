print("---------------------------------------------------")
print('create queue')
a = []
print(a)
b = [1,2,3,4,5,6]
print(b)
print("---------------------------------------------------")
print('create an isempty function')

def isempty(x):
    if x == []:
        return True
    else :
        return False

print('is queue a empty', isempty(a))

print('is queue b empty', isempty(b))

print("---------------------------------------------------")

print('create an peek function')

def peekque(x):
    if isempty(x):
        return None
    else :
        return x[0]

print("peek of a is ",peekque(a))
print("peek of b is ",peekque(b))

print("---------------------------------------------------")

print('create enque i.e adding data to the queue')

def enque(x,i):
    x.append(i)

enque(a,2)
enque(b,7)

print("enque updated of a is ",a)
print("enque updated of b is ",b)


print("---------------------------------------------------")


def deque(x):
    if isempty(x):
        return None
    else :
        return x.pop(0)

print("dequed element of a is ",deque(a))
print("dequed element of b is ",deque(b))

print("deque updated of a is ",a)
print("deque updated of b is ",b)


print("---------------------------------------------------")

def deleteque(x):
    x = []
    return x

b = deleteque(b)

print(b)



