#Nombre:Marcos Alexis Aguilar Sandoval
#Descripción del script: desplegar una lista de nombres
#Fecha: 03/10/2024
#Tema: U1Ejer02_Marcos Alexis Aguilar Sandoval.py
print ('Manejo de listas ')
print ('Autor: Marcos Alexis Aguilar Sandoval')

print('')
nombres=['Jose','Samuel','Marta','Jocelyn']
print('El tamaño de la lista es: ',len(nombres))
print('El contenido de la lista es: ',nombres)
nombres.pop(1)
nombres.insert(1,'Juaquin')
nombres.append('Juan Miguel')
print(nombres)
print('*'.join(nombres[::-1]))