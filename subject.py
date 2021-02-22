
class Subject:

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return """
[Nombre de la materia] {}
[Codigo de la materia] {}""".format(self.name, self.code)