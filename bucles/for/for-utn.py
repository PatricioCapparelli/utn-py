#For
'''Mostrar numeros ascendentes del 1 al 10.'''

numero = 1

for numero in range(10):
    numero += 1
    print(numero)

'''Mostrar numeros descendentes del 10 al 1.'''

numero = 1

for numero in range(11, 1, -1):
    numero -= 1
    print(numero)

'''Ingresar un numero, mostrar los numeros del 0 hasta el numero ingresado.'''

numero = int(input("Ingresa un numero: "))
cont = 0
print(cont)
for i in range(numero):
    cont += 1
    print(cont)

'''Ingresar un numero y mostrar la tabla de multipicar del mismo.'''

numero = int(input("Ingresa un numero: "))
cont = 0

for i in range(numero + 1):
    print(f"{numero} x {cont} = {numero * cont}")
    cont += 1

'''Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
Mostrar la suma y el promedio de todos los números.'''

numeros = 10
suma = 0
acom = 0

for i in range(numeros):
    num = int(input("Ingrese un numero: "))
    if(num == 0):
        break
    suma += num
    acom += 1 

promedio = (suma / acom) * 100

print(f"La suma de todos los numeros ingresados es: {suma}")
print(f"El promedio de todos los numeros es: {promedio}")

'''Imprimir los números múltiplos de 3 entre el 1 y el 10.'''

for i in range(1, 11):
    if i % 3 == 0:
        print(i)

'''Mostrar los números pares que hay desde la unidad hasta el número 50.'''

numero = int(input("Ingrese un numero: "))

for i in range(numero, 51):
    if i % 2 == 0:
        print(i)

'''Realizar un programa que permita mostrar una pirámide de números.'''

numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print() 


'''Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.'''

numero = int(input("Ingresa un numero: "))
contador = 0

print(f"Divisores de {numero}:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        contador += 1

print(f"Cantidad de divisores: {contador}")

'''Determinar si un numero es primo o no'''

numero = int(input("Ingresa un numero: "))
contador = 0

print(f"Divisores de {numero}:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        contador += 1

print(f"Cantidad de divisores: {contador}")

if(contador == 2):
    print(f"El numero ingresado es primo. {numero}")
else:
    print(f"El numero ingresado no es primo. {numero}")

'''Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado.
Informar cuántos números primos se encontraron.'''

numero = int(input("Ingrese un numero: "))
primos = 0  

print(f"Numeros primos entre 1 y {numero}:")

for i in range(2, numero + 1):
    es_primo = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i)
        primos += 1

print(f"Se encontraron {primos} numeros primos.")
