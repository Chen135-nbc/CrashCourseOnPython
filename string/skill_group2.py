
#
def convert_weight(ounces):
    pounds = ounces/16
    # Use the format() method, with {} placeholders for variable data, to create a new string.
    # Use a formatting expression, like {:.2f},
    # to format a float variable and configure the number of decimal places to display for the float.


    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result

print(convert_weight(12))
print(convert_weight(50.5))
print(convert_weight(16))