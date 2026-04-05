"""
Kevin Nelson
Module 05 Lab Assignment
 
This program makes a Super class and then subclasses then makes objects for each class, runs all functions related to them then outputs all data about each object.
"""

class InventoryItem:
    def __init__(self, name: str, quantity: int, price: float):
        self._name = name
        self._quantity = quantity
        self._price = price

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def set_price(self, new_price: float):
        if new_price < 0.01:
            print("Price cannot be below 1 cent.")
            return

        lower_bound = self._price * 0.5
        upper_bound = self._price * 1.5
        if new_price < lower_bound or new_price > upper_bound:
            print("Price change cannot exceed 50%.")
            return
        
        self._price = new_price

    def add_stock(self, amount: int):
        if amount > 0:
            self._quantity += amount

    def remove_stock(self, amount: int):
        if amount > 0:
            self._quantity = max(0, self._quantity - amount)
    
    def clearance(self, reduction_amount: float):
        new_price = self._price - reduction_amount
        if new_price >= 0.01:
            self._price = new_price
        else:
            print("Clearance price cannot be below $0.01")

    def __str__(self):
        return (f"Product Name: {self.get_name()}\n"
                f"  Quantity: {self.get_quantity()}\n"
                f"  Price: ${self.get_price():.2f}")

class PerishableItem(InventoryItem):
    def __init__(self, name, quantity, price, perishable: bool, expiration_date: str):
        super().__init__(name, quantity, price)

        self._perishable = perishable
        self._expiration_date = expiration_date

    def get_perishable(self):
        return self._perishable
    
    def get_expiration_date(self):
        return self._expiration_date
    
    def set_perishable(self, status: bool):
        self._perishable = status

    def set_expiration_date(self, date: str):
        self._expiration_date = date

    def clearance(self):
        reduction_amount = self._price - (self._price * 0.1)

        super().clearance(reduction_amount)

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"  Perishable: {self.get_perishable()}\n"
                f"  Expiration Date: {self.get_expiration_date()}")

class ElectronicItem(InventoryItem):
    def __init__(self, name, quantity, price, warranty: int, return_period: int, serial_number: int):
        super().__init__(name, quantity, price)

        self._warranty = warranty
        self._return_period = return_period
        self._serial_number = serial_number

    def get_warranty(self):
        return self._warranty
    
    def get_return_period(self):
        return self._return_period
    
    def get_serial_number(self):
        return self._serial_number
    
    def set_return_period(self, return_period: int):
        self._return_period = return_period

    def purchase_warranty(self):
        self._warranty += 180
        self._return_period += 180

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"  Warranty: {self.get_warranty()} Days\n"
                f"  Return Period: {self.get_return_period()} Days\n"
                f"  Serial Number: {self.get_serial_number()}")

Item = InventoryItem("Bed", 5, 200.00)
Item.set_price(300.00)
Item.add_stock(10)
Item.remove_stock(7)
Item.clearance(250.00)
print(Item)

Milk = PerishableItem("Milk", 60, 8.00, False, "1-1-1")
Milk.set_price(10.00)
Milk.add_stock(200)
Milk.remove_stock(26)
Milk.set_perishable(True)
Milk.set_expiration_date("5-5-5")
Milk.clearance()
print(Milk)

Computer = ElectronicItem("Computer", 3, 500.00, 50, 55, 2782781)
Computer.set_price(600.00)
Computer.add_stock(1)
Computer.remove_stock(3)
Computer.clearance(50.00)
Computer.set_return_period(20)
Computer.purchase_warranty()
print(Computer)