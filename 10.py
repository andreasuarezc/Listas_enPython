dictionary = {}
respuesta = "si"
while respuesta=="si":
    nombreUsuario=input("Ingresa el nombre de Usuario")
    telefono=input("Ingresa el teléfono")
    dictionary[nombreUsuario]=telefono
    respuesta=input("¿Deseas ingresar otro usuario?. Responde si/no:")
print(dictionary)
    
