# program 1
a=int(input("enter no = "))
f=1
for i in range(1,a+1):
    f=f*i
print(f)

# program 2
n=int(input())
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
    # return factorial
factorial(n)


# program 3
n=int(input("enter"))
def fr(n):
    if n==1:
        return 1
    else:
        return n*fr(n-1)
print(fr(n))