#GUARDEN TODAS LAS FUNCIONES DE ENTRADA DE DATOS

def ingresar_entero(minimo:int,mensaje:str = "Ingrese un numero: ",mensaje_error:str = "Error, Reingrese el numero: "):
    numero = int(input(mensaje))
    while numero < minimo:
        numero = int(input(mensaje_error))
    return numero

# def ingresar_flotante()

# def ingresar_string()
    
# def ingresar_usuario()
    
# def ingresar_clave()
    
# def iniciar_sesion()