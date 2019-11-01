import math
def factorial(n):
    if n == 0: return 1 
    return factorial(n-1) * n
x = int(input("Ingresa el valor de x "))	
res = 1.0
for i in range(1, x+1):
    potencia = 1
    for j in (1, i):
        potencia = math.pow(x,j)
    res = res + (potencia / factorial(i))
print(res)