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
    