lista=[]
num=1
while num!=0:
    num=int(input("Ingresa un número"))
    lista.append(num)
print(lista)
n=(len(lista)-1)
for k in range (n):
    for x in range (n):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
print("lista ordenada de menor a mayor:")
print(lista)

        
        
