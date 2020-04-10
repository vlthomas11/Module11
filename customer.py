class Customer:

    # Constructor
    def __init__(self, customerID, fname, lname, phone, addr):
        if (not isinstance(customerID,int)):
            raise ValueError("% is not a valid CustomerID" % customerID)

        self._ID = customerID
        self._first_name = fname
        self._last_name = lname
        self._phone_num = phone
        self._addresss = addr

    def set_id(self, customerID):
        self._ID = customerID

    def set_last_name(self, lname):
        self.last_name = lname

    def display(self):
        return 'Customer ID: ' + str(self._ID) + '\nName: ' + str(self._first_name) + ' ' + str(
            self._last_name) + '\nPhone Number:' + str(self._phone_num) + '\nAddress: ' + str(self._addresss)


# Driver
customer1 = Customer(12346, 'Vickilee', 'Thomas', '(555)-555-5555', '109 se 10th lane')
customer2 = Customer('ABC', 'Ryan', 'Jones', '(444)-444-4444', '901 ne 11th lane')
print(customer1.display())
print(customer2.display())

del customer1
del customer2
