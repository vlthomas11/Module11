class Customer:

    # Constructor
    def __init__(self, customerID, lname, fname, phone, addr):
        if (not isinstance(customerID,int)):
            raise ValueError("% is not a valid CustomerID" % customerID)
        self.ID = customerID
        self.first_name = fname
        self.last_name = lname
        self.phone_num = phone
        self.address = addr

    def set_id(self, customerID):
        self._ID = customerID

    def set_last_name(self, lname):
        self._last_name = lname

    def set_first_name(self,fname):
        self._first_name = fname

    def set_phone_num(self,phone):
        self._phone_num = phone

    def set_address(self,addr):
        self._address = addr

    def display(self):
        return 'Customer ID: ' + str(self._ID) + '\nName: ' + str(self._first_name) + ' ' + str(
            self._last_name) + '\nPhone Number:' + str(self._phone_num) + '\nAddress: ' + str(self._address)



class Invoice:

    def __init__(self,invoiceid,CustomerObject,items =''):

        self._inoviceID = invoiceid
        self._customerID = CustomerObject.ID
        self._last_name = CustomerObject.last_name
        self._first_name = CustomerObject.first_name
        self._phone_number = CustomerObject.phone_num
        self._address = CustomerObject.address
        self._items_with_price = dict()
        self._total = 0
        self._tax = 0
        self._total_with_tax = 0

    def set_total(self):
        self._total = 0

    def set_items_with_price(self,_items_with_price):
        self._items_with_price = dict()

    def add_item(self,item):
        self._items_with_price.update(item)

    def total_price (self):
        for v in self._items_with_price:
            self._total += self._items_with_price.get(v)

    def calc_tax(self):
        self._tax = self._total * .06
        self._tax = round(self._tax,2)

    def total_with_tax(self):
        self._total_with_tax = self._total + self._tax

    def create_invoice(self):
        return "Name: " + str(self._first_name) + ' ' + str(self._last_name) + \
               '\nCustomerID: ' + str(self._customerID) + \
               '\nPhone number: ' + str(self._phone_number) + \
               '\nAddress:' + str(self._address) +\
               '\nItems: ' + str(self._items_with_price) + \
               '\nTotal before tax: ' + str(self._total) + \
               '\nTax: ' + str(self._tax) + \
               '\nTotal: '  + str(self._total_with_tax)


# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.total_price()
invoice.calc_tax()
invoice.total_with_tax()
print(invoice.create_invoice())

