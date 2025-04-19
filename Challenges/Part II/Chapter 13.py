# Challenge 1
## Create `Rectangle` and `Square` classes with a method called `calculate_perimeter` 
## that calculates the perimeter of the shapes they represent. 
## Create `Rectangle` and `Square` objects and call the method on both of them.
class Shape():
    def what_am_i(self):
        print("I am a shape!")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return (self.side * 4)

    def change_size(self, new_size):
        self.side += new_size

rec1 = Rectangle(2,3)
squ1 = Square(2)

print(rec1.calculate_perimeter())
print(squ1.calculate_perimeter())

squ1.change_size(-1)
print(squ1.calculate_perimeter())
squ1.change_size(2)
print(squ1.calculate_perimeter())

squ1.what_am_i()
rec1.what_am_i()
# Challenge 2 
## Define a method in your Square class called change_size that allows you to pass in a number
## that increases or decreases (if the number is negative) each side of a square object by that number.

# Challenge 3
## Create a class called `Shape`. Define a method in it called `what_am_i` that prints 
## "I am a shape" when called. Change your Square and Rectangle classes from the previous challenges to in inherit from Shape, 
## create square and rectangle objects, and call the new method on both of them.

# Challenge 4
## Create a class called `Horse` and a class called `Rider`. Use composition to model a horse that has a rider.
class Rider():
    def __init__(self, name):
        self.name = name

class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider
    
    def get_team(self):
        print("My name is: {}".format(self.name))
        print("My rider's name is {}".format(self.rider.name))

rider1 = Rider("Merlin")
horse1 = Horse("Maverick", rider1)

horse1.get_team()

# Solutions: http://tinyurl.com/hz9qdh3
