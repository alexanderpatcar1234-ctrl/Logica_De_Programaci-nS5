# EJEMPLO 01
# Se leen dos números
Numero1 = int(input("Ingresa el primer número: "))
Numero2 = int(input("Ingresa el segundo número: "))
# Elige el número más grande
if Numero1 > Numero2:
    Tamaño_numero = Numero1
else:
    Tamaño_numero = Numero2
# Imprime el resultado
print("El número más grande es:", Tamaño_numero)



# EJEMPLO 02
# Se leen dos números
Numero1 = int(input("Ingresa el primer número: "))
Numero2 = int(input("Ingresa el segundo número: "))
# Elige el número más grande
if Numero1 > Numero2:Tamaño_numero = Numero1
else:Tamaño_numero = Numero2
# Imprime el resultado
print("El número más grande es:", Tamaño_numero)




# EJEMPLO 03
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




#EJERCICIP 01
planta = input("Introduce el nombre de la flor: ")

if planta == "espatifilo":
    print("Si, ¡El espatifilo es la mejor planta de todos los tiempos!")
    exit()
if planta == "ESPATIFILO":
    print("Si, ¡El Espatifilio es la mejor planta de todos")
    exit()
elif planta == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
    exit()
else:
    print("¡ESPATIFILIO!, ¡No", planta + "!")
    
    
    

#INFO ADICIONAL
# Se leen tres números.
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
numero4 = int(input("Ingresa el cuarto número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.

Tamaño_numero = max(numero1, numero2, numero3, numero4)
print("El número más grande es:", Tamaño_numero)
