

class Customer:
    def __init__(self, first_name, last_name, products = None):
        self.first_name = first_name
        self.last_name = last_name
        self.products = products


customer = Customer("John", "Doe", ['BMW','AUDI','HONDA'])
print ("First Name: {}".format(customer.first_name))
print ("Last Name: {}".format(customer.last_name))
print ("Products: {}".format(customer.products))