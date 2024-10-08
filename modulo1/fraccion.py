


data = input("")
x, y = data.split() 
x=int(x)
y=int(y)
coc= x//y
res=x%y
if res==0:
    print(coc)
else:
    print ( f"{coc} {res}/{y}")

#print(x + y)
#print(x*y)#multiplicacion
#print(x**y)#potencia
#print(x/y)#divicion
#print(x%y)#reciduo
#print(x//y)#constante