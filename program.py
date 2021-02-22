from consts import *
from university import University
from degree import Degree
from inscription import Inscription
from subject import Subject
from student import Student

UM = University(university_name, university_address, university_web)

degree1 = Degree(name_degree1, description_degree1, [], [], UM)

degree2 = Degree(name_degree2, description_degree2, [], [], UM)

degree3 = Degree(name_degree3, description_degree3, [], [], UM)

list_degrees = [degree1, degree2, degree3]


for i in range(len(list_subjects_degree1)):
    subject = Subject(list(list_subjects_degree1.keys())[i], list(list_subjects_degree1.values())[i])
    degree1.list_subjects.append(subject)

for i in range(len(list_subjects_degree2)):
    subject = Subject(list(list_subjects_degree2.keys())[i], list(list_subjects_degree2.values())[i])
    degree2.list_subjects.append(subject)

for i in range(len(list_subjects_degree3)):
    subject = Subject(list(list_subjects_degree3.keys())[i], list(list_subjects_degree3.values())[i])
    degree3.list_subjects.append(subject)


s = Student("Gaston", "Fenske", 42265179, "s.fenske@alumno.edu.ar")

if Student.dni_validation(s) == True:
    i = Inscription(s, degree1.list_subjects[0], "22/02/2020")
    print("Inscripcion creada correctamente:\n{}".format(i))


