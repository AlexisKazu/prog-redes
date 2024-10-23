'''
Nombre:Marcos Alexis Aguilar Sandoval
Fecha:20/10/2024
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

aux = set()
lista = []
for num in my_list:
    if num not in aux:
        aux.add(num)
        lista.append(num)
        
print("La lista con elementos únicos:")
print(lista)