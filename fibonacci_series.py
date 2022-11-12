# it is a series like 0 1 1 2 3 5 8 13 21 ______

n=int(input("enter no :"))
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))
