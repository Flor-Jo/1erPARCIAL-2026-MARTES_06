class Pokemon: 
    def __init__ (self, nombre: str, tipo: str, nivel: int = 1):
        self.nombre = nobre 
        self.tipo = tipo
        if 1 <= nivel <= 100:
            self.nivel = nivel
        else: 
            self.nivel = 1 

    def subir_nivel(self):
        if self.nivel < 100:
            self.nivel += 1
        else:
            print(f"{self.nombre} ya esta en nivel maximo (100). ")

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Nivel: {self.nivel} "
    
class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.equipo = []

    def agregar_pokemon(self, pokemon: Pokemon) :
        if len(self.equipo) < 6:
            self.equipo.aappend(pokemon)
            print(f"{pokemon.nombre} fue agregado al equipo de {self.nombre}. ")
            else:
                print(f"El equipo ya esta completo (maximo 6 Pokemon). No se pudo agregar a {pokemon.nombre}")
    
    def mostrar_equipo(self):
        if len(self.equipo) == 0:
            print(f"{self.nombre} no tiene ningun Pokemon en su equipo todavia")
        else: 
            print(f"---Equipode {self.nombre} ---")   
            for poke in self.equipo:
                print(poke)

    def nivel_promedio(self): 
        if len(self.equipo) == 0:
            return 0

        suma_niveles = 0
        for poke in self.equipo:
            suma_niveles += poke.nivel


        return suma_niveles / len(self.equipo)