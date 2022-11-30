j=input("enter string : ")
w=list(j)
n=len(j)
d=j[0]
for i in range(1,n):
    if j[i]==d:
        w[i]="$"
    # print(w[i],end="")
a="".join(w)
print(a)