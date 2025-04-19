# 8

# maximo = None
# minimo = None

# for i in range(10):
#     numero = int(input("Ingrese 10 numeros: "))

#     if maximo == None or numero > maximo:
#         maximo = numero
    
#     if minimo == None or numero < minimo:
#         minimo = numero

# print(f"El numero maximo es: {maximo}")
# print(f"El numero minimo es: {minimo}")

# 9

# suma = 0
# num = int(input("¿cuantos numeros desea ingresar? (minimo 5): "))

# if num < 5:
#     print("Error: Debe ingresar al menos 5 numeros.")
# else:
#     for i in range(num):
#         n = int(input(f"Ingrese el numero {i + 1}: "))
#         suma += n

# promedio = suma / num
# print(f"\nLa suma es: {suma}")
# print(f"El promedio es: {promedio}")

# 10

''' Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.'''

# suma = 0

# cantidad = int(input("Ingrese un numero entre 5 y 10: "))

# while cantidad > 10 or cantidad < 5:
#     cantidad = int(input("Error: ingrese un numero entre 5 y 10: "))

# for i in range(cantidad):
#     n = int(input("Ingrese numeros: "))
#     suma += n

# promedio = suma / cantidad
# print(f"El promedio es: {promedio}")
# print(f"La suma es: {suma}")

# 10

# clave = int(input("Ingresa la calve: "))
# clave_guardada = "10"

# while clave != clave_guardada:
#     clave = int(input("Error, ingrese clave nuevamente: "))
# print("La clave ingresada es correcta")    
    

# 11

# clave = int(input("Ingresa la calve: "))
# clave_guardada = "10"
# contador = 0

# while clave != clave_guardada and contador < 2:
#     clave = int(input("Error, ingrese clave nuevamente: "))
#     contador += 1

# if(clave == int(clave_guardada)):
#     print("La clave ingresada es correcta")
# else:     
#     print("La clave ingresada es incorrecta")

# validaciones 

'''Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
Tendrá intentos indeterminados.'''

# clave = int(input("Ingresa la calve: "))
# clave_guardada = 10
# while clave != clave_guardada:
#     clave = int(input("Error, ingrese clave nuevamente: "))
# print("La clave ingresada es correcta")    
    

'''Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.'''

# nota = int(input("Ingrese una nota: "))

# while nota < 1 or nota > 10:
#     nota = int(input("Error: Ingrese una nota entre 1 y 10: "))

# print(f"La nota ingresada es: {nota}")

# color = input("Ingrese un color: (ROJO, VERDE, AZUL)")

# while color != "rojo" and  color != "verde" and  color != "azul":
#     color = input("Error: el color ingresado no es el correcto. (ROJO, VERDE, AZUL)")

# print(f"El color ingresado es: {color}")

'''Mostrar numeros ascendentes del 1 al 10.'''

# numero = 1

# for numero in range(10):
#     numero += 1
#     print(numero)

'''Mostrar numeros descendentes del 10 al 1.'''

# numero = 1

# for numero in range(11, 1, -1):
#     numero -= 1
#     print(numero)

'''Ingresar un numero, mostrar los numeros del 0 hasta el numero ingresado.'''

# numero = int(input("Ingresa un numero: "))
# cont = 0
# for i in range(numero):
#     cont += 1
#     print(cont)

'''Ingresar un numero y mostrar la tabla de multipicar del mismo.'''

# numero = int(input("Ingresa un numero: "))
# cont = 0

# for i in range(numero):
#     print(f"{numero} x {cont} = {numero * cont}")
#     cont += 1

'''Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
Mostrar la suma y el promedio de todos los números.'''

# numeros = 10
# suma = 0
# acom = 0

# for i in range(numeros):
#     num = int(input("Ingrese un numero: "))
#     if(num == 0):
#         break
#     suma += num
#     acom += 1 

# promedio = (suma / acom) * 100

# print(f"La suma de todos los numeros ingresados es: {suma}")
# print(f"El promedio de todos los numeros es: {promedio}")

'''Imprimir los números múltiplos de 3 entre el 1 y el 10.'''

# for i in range(1, 11):
#     if i % 3 == 0:
#         print(i)

'''Mostrar los números pares que hay desde la unidad hasta el número 50.'''

# numero = int(input("Ingrese un numero: "))

# for i in range(numero, 51):
#     if i % 2 == 0:
#         print(i)

'''Realizar un programa que permita mostrar una pirámide de números.'''

# numero = int(input("Ingrese un número: "))

# for i in range(1, numero + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print() 


'''Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.'''

# numero = int(input("Ingresa un número: "))

# contador = 0

# print(f"Divisores de {numero}:")

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         print(i)
#         contador += 1

# print(f"Cantidad de divisores: {contador}")

'''Determinar si un numero es primo o no'''

# numero = int(input("Ingresa un número: "))

# contador = 0

# print(f"Divisores de {numero}:")

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         print(i)
#         contador += 1

# print(f"Cantidad de divisores: {contador}")

# if(contador == 2):
#     print(f"El numero ingresado es primo. {numero}")
# else:
#     print(f"El numero ingresado no es primo. {numero}")

'''Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado.
Informar cuántos números primos se encontraron.'''

# numero = int(input("Ingrese un número: "))

# primos = 0  

# print(f"Números primos entre 1 y {numero}:")

# for i in range(2, numero + 1):
#     es_primo = True
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             es_primo = False
#             break
#     if es_primo:
#         print(i)
#         primos += 1

# print(f"Se encontraron {primos} números primos.")
