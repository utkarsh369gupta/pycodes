# armstrong meaning cube of every digit and then sum

# program 1
x=input("enter no. =")
s1=0
for i in range(0,len(x)):
    s1+=int(x[i])**3
print(s1)


# these are the program to give the sum of any power to the digits :

# program 2
b=input("enter no. : ")
a=int(b)
n=len(b)
s=0
for i in range(0,n):
   s=s+int(b[i])**3
if s==a:
    print("no. is armstrong")
else:
    print("no. is not armstrong")


# program 3
a1=input("enter no. = ")
b1=int(input("enter power = "))
sum=0
i=0
for i in range(0,len(a1)):
    d=int(a1[i])**b1
    sum=sum+d
    i=i+1
print(sum)
