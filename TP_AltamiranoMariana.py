import random
import time
import os

'''
Declarativa de variables
nombre_mayor_menor,nombre_numero,nombre_par_impar:string
ganadas_numero,veces_jugadas_mayor_menor,mayor_racha,veces_jugadas_numero,perdidas_numero,veces_jugadas_par_impar,ganadas_par_impar,perdidas_par_impar:int
,veces_jugadas_par_impar,ganadas_par_impar,perdidas_par_impar:int
Max_Jugadores, cantidad_jugadores: int
Jugadores: array de string
Partidas_Jugadas_BJ, Victorias_BJ, Derrotas_BJ: array de int
creditos: array de enteros

'''
# Variables:
# JUEGO A - HASTA 10 JUGADORES

nombres_mayor_menor = [""] * 10
veces_jugadas_mayor_menor = [0] * 10
mejor_racha_mayor_menor = [0] * 10

cantidad_jugadores_mayor_menor = 0
# JUEGO B arrays
nombre_numero = [""] * 10
veces_jugadas_numero = [0] * 10
ganadas_numero = [0] * 10
perdidas_numero = [0] * 10
cant_jugadores_num = 0
colores_numero = [
    "\033[91m", "\033[92m", "\033[93m", "\033[94m","\033[95m", "\033[96m","\033[31m", "\033[32m", "\033[33m", "\033[35m" ]
colornormal = "\033[0m"
# JUEGO C arrays
Max_Jugadores = 10
Jugadores = Max_Jugadores * [""]
cantidad_jugadores = 0
Partidas_Jugadas_BJ = Max_Jugadores * [0]
Victorias_BJ = Max_Jugadores * [0]
Derrotas_BJ = Max_Jugadores * [0]
# JUEGO D - HASTA 10 JUGADORES
nombres_par_impar = Max_Jugadores * [""]
#nombres_par_impar = ["Brian", "Fausto", "German", "Julieta", "Pablo", "Janet", "Emily", "Federico", "Frodo", ""]
creditos = Max_Jugadores * [1000]
veces_jugadas_par_impar = Max_Jugadores * [0]
ganadas_par_impar = Max_Jugadores * [0]
perdidas_par_impar = Max_Jugadores * [0]
#
#Funcion chequea que un numero sea valido para el juego del numero secreto
def chequeaNumeroValido(numero):
    valido=True
    for i in range(len(numero)):
        if numero[i] < "0" or numero[i] > "9":
            valido=False
    return valido
def buscar_o_agregar_jugador(nombre):
    global cantidad_jugadores_mayor_menor

    # Buscar si el jugador ya existe
    i = 0
    while i < cantidad_jugadores_mayor_menor:
        if nombres_mayor_menor[i].upper() == nombre.upper():
            return i   # devuelve la posición donde está guardado
        i = i + 1

    # Si no existe, verificar si hay lugar
    if cantidad_jugadores_mayor_menor < 10:

        posicion_nueva = cantidad_jugadores_mayor_menor

        nombres_mayor_menor[posicion_nueva] = nombre
        veces_jugadas_mayor_menor[posicion_nueva] = 0
        mejor_racha_mayor_menor[posicion_nueva] = 0

        cantidad_jugadores_mayor_menor = cantidad_jugadores_mayor_menor + 1

        return posicion_nueva

    else:
        # No hay espacio para más jugadores
        return -1
#Función juego A
def juego_mayor_menor():
    '''
    variables locales:
    seguir: boolean
    jugar_nuevamente: boolean
    nombre: string
    numero_actual, siguiente_numero, racha: int
    opcion: string
    '''
    nombre = ""
    while nombre =="" or nombre.isalpha() == False:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre == "":
            print("Porfavor ingrese un nombre")
        elif nombre.isalpha() == False: 
            print("El nombre solo debe contener letras")
    posicion = buscar_o_agregar_jugador(nombre)
    if posicion == -1: 
        print("No hay cupos para un nuevo jugador.") 
        input("Presione ENTER para volver al menu...") 
        return
    jugar_nuevamente = True
    while jugar_nuevamente == True:
        veces_jugadas_mayor_menor[posicion] = veces_jugadas_mayor_menor[posicion] + 1
        numero_actual = random.randint(1, 1000)
        racha = 0
        seguir = True
        os.system("cls")
        print(f"""{C_CYAN}
╔══════════════════════════════╗
║     {blanco}JUEGO MAYOR O MENOR      {C_CYAN}║
╠══════════════════════════════╣
║ {blanco}Adivina si el proximo numero {C_CYAN}║
║ {blanco}sera MAYOR o MENOR.          {C_CYAN}║
║                              ║
║ {blanco}Si fallas, termina la ronda. {C_CYAN}║
╚══════════════════════════════╝{blanco}
        
""")
        input("Presione ENTER para comenzar.")
        os.system("cls")
        while seguir == True:
            print(f"""{C_CYAN}
        ╔════════════════════╗
        ║  {blanco}¿MAYOR O MENOR?   {C_CYAN}║
╔═══════╩════════════════════╩═══════╗
║   ┌────────────────────────────┐   ║
║   │       {blanco}El numero es...      {C_CYAN}│   ║
║   │                            │   ║
║   │      {amarillo}{numero_actual:^19}   {C_CYAN}│   ║
║   │                            │   ║
║   └────────────────────────────┘   ║
║                                    ║
║            {blanco}Escriba {amarillo}MAYOR           {C_CYAN}║
║                 {blanco}o                  {C_CYAN}║
║           {blanco}Escriba {amarillo}MENOR            {C_CYAN}║
╚════════════════════════════════════╝{blanco}
        
""")
            eleccion = input(f"Ingrese {amarillo}Mayor {blanco}o {amarillo}Menor: ").upper()
                #validacion para ingresar solo mayor o menor
            while eleccion != "MAYOR" and eleccion != "MENOR":
                    print(f"{rojo}Error, ingrese una opcion valida{blanco}")
                    eleccion = input("Ingrese Mayor o Menor: ").upper()
                #fin validacion
            siguiente_numero = random.randint(1, 1000)
            os.system("cls")
            print("Siguiente numero:", siguiente_numero)
            if siguiente_numero == numero_actual: 
                print(f"{azul}Salio el mismo numero. La racha no cambia{blanco}.") 
            elif eleccion == "MAYOR" and siguiente_numero > numero_actual: 
                racha = racha + 1 
                print(f"{amarillo}Acertaste")
            elif eleccion == "MENOR" and siguiente_numero < numero_actual: 
                racha = racha + 1 
                print(f"{amarillo}Acertaste{blanco}") 
            else: 
                print(f"{azul}Perdiste") 
                print("Racha lograda:", racha) 
                seguir = False
            numero_actual = siguiente_numero
            if seguir == True:
                    input("Presione ENTER para continuar.")
                    os.system("cls")
        if racha > mejor_racha_mayor_menor[posicion]: 
            mejor_racha_mayor_menor[posicion] = racha
        print(f"""{azul}
╔════════════════════════════════════╗
║             {C_CYAN}Perdiste :C            {azul}║
╠════════════════════════════════════╣
║                                    ║
║   {blanco}Jugador: {C_CYAN}{nombre:^12}            {azul}║
║   {blanco}Racha final: {racha:^10}         {azul}║
║                                    ║
╠════════════════════════════════════╣
║        {C_CYAN}1. {blanco}Jugar de nuevo           {azul}║
║        {C_CYAN}2. {blanco}Volver al menu           {azul}║
╚════════════════════════════════════╝{blanco}
""")
        opcion = input ("Seleccione una opcion: ")
        while opcion != "1" and opcion != "2":
            print("Opcion invalida")
            opcion = input(f"{rojo}Seleccione una opcion valida: {blanco}")
        if opcion == "1":
            os.system("cls")
        else:
            jugar_nuevamente = False

#Funcion buscar jugadores, juego B (para reporte)
def buscar_agregar_jugadores_num(nombre):
    global cant_jugadores_num
    i = 0
    while i < cant_jugadores_num:
        if nombre_numero[i].upper() == nombre.upper():
            return i
        i = i + 1
    if cant_jugadores_num < 10:
        pos_nueva = cant_jugadores_num
        nombre_numero[pos_nueva] = nombre
        veces_jugadas_numero[pos_nueva] = 0
        ganadas_numero[pos_nueva] = 0
        perdidas_numero [pos_nueva] = 0
        cant_jugadores_num = cant_jugadores_num + 1
        return pos_nueva
    else:
        return -1
#colores juego B
azul = "\033[38;5;24m"
amarillo = "\033[38;5;223m"
blanco = "\033[0m"
rojo = "\033[38;5;203m"
verde = "\033[92m"
# funcion juego B
def numero_secreto():
    '''
    variables locales:
    nombre: string
    secreto, intentos: int
    adivino: boolean
    opcion: string
    '''
    global nombre_numero
    global veces_jugadas_numero
    global ganadas_numero
    global perdidas_numero
    nombre = "" 
    while nombre =="" or nombre.isalpha() == False:
            nombre = input("Ingrese su nombre: ").strip()
            if nombre == "":
                print("Porfavor ingrese un nombre")
            elif nombre.isalpha() == False: 
                print("El nombre solo debe contener letras")
    posicion = buscar_agregar_jugadores_num(nombre)
    if posicion == -1:
        print("No se admiten mas jugadores :C")
        input ("Presione ENTER para continuar.")
        return
    jugar_nuevamente = True
    while jugar_nuevamente == True:
        veces_jugadas_numero[posicion] = veces_jugadas_numero[posicion] + 1
        os.system("cls")

        print(f"""{azul}
╔══════════════════════════════╗
║{amarillo}         NUMERO SECRETO       {azul}║
╠══════════════════════════════╣
║ {amarillo}Debes adivinar un numero     {azul}║
║ {amarillo}entre 1 y 100.               {azul}║
║                              ║
║ {amarillo}Tenes 6 intentos.            {azul}║
╚══════════════════════════════╝{blanco}
""")
        input("Presione ENTER para comenzar.")
        os.system("cls")
        secreto = random.randint(1, 100)
        intentos = 6
        adivino = False
        while intentos > 0 and adivino == False:
            print(f"""{azul}
╔══════════════════════════════╗
║{amarillo}      NUMERO SECRETO          {azul}║
╠══════════════════════════════╣
║{amarillo} Intentos restantes: {intentos:^2}       {azul}║
╚══════════════════════════════╝{blanco}
""")
            entrada = input("Ingrese un numero del 1 al 100 o S para salir: ")
            if entrada.upper() == "S":
                return
            #validacion para ingresar solo numeros del 1 al 100
            while entrada == "" or chequeaNumeroValido(entrada) == False:
                if entrada.upper() == "S":
                                return
                print(f"{rojo}Error, ingrese un numero valido{blanco}")
                entrada = input("Ingrese un numero del 1 al 100 o S para salir:")
              #fin validacion
            numero=int(entrada)
            while numero < 1 or numero > 100:
                print(f"{rojo}Error, ingrese un numero entre 1 y 100{blanco}")
                entrada = input("Ingrese un numero del 1 al 100 o S para salir: ")
                if entrada.upper() == "S": 
                    return
                while chequeaNumeroValido(entrada) == False:
                    print(f"{rojo}Error, ingrese un numero valido{blanco}")
                    entrada = input("Ingrese un numero del 1 al 100: ")
                    print()
                numero = int(entrada)
            os.system("cls") 
            if numero == secreto:
                print(f""" {amarillo}
╔══════════════════════════════╗
║         GANASTE :D           ║
╠══════════════════════════════╣
║ {azul}Felicidades    {nombre:^6}      {amarillo}║
║ {amarillo}Adivinaste el numero.        ║
╚══════════════════════════════╝{blanco}
""")
                ganadas_numero[posicion] = ganadas_numero[posicion] + 1
                adivino = True
            elif numero < secreto:
                print(f"El numero secreto es {amarillo}MAYOR{blanco}")
                print(f"Usted ingreso el numero: {amarillo}{numero}")
            else:
                print(f"El numero secreto es {amarillo}MENOR{blanco}")
                print(f"Usted ingreso el numero: {amarillo}{numero}")
            intentos = intentos - 1
        if adivino == False:
            print(f"""{azul}
╔══════════════════════════════╗
║         PERDISTE :c          ║
╠══════════════════════════════╣
║{amarillo} El numero era: {secreto:^13} {azul}║
╚══════════════════════════════╝{blanco}
""")
            perdidas_numero[posicion] = perdidas_numero[posicion] + 1
        print(f"""{rojo}
╔════════════════════════════════════╗
║          FIN DE PARTIDA            ║
╠════════════════════════════════════╣
║{blanco}   Jugador: {amarillo}{nombre:^24}{rojo}║
║                                    ║
║        {amarillo}1. {blanco}Jugar de nuevo           {rojo}║
║        {amarillo}2. {blanco}Volver al menu           {rojo}║
╚════════════════════════════════════╝{blanco}
""")
        opcion = input("Seleccione una opcion: ")
        while opcion != "1" and opcion != "2":
            print(f"{rojo}Opcion invalida{blanco}")
            opcion =input("Seleccione opcion: ")
        if opcion == "1":
            os.system("cls")
        else:
            jugar_nuevamente = False
#Colores juego C
C_VERDE = '\033[92m'
C_AMARILLO = '\033[93m'
C_CYAN = '\033[96m'
C_ROJO = '\033[91m'
C_BLANCO = '\033[0m' 

'''Variables locales:
nombre_ingresado, respuesta_jugar, opcion_juego: string
Tam_Mazo, posicion_carta, palo, numero_carta, posicion_jugador, suma_jugador, suma_banca, ases_jugador, ases_banca, Jugador_Carta1, 
Jugador_Carta2, Banca_Carta1, Banca_Carta2, carta_nueva, carta_banca, carta, indice_limpieza: int
Nombres_Cartas, Nombres: array de string
Valores_Cartas, Cartas_Usadas: array de int'''

# Función juego C

def blackjack():

    global cantidad_jugadores
    Tam_Mazo = 52
    Valores_Cartas = Tam_Mazo * [0]
    Nombres_Cartas = Tam_Mazo * [""]
    Cartas_Usadas = Tam_Mazo * [0] 

    #Funciones para el juego:

    def obtener_carta():
        carta = random.randint(0, 51)
        while Cartas_Usadas[carta] == 1:
            carta = random.randint(0, 51)
        Cartas_Usadas[carta] = 1
        return carta
    
    def limpiar_mazo():
        indice_limpieza = 0
        while indice_limpieza < Tam_Mazo:
            Cartas_Usadas[indice_limpieza] = 0
            indice_limpieza = indice_limpieza + 1

    # ARMADO DEL MAZO
    Nombres = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J(10)", "Q(10)", "K(10)"]

    posicion_carta = 0
    palo = 0
    while palo < 4:
        numero_carta = 0  
        while numero_carta < 13:
            Nombres_Cartas[posicion_carta] = Nombres[numero_carta]
            if numero_carta == 0:
                Valores_Cartas[posicion_carta] = 11
            elif numero_carta >= 10:
                Valores_Cartas[posicion_carta] = 10
            else:
                Valores_Cartas[posicion_carta] = numero_carta + 1
                
            posicion_carta = posicion_carta + 1
            numero_carta = numero_carta + 1  
        palo = palo + 1  

    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{C_VERDE}
╔════════════════════════════════════╗
║          {C_AMARILLO}BLACKJACK                 {C_VERDE}║
╠════════════════════════════════════╣
║     ¡Acercate a 21 sin pasarte!    ║
║    Vence a la banca para ganar.    ║
╚════════════════════════════════════╝{C_BLANCO}
""")
    nombre_ingresado = ""
    while nombre_ingresado == "":
        nombre_ingresado = input("Ingrese su nombre para jugar o 'salir' para terminar: ").lower()
        if nombre_ingresado == "":
            print("Ingrese una opcion porfavor")

    while nombre_ingresado != "salir": 
        posicion_jugador = 0
        while posicion_jugador < cantidad_jugadores and Jugadores[posicion_jugador] != nombre_ingresado:
            posicion_jugador = posicion_jugador + 1

        if posicion_jugador == cantidad_jugadores:
            if cantidad_jugadores < Max_Jugadores:
                Jugadores[posicion_jugador] = nombre_ingresado
                cantidad_jugadores = cantidad_jugadores + 1
                print("Nuevo jugador registrado.")
            else:
                print("Error: No hay cupos disponibles (Máximo 10 jugadores).")
                posicion_jugador = -1

        if posicion_jugador != -1:
            respuesta_jugar = "si"
            
            while respuesta_jugar == "si":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""{C_CYAN}
    ╔══════════════════════════════╗
    ║      REPARTIENDO CARTAS      ║
    ╚══════════════════════════════╝{C_BLANCO}
""")
                
                Partidas_Jugadas_BJ[posicion_jugador] = Partidas_Jugadas_BJ[posicion_jugador] + 1
                
                limpiar_mazo()
                    
                suma_jugador = 0
                suma_banca = 0
                ases_jugador = 0
                ases_banca = 0

                Jugador_Carta1 = obtener_carta()
                suma_jugador = suma_jugador + Valores_Cartas[Jugador_Carta1]
                if Valores_Cartas[Jugador_Carta1] == 11: ases_jugador = ases_jugador + 1
                print(nombre_ingresado, "recibe:", Nombres_Cartas[Jugador_Carta1])

                Jugador_Carta2 = obtener_carta()
                suma_jugador = suma_jugador + Valores_Cartas[Jugador_Carta2]
                if Valores_Cartas[Jugador_Carta2] == 11: ases_jugador = ases_jugador + 1
                print(nombre_ingresado, "recibe:", Nombres_Cartas[Jugador_Carta2])
                print("")

                Banca_Carta1 = obtener_carta()
                suma_banca = suma_banca + Valores_Cartas[Banca_Carta1]
                if Valores_Cartas[Banca_Carta1] == 11: ases_banca = ases_banca + 1
                print("La banca recibe:", Nombres_Cartas[Banca_Carta1])

                Banca_Carta2 = obtener_carta()
                suma_banca = suma_banca + Valores_Cartas[Banca_Carta2]
                if Valores_Cartas[Banca_Carta2] == 11: ases_banca = ases_banca + 1
                print("La banca recibe:", Nombres_Cartas[Banca_Carta2])
                print("____________")
                print("")
                
                while suma_jugador > 21 and ases_jugador > 0:
                    suma_jugador = suma_jugador - 10
                    ases_jugador = ases_jugador - 1
                while suma_banca > 21 and ases_banca > 0:
                    suma_banca = suma_banca - 10
                    ases_banca = ases_banca - 1
                    
                print("Suma inicial de", nombre_ingresado, ": ", suma_jugador)
                print("")
                
                opcion_juego = "pedir"
                while opcion_juego == "pedir" and suma_jugador < 21:
                    opcion_juego = input("\n¿'Pedir' o 'Plantarse'?: ").lower()
                   
                    while opcion_juego != "pedir" and opcion_juego != "plantarse":
                        opcion_juego = input("Opción inválida. ¿'Pedir' o 'Plantarse'?: ").lower()
                    
                    if opcion_juego == "pedir":
                        carta_nueva = obtener_carta()
                        suma_jugador = suma_jugador + Valores_Cartas[carta_nueva]
                        if Valores_Cartas[carta_nueva] == 11: 
                            ases_jugador = ases_jugador + 1
                            
                        print(nombre_ingresado, " recibe: ", Nombres_Cartas[carta_nueva])
                        print("")
                        
                        while suma_jugador > 21 and ases_jugador > 0:
                            suma_jugador = suma_jugador - 10
                            ases_jugador = ases_jugador - 1
                            
                        print("Suma de", nombre_ingresado, "actual:", suma_jugador)
                        print("")

                if suma_jugador <= 21:
                    print(f"""{C_AMARILLO}
    ╔══════════════════════════════╗
    ║       TURNO DE LA BANCA      ║
    ╚══════════════════════════════╝{C_BLANCO}
""")

                    while suma_banca < 17:
                        carta_banca = obtener_carta()
                        suma_banca = suma_banca + Valores_Cartas[carta_banca]
                        if Valores_Cartas[carta_banca] == 11: 
                            ases_banca = ases_banca + 1
                            
                        print("La banca recibe:", Nombres_Cartas[carta_banca])
                        print("")
                        
                        while suma_banca > 21 and ases_banca > 0:
                            suma_banca = suma_banca - 10
                            ases_banca = ases_banca - 1
                            
                    print("Suma de la banca final:", suma_banca)
                    print("")

                print(f"""{C_ROJO}
    ╔══════════════════════════════╗
    ║          RESULTADO           ║
    ╚══════════════════════════════╝{C_BLANCO}
""")

                if suma_jugador > 21:
                    print("Te pasaste de 21. Gana la Banca.")
                    Derrotas_BJ[posicion_jugador] = Derrotas_BJ[posicion_jugador] + 1
                elif suma_banca > 21:
                    print("La Banca se pasó de 21. ¡GANASTE!")
                    Victorias_BJ[posicion_jugador] = Victorias_BJ[posicion_jugador] + 1
                elif suma_jugador > suma_banca:
                    print("Puntaje más alto. ¡GANASTE!")
                    Victorias_BJ[posicion_jugador] = Victorias_BJ[posicion_jugador] + 1
                elif suma_banca > suma_jugador:
                    print("La Banca tiene puntaje más alto. Gana la Banca.")
                    Derrotas_BJ[posicion_jugador] = Derrotas_BJ[posicion_jugador] + 1
                else:
                    print("Empate.")
                    
                print("Total de victorias de", Jugadores[posicion_jugador], ":", Victorias_BJ[posicion_jugador])
                
                respuesta_jugar = input("\n¿Jugar otra partida? (si/no): ").lower()
                while respuesta_jugar != "si" and respuesta_jugar != "no":
                    respuesta_jugar = input("Opción inválida. ¿Jugar otra partida? (si/no): ").lower()

        os.system("cls" if os.name == "nt" else "clear")
        print(f"""{C_VERDE}
╔════════════════════════════════════╗
║          {C_AMARILLO}BLACKJACK                 {C_VERDE}║
╚════════════════════════════════════╝{C_BLANCO}
""")
        nombre_ingresado = input("Ingrese su nombre para jugar o 'salir' para terminar: ").lower()
#Función juego D
def par_impar():
    '''
    variables locales:
    indice_jugador: int
    nombre: string
    dado1, dado2, suma: int
    eleccion, resultado: string
    jugar_nuevamente: bool
    opcion: string
    '''
    global nombres_par_impar
    global creditos
    global veces_jugadas_par_impar
    global ganadas_par_impar
    global perdidas_par_impar
    global Max_Jugadores
    nombre = ""
    while nombre =="" or nombre.isalpha() == False:
            nombre = input("Ingrese su nombre: ").strip()
            if nombre == "":
                print("Porfavor ingrese un nombre")
            elif nombre.isalpha() == False: 
                print("El nombre solo debe contener letras")
    indice_jugador = 0
    
    while (indice_jugador < Max_Jugadores) and nombres_par_impar[indice_jugador] != "" and nombre != nombres_par_impar[indice_jugador]:
        indice_jugador = indice_jugador + 1

    if indice_jugador == 10:
        print(f"{rojo}Maximo de jugadores alcanzado. Sentimos las molestias.")
        time.sleep(0.7)
        input(f"{blanco}Saliendo del juego. Presione ENTER para continuar...")
    elif creditos[indice_jugador] == 0:
        print(f"{rojo}{nombres_par_impar[indice_jugador]} no posee creditos. No es posible iniciar una partida.")
        time.sleep(0.7)
        input(f"{blanco}Saliendo del juego. Presione ENTER para continuar...")
    else:
        if nombres_par_impar[indice_jugador] == "":
            nombres_par_impar[indice_jugador] = nombre

        jugar_nuevamente = True
        while jugar_nuevamente == True and creditos[indice_jugador] != 0:
            print(f"{azul}Jugador: {nombres_par_impar[indice_jugador]}")
            print(f"{amarillo}Credito disponible: {creditos[indice_jugador]}")
            credito_apostado = int(input(f"{blanco}Ingrese la cantidad de creditos que desea apostar: "))
            while credito_apostado > creditos[indice_jugador] and creditos[indice_jugador] != 0:
                print(f"{rojo}No puede apostar una cantidad mayor de creditos a la que posee.")
                print(f"{amarillo}Credito disponible: {creditos[indice_jugador]}")
                credito_apostado = int(input(f"{blanco}Ingrese la cantidad de creditos que desea apostar nuevamente: "))
            print(f"{verde}Credito ingresado correctamente!")
            print(f"{blanco}Preparando juego...")
            time.sleep(1)
            veces_jugadas_par_impar[indice_jugador] = veces_jugadas_par_impar[indice_jugador] + 1
            os.system("cls")
            print(f"""{verde}
    ╔══════════════════════════════╗
    ║  {amarillo}       PAR O IMPAR  {verde}        ║
    ╠══════════════════════════════╣
    ║ {amarillo}Se lanzarán dos dados. {verde}      ║
    ║ {amarillo}Debes adivinar si la suma {verde}   ║
    ║ {amarillo}será PAR o IMPAR. {verde}           ║
    ╚══════════════════════════════╝
    """)
            input(f"{blanco}Presione ENTER para comenzar.")
            os.system("cls")
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            suma = dado1 + dado2
            print(f"""{verde}
    ╔══════════════════════════════╗
    ║       {amarillo} ¿PAR O IMPAR? {verde}        ║
    ╚══════════════════════════════╝
    """)
            eleccion = input(f"{blanco}Ingrese PAR o IMPAR: ").upper()
            #validacion para ingresar solo PAR o IMPAR
            while eleccion != "PAR" and eleccion != "IMPAR":
                print(f"{rojo}Error, ingrese una opcion valida")
                eleccion = input(f"{blanco}Ingrese PAR o IMPAR: ").upper()
            os.system("cls")
            print(f"""{verde}
    ╔══════════════════════════════╗
    ║     {amarillo} RESULTADO DE DADOS {verde}     ║
    ╠══════════════════════════════╣
    ║ {amarillo}Dado 1: {dado1:^21}{verde}║
    ║ {amarillo}Dado 2: {dado2:^21}{verde}║
    ║                              ║
    ║ {azul}Suma:   {suma:^21}{verde}║
    ╚══════════════════════════════╝
    """)
            if suma % 2 == 0:
                    resultado = "PAR"
            else:
                    resultado = "IMPAR"
            print(f"{blanco}Resultado:", resultado)
            if eleccion == resultado:
                print(f"{verde}Acertaste! =D")
                ganadas_par_impar[indice_jugador] = ganadas_par_impar[indice_jugador] + 1
                creditos[indice_jugador] = creditos[indice_jugador] + credito_apostado
            else:
                print(f"{rojo}Perdiste =(")
                perdidas_par_impar[indice_jugador] = perdidas_par_impar[indice_jugador] + 1
                creditos[indice_jugador] = creditos[indice_jugador] - credito_apostado
            print(f"""{verde}
    ╔════════════════════════════════════╗
    ║         {amarillo} FIN DE PARTIDA  {verde}          ║
    ╠════════════════════════════════════╣
    ║  {amarillo} Jugador: {nombres_par_impar[indice_jugador]:^24}{verde}║
    ║  {amarillo} Creditos: {creditos[indice_jugador]:^23}{verde}║
    ║    {amarillo}    1. Jugar de nuevo    {verde}       ║
    ║     {amarillo}   2. Volver al menu     {verde}      ║
    ╚════════════════════════════════════╝
    """)
            if creditos[indice_jugador] == 0:
                print(f"{rojo}Ya no posee creditos para seguir jugando.")
                time.sleep(0.7)
                input(f"{blanco}Volviendo al Menu Principal. Presione ENTER para continuar...")
            else:
                opcion = input(f"{blanco}Seleccione una opcion:")
                while opcion != "1" and opcion != "2":
                    print(f"{rojo}Opcion invalida.")
                    opcion = input(f"{blanco}Seleccione una opcion: ")
                if opcion == "1":
                    os.system("cls")
                else:
                    jugar_nuevamente = False
# REPORTE
def reporte():
    print(f"""{C_VERDE}
            ================ REPORTE ================
            {C_BLANCO}""")
    print("JUEGO A - MAYOR O MENOR") 
    for i in range(cantidad_jugadores_mayor_menor): 
        print(colores_numero[i])
        print("Jugador:", nombres_mayor_menor[i]) 
        print("Partidas jugadas:", veces_jugadas_mayor_menor[i]) 
        print("Mejor racha:", mejor_racha_mayor_menor[i])
        print(colornormal)

    print(f"""{azul}-----------------------------------------{blanco}""")

    print("JUEGO B - NUMERO SECRETO")
    for i in range(cant_jugadores_num):
        print(colores_numero[i])
        print("Nombre del jugador:", nombre_numero [i])
        print("Cantidad de veces jugadas:", veces_jugadas_numero[i])
        print("Cantidad de veces ganadas:", ganadas_numero[i])
        print("Cantidad de veces perdidas:", perdidas_numero[i])
        print(colornormal)

    print(f"""{azul}
========================================={blanco}
""")
    print("JUEGO C - BLACKJACK")
    i = 0
    while i < cantidad_jugadores:
        print(colores_numero[i])
        print("Jugador:", Jugadores[i])
        print("Partidas jugadas:", Partidas_Jugadas_BJ[i])
        print("Victorias:", Victorias_BJ[i])
        print("Derrotas:", Derrotas_BJ[i])
        print("--------------------")
        print(colornormal)
        i = i + 1
    print(f"""{azul}
========================================={blanco}
""")
    print("""
          -----------------------------------------
""")
    print("JUEGO D - PAR O IMPAR")
    i = 0
    while nombres_par_impar[i] != "":
        print(colores_numero[i])
        print("Nombre del jugador:", nombres_par_impar[i])
        print("Creditos: ", creditos[i])
        print("Cantidad de veces jugadas:", veces_jugadas_par_impar[i])
        print("Cantidad de veces ganadas:", ganadas_par_impar[i])
        print("Cantidad de veces perdidas:", perdidas_par_impar[i])
        print(colornormal)
        i = i + 1
    print(f"""{azul}
========================================={blanco}
""")
    os.system("Pause")

def mensaje_bienvenida():

    print(f"""{amarillo}
**************************************************
*                                                *
*            {blanco}JUEGOS AZAR Y LOGICA                {amarillo}*
*                                                *
*  {rojo} LOS JUEGOS DE APUESTA ESTAN PROHIBIDOS       {amarillo}*
*             {rojo}PARA MENORES DE EDAD               {amarillo}*
*                                                *
*        {rojo}EL EXCESO ES PERJUDICIAL PARA           {amarillo}*
*                 {rojo}LA SALUD                       {amarillo}*
*                                                *
**************************************************{blanco}
""")

    input("Presione ENTER para continuar...")

def mensaje_despedida():

    print(f"""{amarillo}
**************************************************
*                                                *
*              GRACIAS POR JUGAR                 *
*                                                *
*   NO APUESTE, JUEGUE POR DIVERSION             *
*                                                *
**************************************************{blanco}
""")

    input("Presione ENTER para salir...")
    
def menu():
    opcion = ""
    while opcion != "F":
        os.system("cls")
        print(f"""{amarillo}
    =========== MENU PRINCIPAL ===========
    A. {blanco}Juego del menor-mayor{amarillo}
    ====================================== 
    B. {blanco}Adivinar el numero secreto{amarillo}
    ====================================== 
    C. {blanco}Blackjack{amarillo}
    ====================================== 
    D. {blanco}Par o impar{amarillo}
    ====================================== 
    E. {blanco}Reporte{amarillo}
    ======================================
    F. {blanco}Salir del programa{amarillo}
    ======================================{blanco}
    """)
        opcion = input("Ingrese una opcion: ").upper()
        if opcion == "A":
            juego_mayor_menor()
        elif opcion == "B":
            numero_secreto()
        elif opcion == "C":
            blackjack()
        elif opcion == "D":
            par_impar()
        elif opcion == "E":
            reporte()
        elif opcion == "F":
            print("Gracias por jugar, no apueste, juega por diversión")
        else:
            print("Opcion invalida")
#PRINCIPAL
mensaje_bienvenida()
menu()
mensaje_despedida()
