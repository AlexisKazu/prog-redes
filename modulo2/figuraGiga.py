datos = input("")
x, y, z =datos.split()
x=float(x)
y=float(y)
z=float(z)

a= (2*x + y) / z 
b= (y**3)-z
c=((x + 2*y + 3*z)/(z - 2*y - 3*x))+x*x +z**2

print(a*b/c)