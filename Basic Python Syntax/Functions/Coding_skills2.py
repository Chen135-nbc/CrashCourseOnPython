# Skill Group 1
# 使用接受多个参数的函数
def volume_of_column(radium, height):
    pi = 3.14
    volume = radium * pi * height / 2
    #  返回结果值
    return volume
print(volume_of_column(5, 3))
print(volume_of_column(7, 10))


# Skill Group 2
# 使用函数返回单位转换的结果
# 使用算术运算符进行计算
def convert_volume(fluid_ounce):
    ml = fluid_ounce * 29.5
    return ml

# 在 print() 语句中将文本与函数调用结合起来
print(convert_volume(33))

# 将 print() 函数的返回值从浮点数据类型转换为字符串。
print("The volume in milliliters is " + str(convert_volume(33)))
# 调用该函数并在 print() 语句中对返回值执行计算。
print("The volume in milliliters is " + str(convert_volume(20)*2))