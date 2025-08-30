class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 9
customer1.addCart()
customer2= Customer()
customer2.name = "gang"
customer2.lastName = "Bad"
customer2.age = 28
customer3 = Customer()
customer3.name = "good"
customer3.lastName = "Boy"
customer3.age = 15
customer2.addCart()
customer3.addCart()
