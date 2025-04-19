
# 1
v = True
# contador = 0;

# while v:
#     if contador == 11:
#         break
#     print(contador)
#     contador += 1

# 2

# contador = 10

# while v:
#     if contador == 0:
#         break
#     print(contador)
#     contador -= 1

# 3

# contador = 0

# while v:
#     if contador == 10:
#         break
#     print(f"{contador} + 1")
#     contador += 1

# 4

# contador = 0
# suma = 0

# while contador <= 10:  
#     if contador % 2 == 0: 
#         suma += contador  
#     contador += 1  

# print(f"La suma de los números pares hasta 10 es: {suma}")


# 5 

# acomulador = 0
# suma = 0

# while acomulador < 5:
#     numero = int(input("Ingresar 5 numeros: "))
#     suma += numero 
#     acomulador += 1

# print(suma)
# promedio = suma / acomulador
# print(promedio)

# 6

# suma = 0
# acomulador = 0

# while v:
#     numero = input("Ingrese los numeros que desee, o 'FIN' para finalizar.")
#     if numero == "FIN":
#         break
#     suma += int(numero)
#     acomulador += 1

# print(f"La suma de los numeros es:  {suma}")
# promedio = suma / acomulador
# print(f"El promedio es: {promedio}")

# 7

# producto_numerico = 1
# suma_numerica = 0

# while v:
#     numero = int(input("Ingrese un numero: "))

#     if numero:
#         if numero < 0:
#             producto_numerico = numero * producto_numerico
#         else:
#             suma_numerica = numero + suma_numerica

#     continuacion = input("Desea continuar? 'SI' | 'NO': ").upper().strip()

#     while continuacion != "SI" and continuacion != "NO":
#         continuacion = input("Error, ingrese un dato valido (SI/NO)").strip().upper()
    
#     if continuacion == "NO":
#         break

# print(f"El producto es: {producto_numerico}")
# print(f"La suma es: {suma_numerica}")

# 8

# acomulador = 0
# maximo = None  
# minimo = None  

while acomulador < 10:  
    numero = int(input("Ingrese un número entero: "))
    acomulador += 1
    
    if maximo == None or numero > maximo:
        maximo = numero
    
    if minimo == None or numero < minimo:
        minimo = numero

print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")

# ANEXO

# 9

# acomulador = 0
# suma = 0

# while acomulador < 5:
#     acomulador += 1

#     numero = int(input("Ingrese 5 numeros para calcular la suma"))
#     suma += numero

# promedio = suma / acomulador
# print(f"La suma de los numeros es: {suma} \n y el promedio es: {promedio}")

# 10

# acomulador = 0
# suma = 0

# while True:
#     if():
#         acomulador += 1

#     numero = int(input("Ingrese 5 numeros para calcular la suma"))
#     suma += numero

# promedio = suma / acomulador
# print(f"La suma de los numeros es: {suma} \n y el promedio es: {promedio}")


