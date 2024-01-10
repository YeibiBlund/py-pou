import random

class Pou:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = 0
        self.hambre = 0
        self.energia = 0
        self.felicidad = 0
        self.salud = 100 
        self.vivo = True

    def estado(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Hambre:", self.hambre)
        print("Energía:", self.energia)
        print("Felicidad:", self.felicidad)
        print("Salud:", self.salud)

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nHambre: {self.hambre}\nEnergía: {self.energia}\nFelicidad: {self.felicidad}\nSalud: {self.salud}"

    def jugar(self):
        if self.energia >= 5 and self.salud > 0:
            self.hambre += 2
            self.energia -= 5
            self.felicidad += 3
            self.salud -= 1
            self.edad += 1
            print(f"{self.nombre} ha jugado. ¡Felicidad +3, Hambre +2, Energía -5, Salud -1!")
        else:
            print(f"{self.nombre} no tiene suficiente energía para jugar o está demasiado débil. Debes alimentarlo o hacerlo dormir.")

        self.verificar_estado()

    def comer(self):
        if self.hambre >= 3 and self.salud > 0:
            self.hambre -= 3
            self.energia += 2
            self.salud += 1
            self.edad += 1
            print(f"{self.nombre} ha comido. ¡Energía +2, Hambre -3, Salud +1!")
        else:
            print(f"{self.nombre} no tiene suficiente hambre para comer o está demasiado débil. Debes hacerlo jugar o dormir.")

        self.verificar_estado()

    def dormir(self):
        if self.energia <= 95 and self.salud > 0:
            self.energia += 5
            self.hambre += 1
            self.salud += 2
            self.edad += 1
            print(f"{self.nombre} ha dormido. ¡Energía +5, Hambre +1, Salud +2!")
        else:
            print(f"{self.nombre} no tiene suficiente cansancio para dormir o está demasiado débil. Debes hacerlo jugar o alimentarlo.")

        self.verificar_estado()

    def verificar_estado(self):
        if self.salud <= 0:
            print(f"{self.nombre} ha fallecido. Descansa en paz.")
            self.vivo = False

toto = Pou("Yei")

while toto.vivo:
    toto.estado()

    opcion = input("¿Qué quieres hacer? (jugar, comer, dormir, salir): ")

    if opcion == "jugar":
        toto.jugar()
    elif opcion == "comer":
        toto.comer()
    elif opcion == "dormir":
        toto.dormir()
    elif opcion == "salir":
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

print("Fin del juego.")
