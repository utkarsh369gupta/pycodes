a=int(input("enter no1 = "))
b=int(input("enter no2 = "))
c=input("enter operator = ")
print("choice from +,-,*,/,%")
while True:
    if a==45 and b==3 and c=="*":
        print(a,c,b," = 555")
        a = int(input("enter no1 = "))
        b = int(input("enter no2 = "))
        c = input("enter operator = ")
    elif a==56 and b==9 and c=="+":
        print(a,c,b," = 77")
        a=int(input("enter no1 = "))
        b=int(input("enter no2 = "))
        c=input("enter operator = ")
    elif a==56 and b==6 and c=="/":
        print(a,c,b," = 4")
        a=int(input("enter no1 = "))
        b=int(input("enter no2 = "))
        c=input("enter operator = ")
    elif c=="+":
        print(a,"+",b,"=",a+b)
        a=int(input("enter no1 = "))
        b=int(input("enter no2 = "))
        c=input("enter operator = ")
    elif c=="-":
        print(a,"-",b,"=",a-b)
        a=int(input("enter no1 = "))
        b=int(input("enter no2 = "))
        c=input("enter operator = ")
    elif c=="*":
        print(a,"*",b,"=",a*b)
        a=int(input("enter no1 = "))
        b=int(input("enter no2 = "))
        c=input("enter operator = ")
    elif c=="/":
        print(a,"/",b,"=",a/b)
        a=int(input("enter no1 = "))
        b=int(input("enter no2 = "))
        c=input("enter operator = ")
    elif c=="%":
        print(a,"%",b,"=",a%b)
        a=int(input("enter no1 = "))
        b=int(input("enter no2 = "))
        c=input("enter operator = ")
