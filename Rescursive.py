def find_sum(n):
    if n == 1:
        return 1
    elif n == 0 :
        return 0
    return n + find_sum(n-1)

print(find_sum(5))

#  0 1 2 3 4 5 6 7 8 9
#  0 1 1 2 3 5 8 13 21 34

def fib(n):
    if n ==0 or n==1:
        return n 
    return fib(n-1)+fib(n-2)

print(fib(30))