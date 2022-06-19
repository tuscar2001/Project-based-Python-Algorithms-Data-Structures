

class Customer:
    def __init__(self, first_name, last_name, products = None):
        self.first_name = first_name
        self.last_name = last_name
        self.products = products

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
        else:
            print ("Customer {} already has the product {}".format(self.first_name, self.products))

    def remove_product(self,product):
        if product in self.products:
            self.products.remove(product)
        else:
            print ("Course not found")


    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nProducts: {', '.join((map(str.capitalize, self.products)))}"

    #number of products boughts by a customer
    def __len__(self):
        return len(self.products)

    
    def __repr__(self):
        return f"First Name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\nProducts: {self.products.capitalize()}
customer = Customer("John", "Doe", ['BMW','AUDI','HONDA'])
print ("First Name: {}".format(customer.first_name))
print ("Last Name: {}".format(customer.last_name))
print ("Products: {}".format(customer.products))
print (customer.add_product("Mercedes"))
print ("Products: {}".format(customer.products))
print (customer.remove_product("Mercedes"))
print ("Products: {}".format(', '.join(map(str.capitalize,customer.products))))  
print ("__str__ results -----------------")
print (customer) 
print("here are the different things you can do with the customer class")
print (dir(customer))
print ("for instance, let us use the __dict__")
print (customer.__dict__)