import re

class Validations:

    def validar_eleccion_usuario(eleccion):
        return re.match(r'^[1-2]$', eleccion)
