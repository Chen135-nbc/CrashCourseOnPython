# PART 1: The and Logical Operator
print((6*3 >= 18) and (9+9 <= 36/2))  # True and True => True
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi") #False and True => False

# PART 2: The or Logical Operator
country = "United States"
city = "New York City"
# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))  # True or True = True

# False or True returns True
print(country == "New York City" or city == "New York City")  # False or True = True

# True or False returns True
print(16 <= 4 ** 2 or 9 ** 0.5 != 3)  # True or False = True

# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name") # False or False = False

# PART 3: The not Logical Operator
x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)
# ----- Example 2 ------
today = "Monday"
print(not today == "Tuesday")

