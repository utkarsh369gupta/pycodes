for i in range (int(input())):
    a,b=map(int,input().split(" "))
    for x in range(a):
        b=b*(b+1)//2
    print(b)

# my try

"""
# program 1
def sum(N):
    a = 0
    for x in range(1, N + 1):
        a = a + x
    print(a)
for i in range(int(input())):
    b=input().split(" ")
    D=int(b[0])
    N=int(b[1])
    for c in range(D):
        N=sum(N)
        # sum(N)
    print(N)
"""