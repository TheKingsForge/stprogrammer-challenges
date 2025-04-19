# Challenge 1
## Find a file on your computer and print its contents using Python.
with open("C:\\Users\\Zachk\\OneDrive\\Desktop\\TEMP\\MassEffect5e\\Mass Effect Mission 2 Hostage Rescue.md", "r") as mass_effect_info:
    mass_effect_info_text = mass_effect_info.read()
    print(mass_effect_info_text)

# Challenge 2
## Write a program that asks a user a question, 
## and saves their answer to a file.
answer = input("What is your favorite color?\n")
with open("answer.txt", "w+") as answer_txt:
    answer_txt.write(answer)

# Challenge 3
## Take the items in this list of lists: 
## [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
## and write them to a CSV file. The data from each list should be a row in the file, with each item in the list separated by a comma.
import csv
movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w+") as movies_list:
    movies_list_csv = csv.writer(movies_list)
    for title_row in movies:
        movies_list_csv.writerow(title_row)