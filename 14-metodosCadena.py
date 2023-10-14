#DIR nos sirve para conocer todos los metodos que podemos usar en una variable.
#print(dir('hola mundo'))
texto = '1 2 3 3'

mayuscula = texto.upper()

esNumero = texto.isnumeric()
esTexto = texto.isalpha()
cuenta = texto.count('3')
longitud = len(texto)
buscar = texto.find('3')
empieza = texto.startswith('1')
reemplaza = texto.replace('12', '44')
#SPLIT crea una lista con el caracter que le indiquemos, por ejemplo una coma o un espacio
separa = texto.split(' ')
print(separa[3])

