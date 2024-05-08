# import the string and random modules
import string
import random

print( "Hello this is a secure password generator" )
# ask the user for the desired length of the password
print( "Please enter password length required " )
B = input( )
B = int (B)

#addds extra special character
string3 = "!@#$%^&*()-_=+\|[]{};:/?.>"

# define the characters that can be used in the password
passw = string.ascii_letters + string.digits + string.punctuation + string3


# generate a password using randomly chosen characters
# using the 'choices' function from the random module
# and joining the resulting characters into a string
password = ''.join(random.choices(passw, k=B))

# display the generated password to the user
print("Your password is:", password)