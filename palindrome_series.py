a=input("enter a series:")
b=len(a)
for i in range(1,b):
    if a[i-1]==a[-i]:
        print("it is palindrome")
        break
else:
    print("it is not a palindrome")