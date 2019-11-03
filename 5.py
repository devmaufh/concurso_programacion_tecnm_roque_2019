x = input("Ingresa una operacion ")
operadores = []
operandos  = []
for i in x:
    if(i.isnumeric() or i.isalpha()):
        operandos.append(i)
    else:
        if not i.isspace() and i is not "(" and i is not ")": operadores.append(i)

print(x)
print(operandos)
print(operadores)