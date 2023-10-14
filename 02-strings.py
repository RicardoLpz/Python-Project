texto = "hola mundo"
print(texto.upper())
print(texto.lower())
print(texto.find("mun"))
print(texto.replace("mundo", "tierra"))

nuevotexto = (texto.replace("mundo", "tierra"))
print(texto, nuevotexto)
print("mundo" in texto)