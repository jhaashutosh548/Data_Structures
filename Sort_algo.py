# quick sort 

def quicksort(x):
    if len(x) <= 1:
        return(x)
    else:
        p = x[0]
        l = [i for i in x[1:] if i < p]
        r = [i for i in x[1:] if i >= p]
        return quicksort(l) + [p] + quicksort(r)
    
arr = [4,3,2,1,2,5,6,74,4]
sorted_array = quicksort(arr)
print(sorted_array)


#tc = O(nlogn) recus
#tc = O(n^2) normal
#sc = O(n)

def marge(x,l,m,r):
    n1 = m-l+1
    n2 = r-m

    L = []
    R = []
    print(n1)

    for i in range(0,n1):
        L.append(x[l+i])

    for j in range(0,n2):
        R.append(x[m+1+j])

    i = 0 # for l side
    j = 0 # for r side
    k = l # for merged one

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            x[k] = L[i]
            i += 1
        else :
            x[k] = R[j]
            j += 1
        k+=1
    
    while i<n1:
        x[k] = L[i]
        i+=1
        k+=1

    while j<n2:
        x[k] = R[j]
        j+=1
        k+=1

def margesort(x,l,r):
    if l<r:
        m= l+(r-l)//2
        margesort(x,l,m)
        margesort(x,m+1,r)
        marge(x,l,m,r)

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
margesort(arr,0,len(arr)-1)
print(arr)

#tc = O(nlogn) recus
#tc = O(n^2) normal
#sc = O(n)

# selection sort

def sectionsort(x):
    l = len(x)
    for i in range(0,l):
        min_ind = i
        for j in range(i+1,l):
            if x[j] < x[min_ind]:
                min_ind = j
        x[i],x[min_ind] = x[min_ind],x[i]

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
sectionsort(arr)
print('selection sort : ',arr)


def bubblesort(x):
    l = len(x)
    swapped = False
    for i in range(l-1):
        for j in range(0,l-i-1):
            if x[j]>x[j+1]:
                swapped = True
                x[j],x[j+1]=x[j+1],x[j]
        if not swapped:
            return
        
arr = [12,34,2,98,46,19,45,54,32,74,15,34]
bubblesort(arr)
print('bubble sort : ',arr)
        

def insertionsort(x):
    l = len(x)
    if l<=1:
        return
    for i in range(1,l):
        n = x[i]
        j = i-1
        while j>=0 and n < x[j]:
            x[j+1] = x[j]
            j=j-1
        x[j+1]=n

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
insertionsort(arr)
print('insertion sort : ',arr)










