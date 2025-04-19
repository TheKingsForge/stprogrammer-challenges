# Challenge 1
## Print every character in the string "Camus".
name = "Camus"
print (name[0])
print (name[1])
print (name[2])
print (name[3])
print (name[4])

# Challenge 2
## Write a program that collects two strings from a user, 
## inserts them into the string " Yesterday I wrote a [response_ one]. I sent it to [response_two]!"
## and prints the new string. 
string1 = input("Enter a string!")
string2 = input("Enter another string!")
print ("Yesterday I wrote a {}. I sent it to {}!".format(string1, string2))

# Challenge 3
## Use a method to make the string "aldous Huxley was born in 1894." 
## grammatically correct by capitalizing the first letter in the sentence.
notCapital = "aldous Huxley was born in 1894."
print (notCapital.capitalize())

x = "aldous huxley was born in 1894. he was born in the United Kingdom.".title()
print(x)
# Challenge 4
## Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: 
## ["Where now?", "Who now?", "When now?"].
questions = "Where now? Who now? When now?"
print (questions.split("?"))

# Challenge 5
## Take the list ["The", "Fox", "Jumped", "Over", "The", "Fence", "."] and turn it into a grammatically correct string. 
## There should be  a space between each word, but no space between the word fence and the period that follows it.
## (Don't forget, you learned a method that returns a list of strings into a single string.)
list1 = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(list1)
fox = fox[0:-2] + "."
print (fox)

# Challenge 6
## Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign. 
phrase2 = "A screaming comes across the sky."
print (phrase2.replace('s', '$'))

# Challenge 7
## Use a method to find the first index of the character "m" in the string "Hemingway". 
name = "Hemingway"
print (name.index('m'))

# Challenge 8
## Find dialogue in your favorite book (containing quotes) and turn it into a string. 
print ("Then He said to them, \"So give back to Caeser, what is Caeser's, and to God, what is Gods'.\"")
print ("""\tThen people brought little children to Jesus for him
to place his hands on them and pray for them. But the
disciples rebuked them.
\tJesus said, “Let the little children come to me, and
do not hinder them, for the kingdom of heaven belongs
to such as these.” When he had placed his hands on
them, he went on from there."
""")
print ("“These people honor me with their lips, but their hearts are far from me. They worship me in vain; their teachings are merely human rules.’”")

# Challenge 9
## Create the string "three three three" using concatenation, and then again using multiplication. 
numberString = "three"
print (numberString + numberString + numberString)
print (numberString * 3)

# Challenge 10
## Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." 
## to only include the letters before the comma.
opening1984 = "It was a bright cold day in April, and the clocks were striking thirteen."
print (opening1984[:33])