# tec_ia = "IA"
# tec_rv = "RV/RA"
# tec_iot = "IOT"

# nombre = None
# empleados = 0
# empleados_masc = 0
# empleados_sin_ia = 0
# edad_de_empleado_max = None
# nombre_del_mayor = None
# tecnologia_elegida_mayor = None

# while empleados < 10:

#     nombre = input("Nombre: ")
#     edad = int(input("Edad: "))

#     while edad < 18:
#         edad = int(input("Debe ser mayor de 18 años o mas!"))

#     genero = input("Genero: (MASCULINO, FEMENINO, OTRO)").lower()

#     tecnologia_elegida = input("Elige una tecnologia: (IA, RV/RA, IOT)").upper()

#     while tecnologia_elegida != tec_ia and tecnologia_elegida !=    tec_rv and tecnologia_elegida != tec_iot:
#         tecnologia_elegida = input("Ingrese una tecnologia valida: (IA, RV/RA, IOT)")

#     if(genero == "masculino" and (tecnologia_elegida == tec_iot or tecnologia_elegida == tec_rv) and (edad >= 25 and edad <= 50)):
#         empleados_masc += 1

#     if(tecnologia_elegida != tec_ia):
#         if tecnologia_elegida != tec_ia and genero != "femenino" and 33 <= edad <= 40:
#             empleados_sin_ia += 1

#     if(genero == "masculino" and (edad_de_empleado_max is None or edad_de_empleado_max < edad)):
#         nombre_del_mayor = nombre
#         edad_de_empleado_max = edad
#         tecnologia_elegida_mayor = tecnologia_elegida

#     empleados += 1

# porcentaje = (empleados_sin_ia / empleados) * 100
# print(f"La cantidad de empleados masculinos que votaron por IOT o IA, cuya edad esta entre 25 y 50 años es: {empleados_masc} ")
# print(f"El empleado mas grande es: {nombre_del_mayor}, edad: {edad_de_empleado_max}, tecnologia: {tecnologia_elegida_mayor}")
# print(f"Porcentaje de empleados que no votaron por IA, género no femenino y edad entre 33 y 40 años: {porcentaje:.2f}%")



