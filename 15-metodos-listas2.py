lista = list([23, 'Hana', 'Noble', 'Tierna'])
lista.append(12) #agrega elemento en cualquier posicion a diferencia de INSERT que agrega segun el indice
lista.extend([45, 67]) #agrega elementos multiples en forma de sublista
lista.pop(5) #elimina elemento, usar indice -1 para eliminar el ultimo elemento
lista.remove('Tierna') #elimina por nombre de busqueda
lista.sort() #ordena de forma ascendente
lista.reverse() #ordena de forma descendente o al reves
lista.clear() 

print(lista)