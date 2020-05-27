tupla=(432,7865,432,6754,231,8643,234,8,6,654,)
mayor=tupla[0]
for x in range (1,9):
    if tupla[x]>mayor:
        mayor=tupla[x]
print("El número mayor de la tupla es:")
print(mayor)

for x in range (1,9):
    if tupla[x]<menor:
        menor=tupla[x]
print("El número menor de la tupla es:")
print(menor)
