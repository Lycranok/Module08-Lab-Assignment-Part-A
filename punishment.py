"""
Kevin Nelson
Module 01 Programming Project
 
This program makes a water cooler class, uses its functions then outputs information about the class
"""

class WaterCooler:
    def __init__(self, location: str, remaining_water: float = 20.0):
        self.location = location
        self.bottles_filled = 0
        self.remaining_water = remaining_water

    def fill_bottle(self):
        if self.remaining_water >= 0.5:
            self.remaining_water -= 0.5
            self.bottles_filled += 1

    def replace_water(self):
        self.remaining_water = 20.0

    def change_location(self, new_location: str):
        self.location = new_location

    def __str__(self):
        return(f"Water cooler located in {self.location} has filled up {self.bottles_filled} bottles and is at {self.remaining_water} gallons of water")

water_cooler_1 = WaterCooler("Break Room", 20.0)
water_cooler_2 = WaterCooler("Office", 50.0)

water_cooler_1.fill_bottle()
water_cooler_1.fill_bottle()
water_cooler_1.fill_bottle()
water_cooler_1.fill_bottle()
water_cooler_1.fill_bottle()
water_cooler_1.fill_bottle()
water_cooler_1.fill_bottle()
water_cooler_1.fill_bottle()
water_cooler_1.replace_water()

water_cooler_2.fill_bottle()
water_cooler_2.change_location("Factory")

print(water_cooler_1)
print(water_cooler_2)