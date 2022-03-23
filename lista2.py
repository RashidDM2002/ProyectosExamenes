jugadores = {1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol",11 : "Capdevila", 14 : "Xabi Alonso",16 : "Busquets", 8 : "Xavi Hernandez",18 : "Pedrito", 6 : "Iniesta",7 : "Villa"}

print("infique el numero de jugador")
Numerodejugador=int(input())
if Numerodejugador in jugadores.keys():
    jugador=jugadores[Numerodejugador]
    print("El jugador es: ", jugador)

