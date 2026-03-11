u=1.0
u_salvat=1.0
p10=0
while(1.0+u)!=1.0:
    u_salvat=u
    p10+=1
    u=10**(-p10)
print(u)
print(f"Cel mai mic m: {p10- 1}")
print(f"Valoarea u: 10^-{p10 - 1}")