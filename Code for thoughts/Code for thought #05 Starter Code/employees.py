### Code for thought #5
### In this assignment, we first read and understand the following code
### The following pizza shop is a composite object: it has an oven, and it has
### employees like servers and chefs. Try to understand when a customer enters and places an
### order, how the components of the shop spring into action.

### Once we understand the code, we run the code and the result will look like the following

##Homer order from <Employee: name = Pat salary = 40000>
##Bob makes pizza
##oven bakes
##Homer pays for item to <Employee: name = Pat salary = 40000>
##...
##Shaggy order from <Employee: name = Pat salary = 40000>
##Bob makes pizza
##oven bakes
##Shaggy pays for item to <Employee: name = Pat salary = 40000>

### We need to add one method to one of the following class so that
### after that the output of the code will look like the following

##Homer order from <Server: name = Pat salary = 40000>
##Bob makes pizza
##oven bakes
##Homer pays for item to <Server: name = Pat salary = 40000>
##...
##Shaggy order from <Server: name = Pat salary = 40000>
##Bob makes pizza
##oven bakes
##Shaggy pays for item to <Server: name = Pat salary = 40000>

### Note we need to determine to which class we will add a method,
### what method we will add, and what code would we write in the
### method.

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveraise(self, percent):
        self.salary += self.salary*percent

    def work(self):
        print(self.name, "does stuff")

    def __str__(self):
        return "<Employee: name = "+ str(self.name) + " salary = " +str(self.salary) +">"

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, "interfaces with customer")

    def __str__(self):
                    return "<Server: name = "+ str(self.name) + " salary = " +str(self.salary) +">"


class PizzaRobot(Chef):
    def work(self):
        print(self.name, "makes pizza")

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "order from", server)

    def pay(self, server):
        print(self.name, "pays for item to", server)

class Oven:
    def bake(self):
        print("oven bakes")

class PizzaShop:
    def __init__(self):
        self.server = Server("Pat")
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

scene = PizzaShop()
scene.order("Homer")
print("...")
scene.order("Shaggy")

