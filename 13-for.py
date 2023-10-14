lenguajes = ["phyton", "ruby", "php", "sql", "java"]
for lengua in lenguajes:
    print(lengua)

#recorriendo 2 listas simultaneas

comida = ['arroz', 'huevo', 'pescado']
ejercicio = ['sentadilla', 'curls', 'flexiones']

for a, b in zip(comida, ejercicio):
    print(a)
    print(b)

#recorre lista obteniendo el indice de cada elemento
for a in enumerate(comida):
    print(a)

#SE puede usar el ELSE dentro de un FOR, como si fuera un IF

#usar el termino CONTINUE dentro del for para saltarse una sentencia y despues continuar con el bucle normal

#usar el termino BREAK para de plano terminar con la ejecucion del bucle

#FOR en una sola linea de codigo
numeros =  [2,4,6,8]
numeros_duplex = [x*2 for x in numeros]
