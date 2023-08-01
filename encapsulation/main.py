"""Encapsulation simply refers to binding data and methods that manipulates the
    data in a single unit called CLASS. Below is a simple implementation of this OOP
    principle in python.
"""

class Movie:
    def __init__(self, title="", year="", genre=""):
        self.title = title
        self.year = year
        self.genre = genre

    """How do you access the data/attributes of the class? You can achieve this by
        implementing getters and setters, or any other public methods.
        Let's dive into that below.
    """
    
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
    
    def get_genre(self):
        return self.genre
    
    def set_genre(self, genre):
        self.genre = genre
    
    def print_details(self):
        print("Title -- ", self.title)
        print("Year -- ", self.year)
        print("Genre -- ", self.genre)

def main():
    movie = Movie(title="The Passion of the Christ", year="2004", genre="Drama")
    movie.print_details()

    print("---")
    movie.set_title("War room")
    print("New title --- ", movie.get_title())
    print("---")
    movie.print_details()

if __name__ == "__main__":
    main()