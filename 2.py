meses=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
num=int(input("Ingresa un número"))
if num>=0 and num<12:
    print(meses[num])
else:
    print("Error")

