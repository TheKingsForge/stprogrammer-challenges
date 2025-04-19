# Challenge 1
## Create a list of your favorite musicians.
favorite_musicians = ["Marty O'Donnell", "Frank Sinatra", "Benny Goodman", "Mariah Carey"]

# Challenge 2
## Create a list of tuples, with each tuple containing the longitude and latitude of somewhere you;ve lived or visited.
cool_places = [(47.3327446,-122.5071871), (44.0273759,-124.1362005), (44.520305,-110.762360), (46.9460071,-91.786446)]

# Challenge 3
## Create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc.
attributes = {"Hair" : "Brown", "Eyes" : "Brown", "Fingers" : 10, "Toes" : 10}

# Challenge 4
## Write a program that lets the user ask your height, favorite color, or favorite author, 
## and returns the result from the dictionary you created in the previous challenge.
key = input ("Type an attribute to return: ")
if key in attributes: 
    key_attribute = attributes[key]
    print (key_attribute)
else: 
    print ("Key not found.")

# Challenge 5
## Create a dictionary mapping your favorite musicians to a list of your favorite songs by them.
favorite_songs = ["MJOLNIR Mix", "Fly Me To The Moon", "Sing. Sing. Sing.", "All I Want For Christmas Is You."]

mapped_songs = {favorite_musicians[0] : favorite_songs[0],
                favorite_musicians[1] : favorite_songs[1],
                favorite_musicians[2] : favorite_songs[2],
                favorite_musicians[3] : favorite_songs[3]}
# Challenge 6
## Lists, tuples, and dictionaries are just a few of the containers built into Python.
## Research Python sets (a type of container). When would you use a set?
# A set holds 
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * set items are unchangeable but items can be added or removed.
# No duplicate items are allowed
# A set would be used when a dataset of unique items needs to be stored.