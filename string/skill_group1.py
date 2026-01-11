# Use a for loop to iterate through each letter of a string.

# Add a character to the front of a string.

# Add a character to the end of a string.

# Use the .lower() string method to convert the case (uppercase/lowercase) of the letters within a string variable.

def mirrored_string(my_string):
    forwards = ""
    backwards = ""

    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards += character + backwards

    if  forwards.lower() == backwards.lower():
        return True
    return False

print(mirrored_string("12 Noon"))
print(mirrored_string("Was it a car or cat I saw"))
print(mirrored_string("'eve, Madam Eve")