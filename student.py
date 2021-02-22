
class Student:

    def __init__(self, name, last_name, dni, email):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.email = email

    def dni_validation(self):
        #no se puede llenar el dni con letras y el numero de dni debe tener un len de 8
        if type(self.dni) == int:
            self.dni = str(self.dni)
            if len(self.dni) == 8:
                return True
            else:
                print('Ingrese un dni de 8 caracteres')
        else:
            print('Ingrese un dni con numeros')

    def __str__(self):
        return """
[Nombre alumno] {}
[Apellido alumno] {}
[DNI alumno] {}
[Email alumno] {}""".format(self.name, self.last_name, self.dni, self.email)
