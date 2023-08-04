"""Polymorphism allows an object to have several different forms and behaviours.
    Forms of Polymorphism:
    - Dynamic Polymorphism (Have to do with Nethod Overriding)
    - Static Polymorphism (Have to do with Method/Operator Overloading)
"""

class Animal:
    def __init__(self):
        pass

    def print_animal():
        print("Animal object from the Animal class")
    
    def print_animal2():
        print("Second animal object from the animal class")

class Lion(Animal):
    def __init__(self):
        super()
    
    def print_animal():
        print("I'm a Lion")

def main():
    lion = Lion
    lion.print_animal()
    lion.print_animal2()

if __name__ == "__main__":
    main()

