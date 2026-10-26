# LA SENTECIA ELIF
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


# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if Numero1 > Numero2: Tamaño_numero = Numero1
else: Tamaño_numero = Numero2

# Imprime el resultado
print("El número más grande es:", Tamaño_numero)


# Se leen tres números
Numero1 = int(input("Ingresa el primer número: "))
Numero2 = int(input("Ingresa el segundo número: "))
Numero3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
Tamaño_numero = Numero1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > Tamaño_numero:
    Tamaño_numero = Numero2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if Numero3 > Tamaño_numero:
    Tamaño_numero = Numero3

# Imprime el resultado.
print("El número más grande es:", Tamaño_numero)




