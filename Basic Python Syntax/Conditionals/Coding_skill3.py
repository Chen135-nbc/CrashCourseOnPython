# Skill Group 1
# 使用数字比较运算符
print(10 * 4 > 23 + 14)
# 使用比较运算符对字符串进行字母排序
print( "tall" < "short")


#Skill Group 2
# 使用带有 def() 关键字的函数
# 向函数传递参数
def translate_error_code(error_code):
    #使用 if-elif-else 语句
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthenticated request."
    elif error_code == "404 Not Found":
        # 将字符串赋值给变量
        translation = "Requested web page not found on server"
    # 使用条件运算符
    elif error_code == "408 Request Timeout":
        translation = "Server request to close unused connection"
    else:
        translation = "Server returned an error"
    # 返回值
    return translation

print(translate_error_code("404 Not Found"))

# Skill Group 3
number = 25
# 使用 if-elif-else 语句：
# comparison operators
if number <= 5:
    print("The number is less than 5")
elif number == 33:
    print("The number is equal to 33")
# 逻辑运算符
elif number < 32 and number >= 6:
    print("The number is less than 32 and greater than 6.")
else :
    print("The number is " + str(number))

# Skill Group4
def round_up(number):
    x = 10
    # 回顾一下算术运算符 // 和 %
    whole_number = number // x
    remainder = number % x
    # 使用 if 语句计算返回值
    # 使用条件运算符
    if remainder >= 5:
        return x * (whole_number + 1)
    return x * whole_number

print(round_up(35))




