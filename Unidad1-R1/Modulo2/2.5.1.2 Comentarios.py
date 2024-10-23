'''
Autor:Marcos Alexis Aguilar Sandoval
Fecha:20/10/2024
'''
hour = int (input ("Hora de inicio (horas) :") )
ming = int (input ("Minuto de inicio (minutos): ") )
dura = int (input ("Duración del evento (minutos): "))

total = ming + dura
cociente = total // 60
residuo = total % 60
hour += cociente


print (hour,':', residuo)