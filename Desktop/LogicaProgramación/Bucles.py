# # BUCLE INFINITO
# while True:
#     print("Help.")
    
# tamanio_numero = -999999999

# numero = int(input("Introduce un número o escribe -1 para detener: "))
# while numero != -1:
#     if numero > tamanio_numero:
#         tamanio_numero = numero
#         numero = int(input("Introduce un número o escribe -1 para detener: "))

# # Imprime el número más grande.
# print("El número más grande es:", tamanio_numero)

#==========================================================================================#
# 2 EJERCICIO


# odd_numero = 0
# even_numero = 0

# # Lee el primer número.
# numero = int(input("Introduce un número o escribe 0 para detener: "))

# # 0 termina la ejecución.
# while numero != 0:
#     # Verificar si el número es impar.
#     if numero % 2 == 1:
#         # Incrementar el contador de números impares odd_numero.
#         odd_numero += 1
#     else:
#         # Incrementar el contador de números pares even_numero.
#         even_numero += 1
#     # Leer el siguiente número.
#     numero = int(input("Introduce un número o escribe 0 para detener: "))

# # Imprimir resultados.
# print("Conteo de números impares:", odd_numero)
# print("Conteo de números pares:", even_numero)

#===========================================================================================#
# contador = 999999999999
# while contador != 0:
#     print("Dentro del bucle", contador)
#     contador -= 1
# print("Fuera del bucle", contador)

# ACTIVIDAD AAAAAAAAA#

numero_secreto = 7

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
numero = int(input(""))

while numero != numero_secreto:
    print("!Ja, ja! ¡Estas atrapado en mi buqle!")
    numero(int(input("Ingresa el numero nuevamente:")))
print("!Bien hecho, muggle! Eres libre ahora.")
