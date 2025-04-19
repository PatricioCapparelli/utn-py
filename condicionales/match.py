viajes = input("Ingrese una estacion del anio para ver donde se puede viajar.").lower().strip()

match viajes:
    case "invierno":
        print("Solo se viaja a bariloche")
    case "verano":
        print("Se viaja a Mar del Plata y Cataratas")
    case "otonio":
        print("Se viaja a todos los lugares")
    case "primavera":
        print("Se viaja a todos los lugares menos Bariloche")
    case _:
        print("No elegiste una estacion valida.")
        exit()