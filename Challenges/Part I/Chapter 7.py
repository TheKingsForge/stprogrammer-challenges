# Challenge 1
## Print each item in the following list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"].
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in shows: 
    print(show)

# Challenge 2
## Print all the numbers from 25 to 50
for i in range(25,51):
    print(i)

# Challenge 3
## Print each item in the list from the first challenge and their indexes.
for i, show in enumerate(shows):
    print("{}: {}".format(i, show))

# Challenge 4
## Write a program with an infinite loop
## (with the option to type q to quit)
## and a list of numbers. Each time through the loop ask the user to guess a number on the list
## and tell them whether or not they guessed correctly.
numbers = [10, 75, 0, 117, 316, 777]
print("Enter \"q\" to exit...")
while True:
    guess = input("Guess a number:\n")
    if(guess.upper() == "Q"):
        break
    try:
        guess = int(guess)
        if(guess in numbers):
            print("{} is in the list! :D".format(guess))
        else:
            print("Your guess was incorrect :(")
    except ValueError:
        print("Please type a number or q to quit.")
    
# Challenge 5
## Multiply all the numbers in the list [8, 19, 148, 4] 
## with all the numbers in the list [9, 1, 33, 83], and append each result to a third list.
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
all_products = []
for i in list1:
    for j in list2:
        all_products.append(i * j)
print(all_products)