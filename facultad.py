class Decano:
    def __init__(self, nombre, facultad, correo):
        self.informacion = {
            "nombre": nombre,
            "facultad": facultad,
            "correo": correo
        }

    def mostrar_informacion(self):
        print("\n--- INFORMACIÓN DEL DECANO ---")
        print("Nombre:", self.informacion["nombre"])
        print("Facultad:", self.informacion["facultad"])
        print("Correo:", self.informacion["correo"])


class Secretaria:
    def __init__(self, nombre, facultad, correo):
        self.informacion = {
            "nombre": nombre,
            "facultad": facultad,
            "correo": correo
        }

    def mostrar_informacion(self):
        print("\n--- INFORMACIÓN DE LA SECRETARIA ---")
        print("Nombre:", self.informacion["nombre"])
        print("Facultad:", self.informacion["facultad"])
        print("Correo:", self.informacion["correo"])


class Profesor:
    def __init__(self, nombre, curso, horario, correo):
        self.informacion = {
            "nombre": nombre,
            "curso": curso,
            "horario": horario,
            "correo": correo
        }

    def mostrar_informacion(self):
        print("\n--- INFORMACIÓN DEL PROFESOR ---")
        print("Nombre:", self.informacion["nombre"])
        print("Curso:", self.informacion["curso"])
        print("Horario:", self.informacion["horario"])
        print("Correo:", self.informacion["correo"])
