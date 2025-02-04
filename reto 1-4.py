def separar(a:list):
    b=[]
    c=0
    try:
        for i in range(len(a)):
            if(a[i]=="," or  a[i]==" "):
                b.append(int(a[c:i]))
                c=i+1 
            elif(len(a)-1==i):
                b.append(int(a[c:]))
        return b
    except  ValueError as error:
        return print(f"{a[i-1]} No es un número ") 
def sum(a:list):
    b=[]
    for i in range(len(a)-1):
        b.append(a[i]+a[i+1])
    return max(b)

a=input("Ingresar uma lista de numeros: ")
x=sum(separar(a))
#print("La maxima suma de dos cifras seguidas es: "+str(x))
print(x)