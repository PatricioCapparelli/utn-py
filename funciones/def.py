# Calculadora
def calculadora() -> int:
    '''Esta funcion devuelve el resultado de una operacion matematica de tipo suma, resta, multiplicacion, division.
        Returns:
            int: Devuelve la operacion matematica entre estos dos numeros.
    '''
    flag = False
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    
    while flag != True:
        operacion = input("Ingrese una operacion: '*', '/', '-', '+': " )
        match operacion:
            case "*":
                result = a * b
                flag = True
            case "/":
                result = a / b
                flag = True
            case "+":
                result = a + b
                flag = True
            case "-":
                result = a - b
                flag = True
            case _:
                print("Ingrese una operacion valida!")
    return print(result)

calculadora()

#1
def pedir_numero_entero() -> int:
    '''Funcion que le pide un numero entero al usuario.
    Returns:
        int: Numero entero que ingreso el usuario.
    '''
    numero = int(input("Ingrese un numero: "))
    return numero

numero = pedir_numero_entero()
print(numero)

#2
def pedir_numero_decimal() -> float:
    '''Funcion que le pide un numero decimal al usuario.
    Returns:
        float: Numero decimal que ingreso el usuario
    '''
    numero = float(input("Ingrese un numero decimal: "))
    return numero

numero = pedir_numero_decimal()
print(numero)

#3
def pedir_cadena_texto() -> str:
    '''Funcion que le pide al usuario que ingrese un texto.
        Returns:
            str: Devuelve la cadena de texto ingresada por el usuario.
    '''
    cadena = input("Ingrese una cadena de texto: ")
    return cadena

cadena = pedir_cadena_texto()
print(cadena)

#4
def calcular_area_rectangulo() -> float:
    '''Funcion que calcula el area de un rectangulo calculando la base por la altura.
        Returns:
            float: Devuelve la multiplicacion de estos dos numeros, base por altura.
    '''
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))

    area = base * altura
    return area


calc = calcular_area_rectangulo()
print(calc)

#5
def calcular_area_circulo(radio:float) -> float:
    '''Funcion que calcula el area de un circulo a travez del radio.
        Args:
            float: Numero decimal
        Returns:
            float: Devuelve el calculo del radio .
    '''
    radio = float(input("Ingrese el radio del circulo: "))
    
    area = 3.14*(radio**2)
    return area

calc = calcular_area_circulo()
print(calc)

print()

# 6
def verificar_numero_par_impar(n:int) -> None:
    '''Funcion que verifica si un numero es par o impar
        Args:
            n (int): Numero
    '''
    if n % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

verificar_numero_par_impar(5)

# 7
def verificar_numero_par_impar(n:int) -> bool:
    '''Funcion que verifica si un numero es par o impar, devuelve VERDADERO si es par y FALSO si es impar.
        Args:
            n (int): numero
        
        Returns:
            bool: Devuelve valor booleano de la verificacion.
    '''
    verificacion = False
    if n % 2 == 0:
        verificacion = True

    return verificacion

n = verificar_numero_par_impar(2)
print(n)

# 8 / 1
def encontrar_maximo(a:int, b:int, c:int) -> int:
    '''Esta funcion recibe tres numeros enteros y devuelve el numero mas grande de los tres.
        Args:
            a (int): numero
            b (int): numero
            c (int): numero
        
        Returns:
            int: Devuelve el numero mas grande entre estos tres numeros.
    '''

    #Determino si los tres numeros son iguales.
    if a == b and a == c:
        numero_mas_grande = a
    #Determino si los tres numeros no son iguales
    elif a != b and a != c and b != c:
        if b < a and a > c:
            numero_mas_grande = a
        elif a < b and b > c:
            numero_mas_grande = b
        else:
            numero_mas_grande = c
    #Determino si dos numeros son iguales y son los mas grandes.
    elif (a == b and a > c) or (a == c and a > b):
        numero_mas_grande = a
    elif (b == a and b > c) or (b == c and b > a):
        numero_mas_grande = b
    elif (c == a and c > b) or (c == b and c > a):
        numero_mas_grande = c
    #Determino si dos numeros son iguales y son los mas chicos.
    elif a == b and c > a:
        numero_mas_grande = c
    elif a == c and b > a:
        numero_mas_grande = b
    else:
        numero_mas_grande = a

    return numero_mas_grande

result = encontrar_maximo(4, 2, 2)
print(result)


#8 / 2
def encontrar_maximo(a:int, b:int, c:int)->int:
    '''Esta funcion recibe tres numeros enteros y devuelve el numero mas grande de los tres.
        Args:
            a (int): numero
            b (int): numero
            c (int): numero
        
        Returns:
            int: Devuelve el numero mas grande entre estos tres numeros.
    '''

    #Determino si los tres numeros son iguales.
    if a == b and a == c:
        numero_mas_grande = a
    else:
        if b < a and a > c:
            numero_mas_grande = a
        elif a < b and b > c:
            numero_mas_grande = b
        elif a < c and c > b:
            numero_mas_grande = c
        #Determino si dos numeros son iguales y el mayor es uno de los iguales
        elif (a == b and a > c) or (a == c and a > b):
            numero_mas_grande = a
        elif (b == a and b > a) or (b == c and b > c):
            numero_mas_grande = b
        elif (c == a and c > b) or (c == b and c > a):
            numero_mas_grande = c
        #Determino si dos numeros son iguales y el mayor es el diferente
        elif a == b and c > a:
            numero_mas_grande = c
        elif a == c and b > a:
            numero_mas_grande = b
        else:
            numero_mas_grande = a

    return numero_mas_grande

result = encontrar_maximo(4, 2, 2)
print(result)

#9
def calcular_potencia(base:int, exponente:int) -> int:
    '''Funcion que se encarga de calcular la potencia de un numero.

        Args:
            base (int): numero
            exponente (int): numero
        
        Returns:
            int: Devuelve la potencia entre estos dos numeros.
    '''
    result = base ** exponente
    return result

potencia = calcular_potencia(2, 3)
print(potencia)

#10
def es_primo(numero:int) -> bool:
    '''Funcion que se encarga de verificar si un numero es primo o no.

        Args:
            numero (int): numero
        
        Returns:
            bool: Devuelve el dato booleano de la verificacion del numero.
    '''
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

#11
def mostrar_numeros_primos(numero:int) -> int:
    '''Funcion que recibe un numero y muestra todos los numeros primos encontrados hasta ese numero y devuelve la cantidad total de numeros primos.

        Args:
            numero (int): Numero
        
        Returns:
            int: Devuelve la cantidad de numeros primos encontrados.
    '''
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

    return primos

#12
def imprimir_tabla_multiplicar(numero:int, inicio:int=1, fin:int=10) -> None:
    '''Funcion que imprime la tabla de multiplicar del numero ingresado por parametro, .

        Args:
            numero (int): Numero a calcular
            inicio (int): Numero del inicio del rango 
            fin (int): Numero del final del rango
        
        Returns:
            None
    '''
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")


#13 / 1
def pedir_numero_entero(n:int=None) -> int:
    '''Funcion que retorna un numero entero. Puede recibirlo como parametro
    o pedirlo al usuario si no se proporciona.
    Args:
        n (int, opcional): numero
    Returns:
        int: Numero entero que ingreso el usuario.
    '''
    if n != None:
        resultado = n 
    else:
        numero = input("Ingrese un numero: ")
        while numero == "":
            numero = input("Error: Ingrese un numero valido: ")
        resultado = int(numero)
    return resultado

#13 / 2
def pedir_numero_decimal(n:float=None) -> float:
    '''Funcion que retorna un numero decimal. Puede recibirlo como parametro
    o pedirlo al usuario si no se proporciona.

    Args:
        n (float, opcional): Numero decimal 

    Returns:
        float: Numero decimal recibido o ingresado por el usuario.
    '''
    if n != None:
        resultado = n
    else:
        numero = input("Ingrese un numero decimal: ")
        while numero == "":
            numero = input("Error: Ingrese un numero valido: ")
        resultado = float(numero)
    return resultado

#13 / 3
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

