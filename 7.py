cadena=input("Ingresa un cadena de caracteres")
lista=[]
y=len(cadena)
x=0
while x<y:
    lista.append(cadena[x])
    x=x+1
print(lista)

contador=0
y=(len(lista)-1)
print(y)
while contador<y:
    n = lista.count(lista[contador])
    if n>1:
        lista.remove(lista[contador])
        contador=contador-1
        y=y-1
    contador=contador+1
print(lista)


cadena=input("Ingresa un cadena de caracteres")
lista=[]
y=len(cadena)
x=0
while x<y:
    lista.append(cadena[x])
    x=x+1

lista = list(dict.fromkeys(lista))
print(lista)
