#!bin/bash
# Challenge 1
## Print `Self-taught` in Bash
echo self-taught

# Challenge 2
## Navigate to your home directory from another directory
## using an absolute and relative path.
cd /home/zking # Absolute
cd home/zking # Relative

# Challenge 3 
## Create an environmental variable called `$python_projects` 
## That is an absolute path to the directory where you keep your Python files. 
## Save the variable in your .profile file 
## and then use the command `cd $python_projects` to navigate there.
export python_projects=/mnt/c/Users/Zachk/OneDrive/Documents/Programming/Self-Taught-Programmer/Exercises

# To persist this line, save it into the .profiles file. I did this using `vim .profiles` and added it in the file.
# NOTE this line doesn't work if you put spaces on either side of the equals sign.