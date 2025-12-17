from modelo_animales import Animal

class Insecto(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, numero_patas):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.numero_patas = numero_patas

    def volar(self):
        return f"{self.nombre} puede volar si tiene alas."

    def imprimir_info(self):
        super().imprimir_info()
        print(f"Número de patas: {self.numero_patas}")
        print("Reino: Insecto\n")