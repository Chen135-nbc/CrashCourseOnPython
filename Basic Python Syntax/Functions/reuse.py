# 不使用reuse
name = "Kay"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))
name = "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

# 封装函数实现reuse
def lucky_number(name1):
    number1 = len(name1) * 9
    print("Hello " + name1 + ". Your lucky number is " + str(number1))

lucky_number("Harry")
lucky_number("Cameron")
lucky_number("Alexander")

