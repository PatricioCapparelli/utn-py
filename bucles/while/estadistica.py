'''Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
'''
#Estadisticas
fin = "no"
suma = 0
positivos = 0
negativos = 0
contador_positivos = 0
contador_negativos = 0
contador_total = 0
maximo = None

while fin != "si":
    numero = input("Ingrese un numero: ")

    if numero == "":
        print("Error ingrese el numero nuevamente.")
    else:
        n = int(numero)
        if n > 0:
            positivos += n
            contador_positivos += 1
        elif n < 0:
            negativos += n
            contador_negativos += 1

        if (maximo == None) or (n > maximo):
            maximo = n

        suma += n
        contador_total += 1
        fin = input("¿Desea finalizar? Escriba 'si' para terminar: ")


# Promedio de positivos y porcentaje de negativos.
promedio = positivos / contador_positivos
porcentaje_negativos = (contador_negativos / contador_total) * 100
print(f"La suma de los numeros negativos es: {negativos}")
print(f"La suma de los numeros positivos es: {positivos}")
print(f"La cantidad de numeros negativos ingresados es: {contador_negativos}")
print(f"El promedio de los numeros positivos es: {promedio}")
print(f"El numero maximo de los positivos es: {maximo}")
print(f"El porcentaje de numeros negativos respecto al total ingresado es: {porcentaje_negativos}%")
