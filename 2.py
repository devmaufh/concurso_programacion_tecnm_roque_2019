n1 = int(input("Ingresa el primero numero "))
n2 = int(input("Ingresa el segundo numero "))
aux = " " 
if n1 > n2: print("Error")
else:
    for i in range(n1, n2+1):
        aux = aux + str(i) + " "
        print(aux)
