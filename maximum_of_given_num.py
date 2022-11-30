# program 1
list=[]
a=int(input("enter 1 for yes and 0 for no : "))
while a==1:
    b=int(input("enter no. : "))
    list.append(b)
    a = int(input("enter 1 for yes and 0 for no : "))
list.sort()
list.reverse()
print("maximum number is : ",list[0])

# program 2
b=input().split(" ")
for i in b:
    for x in range(len(b)):
        if int(i)>int(b[x]):
            max=i
print(max)
