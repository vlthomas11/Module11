class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address.display()

class Student:

    def __init__(self,lname,fname,major,gpa):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def set_major(self,major):
        self.major = major

    def set_gpa(self,gpa):
        self.gpa = gpa

    def change_major(self,major):
        self.major = major

    def change_gpa(self,gpa):
        self.gpa = gpa

    def display(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

per = Person('Thomas','Vickilee')
per.display()
stud = Student(per,'CIS',4.0)
stud.change_major('Being Awesome')
stud.change_gpa(3.0)
print(stud.display())