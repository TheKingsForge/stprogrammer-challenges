import math

# Challenge 1
## Define a class called "Apple" with four instance variables that represent four attributes of an apple.
class Apple():
    def __init__(self, color, apple_name, size, stem):
        self.color = color
        self.apple_name = apple_name
        self.size = size
        self.has_stem = stem

# Challenge 2
## Create a Circle class with a method called area that calculates and returns its area.
## Then create a Circle object, call area on it, and print the result. Use Python's pi function in the built-in math module.
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * pow(self.radius, 2)

# Challenge 3
## Create a Triangle class with a method called area that calculates and returns its area.
## Then create a Triangle object, call area on it, and print the result. 
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return .5 * self.base * self.height
    
# Challenge 4
## Make a Hexagon class with a method called "calculate_perimeter" that calculates and returns its perimeter.
## Then create a Hexagon object, call "calculate_perimeter" on it, and print the result. 
class Hexagon():
    def __init__(self, side1, side2, side3, side4, side5, side6):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = side5
        self.side6 = side6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6
    

apple = Apple("red", "macintosh", "medium", True)
print(apple.apple_name)
print(apple.color)
print(apple.size)
print(apple.has_stem)

radius = 2
circle = Circle(radius)
print("The area of a circle with radius {} is {}".format(radius, circle.get_area()))

base = 2
height = 4
triangle = Triangle(base, height)
print("The area of a triangle with base {} and height {} is {}"\
      .format(base, height, triangle.get_area()))

hexagon = Hexagon(1,2,3,4,5,6)
print("The perimeter of a hexagon with side lengths {}, {}, {}, {}, {}, {} is {}" \
      .format(1, 2, 3, 4, 5, 6, hexagon.calculate_perimeter()))

