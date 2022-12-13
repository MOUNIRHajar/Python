import string
utilisateur=int(input("bonjour dans notre programme  si tu veux crypter votre message écrire 1 Et si vous voulez le décoder écrire 2 : "))
def codage():
    cod=input("votre texte:")
    clef=input("votre cle:")
    mss=""
    ind=0
    for i in cod:
        if i in string.ascii_lowercase:
            off=ord(clef[ind])-ord('a')
            enk=chr((ord(i)-ord('a')+off)%26 + ord('a')) 
            mss=mss+enk
            ind=(ind+1) % len(clef)
        else:
            mss=mss+i
    print("votre message à coder :"+ mss)

def decodage():
    clef=input("votre cle:")
    mss=input("votre message:")
    cod=""
    ind=0
    for i in mss:
        if i in string.ascii_lowercase:
            off=ord(clef[ind])-ord('a')
            enk=ord(i)-ord('a')-off
            if enk < 0:
                enk=enk+26
            cc=chr(enk+ord('a'))
            cod=cod+cc
            ind=(ind+1) % len(clef)
        else:
            cod=cod+i
    print("vote code à décoder:{}".format(cod))
if utilisateur==1:
    codage()
elif utilisateur==2:
    decodage()
