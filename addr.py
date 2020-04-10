
class Address:
    """Address class for US addresses"""
    def __init__(self, st_number, st_name, st_type, city, state, zip, apt_num=''):
        self.street_number = st_number
        self.street_name = st_name
        self.street_type = st_type
        self.apartment_number = apt_num
        self.city = city
        self.state = state
        self.zip_code = zip

    def display(self):
        return(self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number
               + '\n' + self.city + ', ' + self.state + ' ' + self.zip_code)

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

# Driver
addy1 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
person1 = Person('Hammer', 'Martin', addy1)
print(person1.display())
# apartemnt number is at the end. Why?
addy2 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
person2 = Person('Hammer', 'Martin', addy2)
print(person2.display())
del(addy1, addy2)
del(person1, person2)