n=int(input("enter no.="))
b=int(input("enter no. 0 or 1="))
c=bool(b)
while bool(1):
    if c==True:
        i = 1
        while i<=n:
            print("*"*i)
            i+=1
    elif c==False:
        i=n
        while i <= n and i>0:
            print("*"*i)
            i-=1
    n = int(input("enter no.="))
    b = int(input("enter no. from 0 or 1="))
    c = bool(b)