def Palindromo():
    a=input("Escriba la palabra a comprobar: ")
    b="abcdefghijklmnopqsrtuvwxyzñóúíáéü"
    for i in b:
        if i not in a:
            return print(f"{a} No es una palabra")
    if(len(a)%2==0):
        x:bool=True
        for i in range((len(a)//2)):
            if(a[i]!=a[-(i+1)]):
                x=False
                print(str(a)+" NO es palindromo")
                break
        if x:
            print(str(a)+" es palindromo")
    else:
        x:bool=True
        for i in range((len(a)//2)+1):
            if(a[i]!=a[-(i+1)]):
                x=False
                print(str(a)+" NO es palindromo")
                break
        if x:
            print(str(a)+" es palindromo")
Palindromo()