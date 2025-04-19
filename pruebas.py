def pedir_cadena_texto(cadena:str=None) -> str:
    '''Funcion que le pide al usuario que ingrese un texto, 
    o usa el texto proporcionado por parametro.

    Args:
        cadena (str, opcional): Texto proporcionado.

    Returns:
        str: La cadena de texto proporcionada o ingresada por el usuario.
    '''
    if cadena != None:
        texto = cadena
    else:
        cadena = input("Ingrese un texto: ")
        while cadena == "":
            cadena = input("Error: La cadena no puede estar vacia. Ingrese una cadena valida: ")
        texto = cadena
    return texto

cadena_usuario = pedir_cadena_texto("sdds")  
print(cadena_usuario)
