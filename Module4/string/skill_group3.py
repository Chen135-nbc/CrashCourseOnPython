# Within the format() parameters, select characters at specific index [ ] positions from a variable string.

# Use the format() method, with {} placeholders for variable data, to create a new string.

def username(last_name, birth_year):

    return "{}{}".format(last_name[0:3], birth_year)

print(username("John", "1989"))
print(username("Nancy", "1997"))
print(username("Heinrich", "1999"))