import math
import time
import random


def reducere_intervalpi2(x):

    k = round(x / math.pi)
    bool semn=False   #false=pozitiv
    rest = x - (k * math.pi)
    if rest<0:
        semn=True
        rest=-rest  #schimba rest in -rest pt antisimetrie
    return rest,semn


def my_tan_core(x):
    c1=0.33333333333333333
    c2=0.133333333333333333
    c3=0.053968253968254
    c4=0.0218694885361552
    x_2=x*x
    x_3=x_2 *x
    x_4=x_2*x_2
    x_6=x_3*x_3
    p=c1+c2*x_2+c3*x_4+c4*x_6
    return p

def my_tan(x):
    x,semn=reducere_intervalpi2(x)

    if (x==math.pi/2):return 0
    if semn==True:
        if x>=math.pi/4:
            y=math.pi/2-x
            p=my_tan_core(y)
            rezultat=-1/(y+y*y*y*p)
        else:
            p=my_tan_core(x)
            rezultat=-(x+x*x*x*p)
    else:
        if x>=math.pi/4:
            y=math.pi/2-x
            p=my_tan_core(y)
            rezultat=1/(y+y*y*y*p)
        else:
            p=my_tan_core(x)
            rezultat=(x+x*x*x*p)
    return rezultat

numere=10000
valori_test = [random.uniform(-math.pi/2, math.pi/2) for _ in range(numere)]
start_my = time.perf_counter()
for x in valori_test:
    _ = my_tan(x)
stop_my = time.perf_counter()
timp_my_tan = stop_my - start_my

start_math = time.perf_counter()
for x in valori_test:
    _ = math.tan(x)
stop_math = time.perf_counter()
timp_math_tan = stop_math - start_math

eroare_totala = 0
for x in valori_test:
    eroare_totala += abs(math.tan(x) - my_tan(x))

print("Timpul my_tan:",timp_my_tan)
print("Timpul math.tan:",timp_math_tan)
print("Eroarea totală:",eroare_totala)


