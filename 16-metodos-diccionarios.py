diccionario = {
    "nombre": 'Hana',
    "apellido": 'Favela',
    "subs": 1000
}

claves = diccionario.keys() #obtiene llaves o nombres de campos
obtener = diccionario.get("subs") #sirve para obtener el valor de un campo, sin que arroje error de excepcion
diccionario.clear()
diccionario.pop()
print(dir(diccionario))