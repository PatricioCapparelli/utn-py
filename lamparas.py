'''
Todas las lámparas están  al mismo precio de $800 pesos final.
        A.    Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
        B.    Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" 
        se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
        C.    Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o 
        “Felipelamparas_nuevas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
        D.    Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"
        el descuento es del 15%, si es  “Felipelamparas_nuevas” se hace un descuento del 10 % y 
        si es de otra marca un 5%.
        E.    Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''
# lamparas = 800
# lamparas_nuevas = 0
# lamparas_compradas = int(input("Ingrese cuantas lamparas desea comprar: "))
# marca_de_lamparas_nuevas = input("Ingrese que marca desea comprar ('ArgentinaLuz' o 'Felipelamparas_nuevas'): ")


# precio_final = lamparas * lamparas_compradas


# if lamparas_compradas >= 6:
#     descuento = (precio_final * 50) / 100
#     precio_final -= descuento
#     print(f"Compra finalizada! Se te hizo un descuento del 50%, precio final: {precio_final}")
# elif lamparas_compradas == 5:
#     if marca_de_lamparas_nuevas == "ArgentinaLuz":
#         descuento = (precio_final * 40) / 100
#         precio_final -= descuento
#         print(f"Compra finalizada! Se te hizo un descuento del 40%, precio final: {precio_final}")
#     else:
#         descuento = (precio_final * 30) / 100
#         precio_final -= descuento
#         print(f"Compra finalizada! Se te hizo un descuento del 30%, precio final: {precio_final}")
# elif lamparas_compradas == 4:
#     if marca_de_lamparas_nuevas == "ArgentinaLuz" or marca_de_lamparas_nuevas == "Felipelamparas_nuevas":
#         descuento = (precio_final * 25) / 100
#         precio_final -= descuento
#         print(f"Compra finalizada! Se te hizo un descuento del 25%, precio final: {precio_final}")
#     else:
#         descuento = (precio_final * 20) / 100
#         precio_final -= descuento
#         print(f"Compra finalizada! Se te hizo un descuento del 20%, precio final: {precio_final}")
# elif lamparas_compradas == 3:
#     if marca_de_lamparas_nuevas == "ArgentinaLuz":
#         descuento = (precio_final * 15) / 100
#         precio_final -= descuento
#         print(f"Compra finalizada! Se te hizo un descuento del 15%, precio final: {precio_final}")
#     elif marca_de_lamparas_nuevas == "Felipelamparas_nuevas":
#         descuento = (precio_final * 10) / 100
#         precio_final -= descuento
#         print(f"Compra finalizada! Se te hizo un descuento del 10%, precio final: {precio_final}")
#     else:
#         descuento = (precio_final * 5) / 100
#         precio_final -= descuento
#         print(f"Compra finalizada! Se te hizo un descuento del 5%, precio final: {precio_final}")

# # Descuento adicional si el precio final supera los $4000
# if precio_final > 4000:
#     descuento_adicional = (precio_final * 5) / 100
#     precio_final -= descuento_adicional
#     print(f"Compra finalizada! Se te hizo un descuento adicional del 5%, precio final: {precio_final}")
# else:
#     print(f"Compra finalizada, precio final sin descuento adicional: {precio_final}")
