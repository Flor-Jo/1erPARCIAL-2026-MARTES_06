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
    
class PokemonNode:
    def __init__(self, pokemon: Pokemon):
        self.pokemon = pokemon
        self.siguiente = None


class Entrenador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cabeza = None
        self.cantidad = 0

    def agregar_pokemon(self, pokemon: Pokemon) :
        if self.cantidad >= 6:
            print("No se pueden tener más Pokemon en el equipo. ")
            return
        nuevo_nodo = PokemonNode (pokemon)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
                actual.siguiente = nuevo_nodo

        self.cantidad += 1
    
    def mostrar_equipo(self):
        actual = self.cabeza
        while actual is not None:
            print(str(actual.pokemon))
            actual = actual.siguiente

    def nivel_promedio(self):
        if self.cantidad == 0:
            return 0

        suma_niveles = 0
        actual = self.cabeza
        while actual is not None:
            suma_niveles += actual.pokemon.nivel
            actual = actual.siguiente
    
    return suma_niveles / self.cantidad