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

    def evaluar_beca(self, estudiante):
        if estudiante.nota >= 85:
            resultado = "Beca aprobada"
        else:
            resultado = "Beca rechazada"

        print("\n--- EVALUACIÓN DE BECA ---")
        print("Estudiante:", estudiante.obtener_nombre_completo())
        print("Nota:", estudiante.nota)
        print("Resultado:", resultado)

        return resultado


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

    def evaluar_datos_estudiante(self, estudiante):
        datos = {
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
            "nota": estudiante.nota
        }

        completos = all(
            valor is not None and valor != ""
            for valor in datos.values()
        )

        print("\n--- EVALUACIÓN DE DATOS ---")
        print("Estudiante:", estudiante.obtener_nombre_completo())

        if completos:
            print("Los datos del estudiante están completos.")
        else:
            print("Los datos del estudiante están incompletos.")

        return completos


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

    def registrar_nota(self, estudiante, nota):
        if 0 <= nota <= 100:
            estudiante.nota = nota
            print(
                "\nEl profesor",
                self.informacion["nombre"],
                "registró la nota",
                nota,
                "para",
                estudiante.obtener_nombre_completo()
            )
        else:
            print("\nLa nota debe estar entre 0 y 100.")
