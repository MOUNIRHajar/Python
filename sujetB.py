N=int(input("donner un nombre"))
R=0
while N<0:
    N=int(input("donner un nombre"))
M=N%10
T=N*M
a=N 
while N!=0:
    R=R*10
    R=R+N%10
    N=N//10
if T==R and a==R:
    print("propre et symetrique")
else:
    if T==R:
        print("propre")
    else:
        if a==R:
            print("symétrique")
        else:
            print("non propre,non symétrique")