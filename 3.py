num=int(input("Ingresar un número"))
lista=[(1*num),(2*num),(3*num),(4*num),(5*num),(6*num),(7*num),(8*num),(9*num),(10*num)]
print("La tabla de multiplicar del número ingresado es:")
print(lista)

num1=int(input("Ingresar un número, del cual quieres conocer su tabla de multiplicar"))
num2=int(input("Ingresar un número, que será el límite de la tabla de multiplicar"))
x=0
y=1
lista=[]
while x<num2:
    lista.append(num1*y)
    x=x+1
    y=y+1
print("La tabla de multiplicar del número ingresado ", num1, " hasta el número ", num2, " es:")
print(lista)
