tupla=(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,1,2,3,4,5,6,1,2,3,4,5,1,2,3,4,1,2,3,1,2,1,)
num=int(input("Ingresar un número del 0 al 9"))
if num<0 or num>9:
    print("Error. El número ingresado no cumple con los parametros solicitados")
else:
    n=tupla.count(num)
    print("El número ingresado se repite ", n, " veces en la tupla existente") 
