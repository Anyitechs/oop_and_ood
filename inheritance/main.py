"""Inheritance basically provides a way to create a class from an existing class.
    This can exist whereever there's a IS-A relationship. A good example is Square and Shape.
    A Square IS-A type/kind of Shape. So the Shape is the base class, while the Square is a
    derived class. 

    There are many forms of Inheritance:
    - Single Inheritance
    - Multiple ,,
    - Multi-level ,,
    - Hierarchical ,,
    - Hybrid ,,
"""
# Base Class (Parent Class)
class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_name(self):
        print("The car is a, ", self.name, self.model, end="")

# Single Inheritance  
# FuelCar is extending from the Vehicle class
# Derived Class (Child)
class FuelCar(Vehicle):
    def __init__(self, name, model, combust_type):
        Vehicle.__init__(self, name, model)
        self.combust_type = combust_type

    def get_fuel_car(self):
        super().get_name()
        print(", combust type is ", self.combust_type, end="")

# Hierarchical Inheritance
# Alongside the FuelCar class, the ElectricCar class is also extending from Vehicle class
# Another Derived class (Child)
class ElectricCar(Vehicle):
    def __init__(self, name, model, battery_power):
        Vehicle.__init__(self, name, model)
        self.battery_power = battery_power

    def get_electric_car(self):
        super().get_name()
        print(", battery power is ", self.battery_power, end="")

# Multi-level Inheritance
# GasolineCar is derived from the FuelCar class which in turn is derived from the Vehicle class
# Derived class (Grandchild)
class GasolineCar(FuelCar):
    def __init__(self, name, model, combust_type, gas_capacity):
        FuelCar.__init__(self, name, model, combust_type)
        self.gas_capacity = gas_capacity

    def get_gasoline_car(self):
        super().get_fuel_car()
        print(", gas capacity", self.gas_capacity, end="")

# Hybrid Inheritance
# The HybridCar class is derived from two different classes, The GasolineCar class and the ElectricCar class 
# Derived class
class HybridCar(GasolineCar, ElectricCar):
    def __init__(self, name, model, combust_type, battery_power):
        FuelCar.__init__(self, name, model, combust_type)
        ElectricCar.__init__(self, name, model, battery_power)
        self.battery_power = battery_power

    def get_hybrid_car(self):
        super().get_fuel_car()
        print(", battery power is", self.battery_power)


# main
def main():
    print("Single Inheritance:")
    Fuel = FuelCar("Honda", "Accord", "Petrol")
    Fuel.get_fuel_car()
    print("\n")

    print("Hierarchical Inheritance:")
    Electric = ElectricCar("Tesla", "ModelX", "200MWH")
    Electric.get_electric_car()
    print("\n")

    print("Multi-level Inheritance:")
    Gasoline = GasolineCar("Toyota", "Corolla", "Gasoline", "30 liters")
    Gasoline.get_gasoline_car()
    print("\n")

    print("Multiple Inheritance:")
    Hybrid = HybridCar("Toyota", "Prius", "Hybrid", "100MWH")
    Hybrid.get_hybrid_car()

if __name__ == "__main__":
    main()