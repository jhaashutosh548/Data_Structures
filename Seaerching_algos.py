def linner(x, value):
    for i in range(len(x)):
        if x[i] == value:
            return i
    return -1

x = [1,23,45, 75,878,3432,2323,4,5,66,9]

print(linner(x,45))

def bs(x, value):
    l = 0
    h = len(x)-1
    m = 0

    while l <= h:
        m = (l+h)//2
        mid_value = x[m]

        if mid_value == value:
            return m
        
        if mid_value < value:
            l = m+1
        else:
            h = m-1
    return 'value not found'

x.sort()

print(x)

print(bs(x,75))

def bsr(x,value,l,h):
    if l>h:
        return "value not found"
    m = (l+h)//2
    mid_value = x[m]

    if mid_value == value:
        return m
    
    if mid_value < value:
        l = m+1
    else:
        h = m-1
    return bsr(x,value,l,h)


print(bsr(x,1000,0,len(x)-1))
    
    






