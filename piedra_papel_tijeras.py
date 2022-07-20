import random

puntuacion_usuario = 0
puntuacion_pc= 0
opciones = ["piedra", "papel", "tijera"]

while True:
    opcion_jugador=input("Elige: piedra, papel o tijera para jugar, o Q para salir: ").lower()
    if opcion_jugador == "q":
        break
    
    if opcion_jugador not in opciones:
        continue

    # piedra es 0, papel = 1 y tijeras = 2
    numero_random = random.randint(0,2)
    opcion_pc = opciones[numero_random]
    print("Elección pc:",opcion_pc +".")
    
    if opcion_jugador == opcion_pc:
        print("Empate")

    elif opcion_jugador == "piedra" and opcion_pc == "tijeras":
        print("Ganaste")
        puntuacion_usuario +=1

    elif opcion_jugador == "papel" and opcion_pc == "piedra":
        print("Ganaste")
        puntuacion_usuario +=1

    elif opcion_jugador == "tijeras" and opcion_pc == "papel":
        print("Ganaste")
        puntuacion_usuario +=1

    else:
        print("Has perdido")
        puntuacion_pc +=1

if puntuacion_usuario == 1:
    print("Has ganado", puntuacion_usuario, "vez")
else:
    print("Has ganado", puntuacion_usuario, "veces")

if puntuacion_pc == 1:
    print("Has perdido", puntuacion_pc, "vez")
else:
    print("Has perdido", puntuacion_pc, "veces")
