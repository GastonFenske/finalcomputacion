
class Inscription:

    def __init__(self, student, subject, date_inscription):
        self.student = student
        self.subject = subject
        self.date_inscription = date_inscription

    def __str__(self):
        return """
[Estudiante] {}
[Materia] {}
[Fecha] {}""".format(self.student, self.subject, self.date_inscription)