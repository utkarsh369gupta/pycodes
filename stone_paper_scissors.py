import random
l=["stone","paper","scissors"]
a=random.choice(l)
c =1
co=0
m=0
while c==1:
    print("1 for stone\n2 for paper\n3 for scissors")
    b = int(input("enter your choice : "))
    if a=="stone" and b==1:
        print(a)
        print("draw")
    elif a=="stone" and b==2:
        print(a)
        print("you win")
        m+=1
    elif a=="stone" and b==3:
        print(a)
        print("you loss")
        co+=1
    elif a=="paper" and b==1:
        print(a)
        print("you loss")
        co+=1
    elif a=="paper" and b==2:
        print(a)
        print("draw")
    elif a=="paper" and b==3:
        print(a)
        print("you win")
        m+=1
    elif a=="scissors" and b==1:
        print(a)
        print("you win")
        m+=1
    elif a=="scissors" and b==2:
        print(a)
        print("you loss")
        co+=1
    elif a=="scissors" and b==3:
        print(a)
        print("draw")
    c=int(input("enter 1 to play more and 2 to end game:"))
    l = ["stone", "paper", "scissors"]
    a = random.choice(l)
if c==2:
    print("thanks for playing")
    print("your score is",m,"out of",co+m)
    if m>co:
        print("congratulations, you won the game!!!")
    elif m==co:
        print("game is draw")
    else:
        print("sorry, you loss the game")
else:
    print("error")

