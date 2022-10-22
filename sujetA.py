from math import *
n=int(input("taper le nombre n: "))
m=int(input("taper le nombre m: "))
while n<=4000 or m>10000 or n>m:
    n=int(input("taper le nombre n: "))
    m=int(input("taper le nombre m: "))
for i in range(n,m+1):
    R=0
    N=i
    while True:
        int(sqrt(i))
        rac=sqrt(i)
        j=2
        prm=True
        while prm and j<=rac:
            prm=i%j!=0
            j=j+1
        if prm:
            R=R+1
            i=i//10
        else:
            R=0
        if i==0 or R==0 :
            break
    if R!=0:
        print(N,end="\n")