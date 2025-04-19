# while

#1

# clave = "utn"
# clave_user = input("Ingrese la clave del usuario: ")

# while clave_user != clave:
#     clave_user = input("Error: clave invalida. Ingrese nuevamente la clave: ")

# input("Inicio de usuario exitoso!")

#2

# clave = "utn"
# clave_user = input("Ingrese la clave del usuario: ")
# intentos = 0
# flag = 0

# while clave_user != clave and intentos < 3:
#     clave_user = input("Error: clave invalida. Ingrese nuevamente la clave: ")
#     if(clave_user == clave):
#         break
#     intentos += 1

# if(intentos >= 3):
#         print("Superaste el maximo de intentos posibles!.")
#         flag += 1

# if(flag != 1):
#     print("Ingreso de usuario exitoso!")
# else:
#     print("No pudiste ingresar a tu cuenta, debido a que superaste el maximo de intentos posibles.")
    

#3

# nota = int(input("Ingrese una nota: "))

# while nota > 10 or nota < 1:
#     nota = int(input("Error: Ingrese nuevamente la nota: "))

# print(f"La nota ingresada es: {nota}")

#4

# color = input("Ingrese un color (ROJO, AZUL, VERDE): ").lower()

# while color != "verde" and color != "rojo" and color != "azul":
#     color = input("Error: Ingrese un color valido (ROJO, AZUL, VERDE): ")

# print(f"El color ingresado es: {color}")

'''Integrador Validaciones'''

apellido = input("Ingrese su apellido: ")

edad = int(input("Ingrese su edad (entre 18 y 90): "))
while edad < 18 or edad > 90:
    edad = int(input("Error: La edad debe estar entre 18 y 90 años. Ingrese nuevamente: "))

estado_civil = input("Ingrese su estado civil (Soltero, Casado, Divorciado, Viudo): ").strip().capitalize()
estados_validos = ["Soltero", "Casado", "Divorciado", "Viudo"]

while estado_civil not in estados_validos:
    estado_civil = input("Error: Ingrese un estado civil valido (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ").strip().capitalize()

num_legajo = input("Ingrese su número de legajo (4 cifras sin ceros a la izquierda): ")
while not (num_legajo.isdigit() and len(num_legajo) == 4 and num_legajo[0] != '0'):
    num_legajo = input("Error: El numero de legajo debe ser de 4 cifras numericas y no puede comenzar con 0. Intente nuevamente: ")

print("\n--- Datos ingresados correctamente ---")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Número de legajo: {num_legajo}")

print("hola")
# a = int(input("Ingrese un numero: "))
# b = int(input("Ingrese otro numero: "))

def suma(a:int=20, b:int=50) -> int:
    '''Esta funcion devuelve la suma de dos numeros.'''

    resultado = a + b
    return resultado

resultado_suma = suma(1,3)

print(type(resultado_suma))








