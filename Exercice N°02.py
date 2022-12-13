num=int(input('taper le nombre de colone:'))
l=[]
for j in range(1,num):
    ch=''.join(map(str,str(11**j)))
    l.append(ch)
l.reverse()
for i in l:
    print(i)
mat=[[0]*num for i in range(num)]
for x in range(len(mat)):
    for i in range(len(mat[0])):
        mat[x][i]=1
        break
for x in range(1,len(mat)):
    for i in range(len(mat[0])):
        mat[x][i]=mat[x-1][i]+mat[x-1][i-1]
for x in range(len(mat)):
    for j in range(x+1):
        print(mat[x][j],end='')
    print()