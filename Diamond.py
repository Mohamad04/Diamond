

# Write a Python program that prompts the user to enter a number of rows and then generates a symmetrical "palindrome" star pattern, centered to form a diamond shape. Example: 
# For rows =5, 
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


user_input =  int(input("Enter the number of rows : "))
nb_of_diamonds = "*"
nb_of_spaces = user_input - 1

# first half of the diamond shape
for i in range(1, user_input+1):
        display_msg = " " * nb_of_spaces + nb_of_diamonds
        print(display_msg)
        nb_of_diamonds += "**"
        nb_of_spaces -= 1

# second half of the diamond shape
nb_of_diamonds = "*"
nb_of_spaces = 1
for i in range(user_input-1, 0, -1): 
        display_msg = " " * nb_of_spaces + nb_of_diamonds * ((i * 2) - 1)  
        print(display_msg )
        nb_of_spaces += 1
        
    