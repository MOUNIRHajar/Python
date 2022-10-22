bi=int(input("taper le nombre bi: "))
bs=int(input("taper le nombre bs: "))
while bi<=10 or bs>500 or bi>bs:
    bi=int(input("taper le nombre bi: "))
    bs=int(input("taper le nombre bs: "))
for i in range(bi,bs+1):
    t=0
    n=i
    while True:
        p=True
        for j in range(2,(i//2)+1):
            if i%j==0:
                p=False
        if p==False:
            t=0
        else:
            t=1
            m=i%10
            d=i//10
            if i<100:
                i=(m*10)+d
            else:
                i=(m*100)+d
        if n==i or p==False:
            break
    if t!=0:
        print(n,end="\n")