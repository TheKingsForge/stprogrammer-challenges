# Challenge 1
## Call a different function from the 'statistics' module.
import statistics
nums = [22, 13, 777, 316, 117, 0, 2, 10]

print(statistics.median_high(nums))

# Challenge 2
## Create a module named cubed with a function that takes a number as a parameter,
## and returns the number cubed. Import and call the function from an other module. 
import Cubed

print(Cubed.cubed_num(input("Enter a number to cube:\n")))