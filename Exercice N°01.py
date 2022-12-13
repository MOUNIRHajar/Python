n=int(input("donner la longueur du tableau : "))
t1=[]

for j in range(n):
    for x in range(n):
        g=str(input(f"doner le chiffre N{x+1}:"))
        t1.append(g.upper())
    print(len(t1))
    print(t1)

    m = ord(t1[0])
    k = str
    j = 0
    for i in range(1,len(t1)):
        if ord(t1[i])<m:
            k=t1[i]
            j=i
            m=ord(k)

print(f"la lettre a le code askii plus petit est {k} qui est egale {m}")
print("y=",ord('Y'))
print("h=",ord('H'))
print("d=",ord('D'))
print("f=",ord('F'))
t1[j]="*"
print(t1)
t2=[]
t2.append(k)
print(t2)
t2=sorted(t1)
print(t2)
