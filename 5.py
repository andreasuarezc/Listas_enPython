lista=[]
x=1
while x!=0:
    x=int(input("Ingresar un número"))
    lista.append(x)
print(lista)
n=(len(lista)-1)
for k in range (n):
    for x in range (n):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux

print("La lista ordenada de mayor a menor es:")
print(lista)
