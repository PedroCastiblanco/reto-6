def separar(a:list):
    b=[]
    c=0
    d=1
    a=a[2:-1]
    #print(a)
    for i in range(len(a)):
        if(a[i]=='"'):
            if d==1 and a[c:i]!="":
                b.append(a[c:i])
                c=i+3 
                d=d*-1
            if d==-1:
                d=d*-1
    return b

def Acronimo(a:list):
    b,z=[],[]
    for i in a:
        b.append(sorted(i))
    for i in range(len(a)):
        c=[]
        for x in range(len(a)):
            if b[i]==b[x] and a[x] not in c and i!=x:
                c.append(a[x])
                b[x]=a[x]
        if len(c)!=0 and c not in z:
             c.insert(0,a[i])
             #c.append()
             b[i]=a[i]
             z.append(c)
    return z

x=separar(input("lista: "))
print(x)
print(Acronimo(x))
