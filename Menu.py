#Las funciones de un menu de opciones no son funciones genericas (especificas), cuando veamos paradigma funcional de forma más profunda (ciudadanos de primera clase) si vamos a poder hacer menus genericos, por ahora no.
import os
import Inputs
import Funciones

def limpiar_consola() -> None:
    if os.name == 'nt': #WINDOWS
        os.system('cls')
    else:#MAC/LINUX
        os.system('clear')
    print("")

def esperar_menu() -> None:
    input("Toque enter para continuar...")
    limpiar_consola()

#Calculadora menu principal
def mostrar_menu_principal_calculadora()-> None:
    #CALCULADORA
    #1.Ingresar el primer numero
    #2.Ingresar el segundo numero
    #3.Realizar operaciones
    #4.Salir del sistema
    numero_uno = None
    numero_dos = None

    while True:
        print("{:^30}".format("🧮  CALCULADORA  🧮"))
        print(f"1. Ingresar el primer numero ({numero_uno})")
        print(f"2. Ingresar el segundo numero ({numero_dos})")
        print("3. Realizar operaciones")
        print("4. Salir del sistema")

        opcion = input("Ingrese su opcion: ")
        #Match
        limpiar_consola()
        match opcion:
            case "1":
                print("")
                numero_uno = Inputs.ingresar_entero(0,"Ingrese el primer numero: ","Error, no se permiten negativos\nReingrese el primer numero: ")
                print(f"Se ingreso correctamente el numero: {numero_uno}")
            case "2":
                print("")
                numero_dos = Inputs.ingresar_entero(0,"Ingrese el segundo numero: ","Error, no se permiten negativos\nReingrese el segundo numero: ")
                print(f"Se ingreso correctamente el numero: {numero_dos}")
            case "3":
                if numero_uno != None and numero_dos != None:
                    mostrar_sub_menu_calculadora(numero_uno,numero_dos)
                else:
                    print("No ingresaste los dos numeros no se puede hacer ninguna operación")
                    esperar_menu()
            case "4":
                print("Chau chau")
                break
            case _:
                print("OPCION INVALIDA")

        if opcion != "3":
            esperar_menu()

        #if-elif
        # if opcion == "1":
        #     print("OPCION 1")
        # elif opcion == "2":
        #     print("OPCION 2")
        # elif opcion == "3":
        #     print("OPCION 3")
        # elif opcion == "4":
        #     print("OPCION 4")
        # else:
        #     print("OPCION INVALIDA")


# #Calculadora sub menu principal
def mostrar_sub_menu_calculadora(numero_uno:int,numero_dos:int) -> None:
    #1.Calcular suma
    #2.Calcular resta
    #3.Calcular division
    #4.Calcular multiplicacion
    #5.Calcular resto
    #6.Calcular potencia
    #7.Calcular factorial
    #8.Volver al menu principal

    while True:
        print("{:^30}".format("⚙️  OPERACIONES  ⚙️"))
        print("1. Calcular suma")
        print("2. Calcular resta")
        print("3. Calcular multiplicacion")
        print("4. Calcular división")
        print("5. Calcular resto")
        print("6. Calcular potencia")
        print("7. Calcular factorial")
        print("8. Calcular fibonacci")
        print("9. Volver al menu principal")

        opcion = input("Ingrese su opcion: ")
        #Match
        limpiar_consola()
        match opcion:
            case "1":
                resultado = Funciones.calcular_suma(numero_uno,numero_dos)
                print(f"{numero_uno} + {numero_dos} = {resultado}")
            case "2":
                resultado = Funciones.calcular_resta(numero_uno,numero_dos)
                print(f"{numero_uno} - {numero_dos} = {resultado}")
            case "3":
                resultado = Funciones.calcular_multiplicacion(numero_uno,numero_dos)
                print(f"{numero_uno} * {numero_dos} = {resultado}")
            case "4":
                resultado = Funciones.calcular_division(numero_uno,numero_dos)
                print(f"{numero_uno} / {numero_dos} = {resultado}")
            case "5":
                resultado = Funciones.calcular_resto(numero_uno,numero_dos)
                print(f"{numero_uno} / {numero_dos} da como resto = {resultado}")
            case "6":
                resultado = Funciones.calcular_potencia(numero_uno,numero_dos)
                print(f"{numero_uno} elevado a {numero_dos} = {resultado}")
            case "7":
                resultado_a = Funciones.calcular_factorial(numero_uno)
                resultado_b = Funciones.calcular_factorial(numero_dos)
                print(f"a) {numero_uno}! = {resultado_a}")
                print(f"b) {numero_dos}! = {resultado_b}")
            case "8":
                resultado_a = Funciones.calcular_fibonacci(numero_uno)
                resultado_b = Funciones.calcular_fibonacci(numero_dos)
                print(f"a) Fibonacci de {numero_uno} = {resultado_a}")
                print(f"b) Fibonacci de {numero_dos} = {resultado_b}")
            case "9":
                break
            case _:
                print("OPCION INVALIDA")
        esperar_menu()