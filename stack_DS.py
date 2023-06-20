print("---------------------------------------------------")
print('create stack')
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

print('is stack a empty', isempty(a))

print('is stack b empty', isempty(b))

print("---------------------------------------------------")

print('create an peek function')

def peek(x):
    if isempty(x):
        return None
    else:
        return(x[len(x)-1])
    
print('peek a =', peek(a))

print('peek b =', peek(b))

print("---------------------------------------------------")

print('create an push function')

def push(x, item):
    x.append(item)
    return x
    
print('push a with 1 =', push(a,1))

print('push b with 7 =', push(b,7))

print("---------------------------------------------------")

print("---------------------------------------------------")

print('create an pop function')

def s_pop(x):
    if isempty(x):
        return ('stack is empty')
    else:
        return x.pop()
    
print('pop a  =', s_pop(a))
print("after pop of a = ",a)
print('pop b = ', s_pop(b))
print("after pop of b = ",b)
for i in range(len(b)):
    s_pop(b)
    print(b)
print("---------------------------------------------------")

print("---------------------------------------------------")

print('create an delete function')

def s_delete(x):
    x = []
    return x

print('delete a  =', s_delete(a))
print('delete b = ', s_delete(b))

print("---------------------------------------------------")


    





