import random; n1='';x1=''
def cl():
    for i in range(25):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
cl()
myList=["rock", "paper", "scissors"]
listlist=[["1","1 player","1 players"],["2","2 player","2 players"]]
p=(input("1 player or 2 players?: ")).lower()
while (p not in listlist[0]) and (p not in listlist[1]):
    print("Invalid: You are Invalid.")
    p=(input("1 player or 2 players?: ")).lower()
if p in listlist[0]:
    x=random.choice(myList)
if p in listlist[1]:
    x=(input("First player: Rock, paper or scissors?: ")).lower()
    cl()
    n=(input("Second player: Rock, paper or scissors?: ")).lower()
    cl()
    x1="First player "
    n1="Second player "
else:
    n=(input("Rock, paper or scissors?: ")).lower()
    n1="You "
while not n in myList:
        print("Invalid: You are Invalid.")
        n=(input("Rock, paper or scissors?: ")).lower()
if (n=="rock" and x=="scissors") or (n=="paper" and x=="rock") or (n=="scissors" and x=="paper"):
    print(f"{n.capitalize()} beats {x}")
    print(f"{n1}won!")
elif n==x:
    print(f"Draw. ({n} x {x})")
else:
    print(f"{x.capitalize()} beats {n}")
    if p in listlist[1]:
        print(f"{x1}win")
    else:
        print("Game over.")