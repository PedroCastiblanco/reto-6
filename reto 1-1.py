def Calcu():
        
    a=input("Ingrese los digitos y el simbolo de la operacion: ")
    b=[]
    c=0
    try:
        for i in range(len(a)):
            if(a[i]=="," ):
                b.append(int(a[c:i]))
                c=i+1
            elif(len(a)-1==i):
                b.append(a[-2])
    except ValueError as error:
        return print(f"{a[i-1]} No es un número ") 
    except IndexError as e:
        return print('El formato de entrada es: numero1,numero2,"operador"') 
    #print(b)
    try:
        if len(b)!=3:
            return print('El formato de entrada es: numero1,numero2,"operador"') 
        if b[-1]=="+":
            return print("La suma entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]+b[1]))
        if b[-1]=="-":
            return print("La resta entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]-b[1]))
        if b[-1]=="*":
            return print("La multiplicación entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]*b[1]))
        if b[-1]=="/":
            return print("La division entre "+str(b[0])+" y "+str(b[1])+" es: "+str(b[0]/b[1]))
        else:
            if(b[-1]==","):
                return print('El formato de entrada es: numero1,numero2,"operador"')
            return print(f"No es un operador valido: { b[-1] }")
    except ZeroDivisionError as e:
        print(f"No se puede dividir por 0") 
    except IndexError as e:
        print('El formato de entrada es: numero1,numero2,"operador"') 


Calcu()




