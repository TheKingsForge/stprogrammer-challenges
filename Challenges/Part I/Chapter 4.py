# The Self Taught Programmer Chapter 4 Challenges

# Challenge 1
## Write a function that takes a number as an input and returns that number squared.
def square_value(number):
    """ Squares the entered number.
    :param number: some number value.
    :return: squared number.
    """
    return number ** 2

# Challenge 2
## Create a function that accepts a string as a parameter and prints it.
def print_string(some_string):
    """ Prints the entered string.
    :param some_string: string to be printed.
    """
    print (some_string)

# Challenge 3
## Write a function that takes three required paramaeters and two optional parameters.
def make_car(color, convertable, engine, make = "Mazda", year = "2015") :
    """ Prints all entered values for the car.
    :param color: color of the car.
    :param convertable: yes or no if the user wants a convertable.
    :param engine: type of engine the user wants.
    :optional param make: make of the car and the default value is Mazda.
    :optional param year: year of the car and the default is 2015.
    """
    print (color)
    print (convertable)
    print (engine)
    print (make)
    print (year)

# Challenge 4
## Write a program with two functions. 
## The first function should take an integer as a parameter and return the result of the integer divided by 2.
## The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
## Call the first function, save the result as a varaible, and pass it as a parameter to the second function.
def div_by_2(number1):
    """ Divides number2 by 2.
    :param number1: number to be divided by 2.
    :return: calulation of entered number divided by 2.
    """
    return number1 / 2

def mult_by_4(number2):
    """ Multiplies number2 by 4
    :param number2: number to be multiplied by 4.
    :return: calculation of entered number multiplied by 4.
    """
    return number2 * 4

# Challenge 5
## Write a function that converts a string to a float and returns the result. 
## Use exception handling to catch the exception that could occur.
def string_to_float(some_other_string):
    """ Converts string to float.
    :param some_other_string: string value to be converted to float.
    :return: entered string value converted to float.
    """
    try:
        return float(some_other_string)
    except ValueError:
        print ("Cannot convert string to float.")
        return 0

# Challenge 6
## Add a docstring to all of the functions you wrote in challenges 1-5.


square_value(5)
print_string("Functions are pretty cool.")
make_car("black", "No", "2.5L")
make_car("black", "No", "3.6L", "Chrysler", 2013)
print (mult_by_4(div_by_2(10)))
print (string_to_float("3.a"))
