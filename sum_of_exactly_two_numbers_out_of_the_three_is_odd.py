# Chef has 3 numbers A, B, C.
# Chef wonders if it is possible to choose exactly two numbers out of the three numbers
# such that their sum is odd.
a=int(input(""))
for i in range(0,a):
    l=input("").split(" ")
    n=m=0
    for x in l:
        if int(x)%2==0:
            n=n+1
        else:
            m=m+1
    if (m==1 and n==2):
        print("YES")
    elif (n==1 and m==2):
        print("YES")
    else:
        print("NO")