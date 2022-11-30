import random
a=int(input("enter no. = "))
n=random.randint(0,100)
i=0
while i<=10 :
    if a<n:
        print("no. is greater than your no.")
        a = int(input("enter no. = "))
    elif a==n:
        print("you won")
        print("number of moves you taken",i+1)
        break
    elif a>n:
        print("no. is smaller than your no.")
        a = int(input("enter no. = "))
    i=i+1
if i>10:
    print("you loose!!!")
