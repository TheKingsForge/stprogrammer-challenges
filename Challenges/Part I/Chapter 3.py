# The Self Taught Programmer Chapter 3 Challenges

# Challenge 1
## Print three different strings.

print ("Hello, world!")
print ("This is a second string being printed.")
print ("A third string... very nice!")

# Challenge 2
## Write a program that prints a message if a variable is less than 10, 
## and a different message if the variable is greater than or equal to 10.

cars = 5
if (cars < 10):
    print ("You don't have enough cars.")
else:
    print ("You have at least 10 cars! You need a bigger garage.")

# Challenge 3
## Write a program that prints a message if a variable is less than or equal to 10, 
## another message if the variable is greater than 10 but less than or equal to 25, 
## and another message if the variable is greater than 25.

garageSpaces = 6
if (garageSpaces <= 10):
    print ("You have 10 or less garage spaces. Keep going!")
elif (garageSpaces <= 25):
    print ("You have more than 10 and at most 25 garage spaces. Getting there!")
else:
    print ("You have more than 25 garage spaces. That's probably enough. Probably...")

# Challenge 4 
## Create a program that divides two varaibles and prints the remaineder
number1 = 10
number2 = 11
print (11 % 10)

# Challenge 5
# Create a program that takes two varaibles, divides them, and prints the quotient.
number1 = 10
number2 = 11
print (11 // 10)

# Challenge 6
## Write a prigram with a variable "age" assigned to an integer that prints 
## different strings depending on what the integer age is. 
age = 17
if (age < 18):
    print ("Live while you're young kid.")
else: 
    print ("Welcome to the jungle!")