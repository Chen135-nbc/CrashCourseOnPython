# Returning values
def volume (a,b,c):
    return a*b*c

volume_a = volume(3,5,8)
volume_b = volume(4,6,9)

print("The volume of the cuboid is " + str(volume_a))
print("The volume of the cuboid is " + str(volume_b))

def cube_volume (a):
    return a**3
volume_c = cube_volume(3)
print("The volume of the cube is " + str(volume_c))