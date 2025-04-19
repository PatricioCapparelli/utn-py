# Definimos las variables base
cargo_fijo = 7000
costo_metro_cubico = 200  
total = cargo_fijo 
consumo = int(input("Ingrese su consumo en metros cúbicos: "))
tipo_de_cliente = input("Ingrese el tipo de cliente que es: (Residencial/Comercial/Industrial): ").lower().strip()

bonificacion = 0  
recargo = 0  
descuento_adicional = 0  

# Cálculos según el tipo de cliente
match tipo_de_cliente:
    case "residencial":
        if consumo < 30:
            bonificacion = consumo * costo_metro_cubico * 0.10  # Bonificación del 10%
        elif consumo > 80:
            recargo = consumo * costo_metro_cubico * 0.15  # Recargo del 15%
    
    case "comercial":
        if consumo > 150:
            bonificacion = consumo * costo_metro_cubico * 0.08  # Bonificación del 8%
        elif consumo > 300:
            bonificacion = consumo * costo_metro_cubico * 0.12  # Bonificación del 12%
        elif consumo < 50:
            recargo = consumo * costo_metro_cubico * 0.05  # Recargo del 5%
    
    case "industrial":
        if consumo > 500:
            bonificacion = consumo * costo_metro_cubico * 0.20  # Bonificación del 20%
        elif consumo > 1000:
            bonificacion = consumo * costo_metro_cubico * 0.30  # Bonificación del 30%
        elif consumo < 200:
            recargo = consumo * costo_metro_cubico * 0.10  # Recargo del 10%

    case _:
        print("Tipo de cliente no válido.")
        exit()  # Salir del programa si el tipo de cliente no es válido

# Cálculos finales
subtotal_consumo = consumo * costo_metro_cubico  # Cálculo del costo base por consumo
subtotal_con_ajustes = subtotal_consumo + recargo - bonificacion  # Subtotal con recargos y bonificaciones

# Descuento adicional para cliente residencial si el subtotal sin impuestos es menor a $35,000
if tipo_de_cliente == "residencial" and subtotal_con_ajustes < 35000:
    descuento_adicional = subtotal_con_ajustes * 0.05  # 5% de descuento
    subtotal_con_ajustes -= descuento_adicional

# Cálculo del IVA
iva = subtotal_con_ajustes * 0.21  # 21% de IVA
total_final = subtotal_con_ajustes + iva  # Total final a pagar

# Mostrar los resultados
print("\nFactura del Servicio de Agua Potable")
print(f"Tipo de cliente: {tipo_de_cliente.capitalize()}")
print(f"Cantidad de metros cúbicos consumidos: {consumo} m³")
print(f"Bonificaciones aplicadas: {bonificacion}")
print(f"Recargos aplicados: {recargo}")
print(f"Subtotal (sin impuestos): {subtotal_consumo}")
print(f"Subtotal con recargos y bonificaciones: {subtotal_con_ajustes}")
if descuento_adicional > 0:
    print(f"Descuento adicional (5%) para clientes residenciales: {descuento_adicional}")
print(f"IVA aplicado (21%): {iva}")
print(f"Total final a pagar: {total_final}")
