


from modelos.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, correo, dni):
        super().__init__(nombre, apellido, correo, dni)