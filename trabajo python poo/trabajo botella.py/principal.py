from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio

# Código principal
# Ejecución de la lógica del negocio

# Instancia de la clase padre
obj_Botella = Botella("Coca_Cola", "1.5L", "Especial")
obj_Botella.rellenar_botella("1.5L")
obj_Botella.cerrar_tapa(1)
obj_Botella.imprimir_resultado()



# la clase hija Botella_plastico
obj_Botella_Plastica = Botella_plastico(
    "quatro", "2.5L", "Comun", "Redondo", "Plástico", "amarillo"
)
obj_Botella_Plastica.reusar_botella()
obj_Botella_Plastica.imprimir_info()



#  la clase hija Botella_vidrio
objBotella_Vidrio = Botella_vidrio(
    "pepsi", "1.5L", "Comun", "Cubo", "Vidrio", "negra"
)
objBotella_Vidrio.reutilizar_botella()
objBotella_Vidrio.imprimir_info()