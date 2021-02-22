
class Degree:

    def __init__(self, name, description, list_subjects, list_students, university):
        self.name = name
        self.description = description
        self.list_subjects = list_subjects
        self.list_students = list_students
        self.university = university

    def __str__(self):
        return """
[Nombre de la carrera] {}
[Descripcion de la carrera] {}
[Lista de materias de la carrera] {}
[Lista de estudiantes] {}
[Universidad] {}""".format(self.name, self.description, self.list_subjects, self.list_students, self.university)



