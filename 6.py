cadena=input("Ingresa una cadena de texto")
lista=[]
y=(len(cadena))
x=0
while x<y:
    if cadena[x]!=" ":
        lista.append(cadena[x])
    x=x+1
print(lista)
