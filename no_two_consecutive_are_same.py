'''Chef has a binary string S of length N. Chef can perform the following operation on S:

Insert any character (0 or 1) at any position in S.
Find the minimum number of operations Chef needs to perform so that no two consecutive characters
are same in S.'''


a=int(input(""))
for i in range(a):
    b=int(input(""))
    c=input("")
    r = 0
    for x in range(1,b):
        if c[x-1]==c[x]:
            r+=1
    print(r)