# Challenge 1
## Add a square_list class variable to a class called `Square` 
## so that every time you create a new `Square` object,
## the new object gets added to the list.
class Shape():
    def what_am_i(self):
        print("I am a shape!")

class Square(Shape):
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def calculate_perimeter(self):
        return (self.side * 4)

    def change_size(self, new_size):
        self.side += new_size

    def what_am_i(self):
        super().what_am_i()
        print("I am a square!")

    # Challenge 2
    ## Change the `Square` class so that when you print a `Square` object,
    ## a message prints telling you the len of each of the four sides of the shape.
    ## For example, if you create a square with `Square(29)` and print it,
    ## Python should print 29 by 29 by 29 by 29.
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)
    
    
# Challenge 3
## Write a function that takes two objects as parameters
## and returns True if they are the same object, and False if not.
def compare(object1, object2):
    return object1 is object2

## http://tinyurl.com/j9qjnep


squ1 = Square(10)
print(squ1)
squ2 = Square(15)
print(squ2)
squ3 = Square(20)
print(squ3)
squ4 = Square(25)
print(squ4)
print(squ1.square_list)

print(compare(squ1, squ2))
print(compare(squ1, squ1))