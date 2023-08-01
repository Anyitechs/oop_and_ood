"""Abstraction focuses only on revealing the neccessary details of a system and
    hiding irrelevant information to minimize it's complexity. It simpply means
    to show what an object does and how it hides.
"""

class Circle:
    def __init__(self, radius=None):
        self.radius = radius
        self.pi = 3.142
    
    def area(self):
        return self.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * self.pi * self.radius
    
def main():
    circle = Circle(5)
    print("Area: {:.2f}".format(circle.area()))
    print("Perimeter: {:.2f}".format(circle.perimeter()))

if __name__ == "__main__":
    main()