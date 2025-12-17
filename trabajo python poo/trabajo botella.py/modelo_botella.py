#Clase Padre Botella

class Botella:
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa

    def rellenar_botella(self,capacidad):
        print(f"la botella esta llenandose:{capacidad}")
        print(f"Se requiere el uso de tapa:{self.tapa}")

    def cerrar_tapa(self, dato_cantidad):
        print(f"Se hizo uso de la tapa:{self.tapa}")
        print(f"Cantidad de tapas usadas:{dato_cantidad}")
        return dato_cantidad
    
    def imprimir_resultado(self):
        
        print(f"La marca es: {self.marca}")
        print(f"La capacidad de la botella es: {self.capacidad}")
        print(f"El tipo de tapa es: {self.tapa}")
        