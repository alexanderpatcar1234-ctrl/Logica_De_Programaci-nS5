# Se leen tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero4 = int(input("Ingresa el cuarto número: "))
# Asumimos temporalmente que el primer número
# numero1=4
# numero2=7
# numero3=15
# numero4=1
Tamaño_numero = numero1
if numero2 > Tamaño_numero:
    Tamaño_numero = numero2
    
if numero3 > Tamaño_numero:
    Tamaño_numero = numero3
    
if numero4 > Tamaño_numero:
    Tamaño_numero = numero4
# Imprime el resultado.
print("El número más grande es:", Tamaño_numero)