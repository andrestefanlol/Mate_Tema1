u=10**(-15)
x=1.0
y=u/10
z=u/10
#verifica daca e precizie masina
#if (1.0+u)!=1.0 and (1.0+(u/10))==1.0:
#    print('da')
#else:
#    print('nu')
a=(x+y)+z
b=x+(y+z)
if a==b:
    print('este adunarea asociativa')
else:print('Nu este adunarea asociativa')

#verific daca acele numere au inmultirea asociativa
#a=(x*y)*z
#b=x*(y*z)
#if a==b:
#    print('ok')
#else:print('Nu ok')

x_m=1.0
y_m=1.0
z_m=1.0
p=0
while ((x_m*y_m)*z_m)==(x_m*(y_m*z_m)):
    p+=1
    x_m=10.0**p
    y_m=x_m
    z_m=10.0**(-p)
#10^-5 nu se poate scrie in baza 2 corect
print(x_m,y_m,z_m)

