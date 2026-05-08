def calcular_suma(numero_uno:int,numero_dos:int) -> int:#Firma de la función (1.Definición)
    """Realizar la suma entre dos numeros

    Args:
        numero_uno (int): Primer numero ingresado
        numero_dos (int): Segundo numero ingresado

    Returns:
        int: Resultado de la suma
    """
    if type(numero_uno) == int and type(numero_dos) == int: 
        resultado = numero_uno + numero_dos 
    else:
        resultado = "Error desconocido"
    return resultado

def calcular_resta(numero_uno:int,numero_dos:int) -> int:
    """Realizar la resta entre dos numeros

    Args:
        numero_uno (int): Primer numero ingresado
        numero_dos (int): Segundo numero ingresado

    Returns:
        int: Resultado de la resta
    """
    resultado = numero_uno - numero_dos 
    return resultado

def calcular_multiplicacion(numero_uno:int,numero_dos:int) -> int:
    """Realizar el producto entre dos numeros

    Args:
        numero_uno (int): Primer numero ingresado
        numero_dos (int): Segundo numero ingresado

    Returns:
        int: Resultado de la multiplicacion
    """
    resultado = numero_uno * numero_dos 
    return resultado

def calcular_division(dividendo:int,divisor:int,mensaje_error:str = "ERROR") -> float | str:
    """Realizar la división entre dos numeros

    Args:
        dividendo (int): Numero que se va a dividir
        divisor (int): Numero por el que voy a dividir
        mensaje_error (str , opcional): Mensaje de error prederminado, por defecto es "ERROR"

    Returns:
        float | str: Resultado de la division o un mensaje de error en caso de división por cero
    """
    if divisor != 0:
        resultado = dividendo / divisor 
    else:
        resultado = mensaje_error
        
    return resultado

def calcular_resto(dividendo:int,divisor:int,mensaje_error:str = "ERROR") -> int | str:
    """Realizar el resto entre dos numeros

    Args:
        dividendo (int): Numero al que se le va a calcular el resto
        divisor (int): Numero por el que voy a dividir para calcular ese resto
        mensaje_error (str , opcional): Mensaje de error prederminado, por defecto es "ERROR"

    Returns:
        int | str: El resto de esa division o un mensaje de error en caso de división por cero
    """
    if divisor != 0:
        resultado = dividendo % divisor 
    else:
        resultado = mensaje_error
        
    return resultado

def calcular_potencia(base:int,exponente:int) -> int:
    """Realizar la potencia entre dos numeros

    Args:
        base (int): Numero base para calcular la potencia
        exponente (int): El numero que voy a elevar para calcular esa potencia

    Returns:
        int: Resultado de esa potencia
    """
    resultado = base ** exponente 
    return resultado

def calcular_factorial(numero:int) -> int:
    """Se encarga de calcular el factorial de un numero

    Args:
        numero (int): El numero al que hay que calcular el factorial

    Returns:
        int: El factorial calculado
    """
    if numero == 0 or numero == 1:
        factorial = 1
    else:
        factorial = numero * calcular_factorial(numero -1)
    
    return factorial