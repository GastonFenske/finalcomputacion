
class University:

    def __init__(self, name, address, web):
        self.name = name
        self.address = address
        self.web = web
        #self.list_degrees = list_degrees

    def __str__(self):
        return """
[Nombre de la universidad] {}
[Direccion de la universidad] {}
[Web de la universidad] {}""".format(self.name, self.address, self.web)