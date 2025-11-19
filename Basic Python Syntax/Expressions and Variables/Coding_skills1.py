# 技能组 1
# 使用变量来存储值
hotel_room = 100
tax = hotel_room * 0.05
total = hotel_room + tax
room_guest = 4
# 使用基本算术运算符和变量创建表达式
share_per_person = total / room_guest
# 使用显式转换将数据类型从浮点数更改为字符串。
print("Each person should pay: " + str(share_per_person))







# 技能组 2
# 在一行中输出多个字符串变量，以组成一个句子。
salutation = "Dr."
first_name = "Nancy"
middle_name = "Chen"
Last_name = "Meyer"
# 在print()函数中，使用加号 (+) 或逗号连接字符串。
print(salutation + first_name + middle_name + Last_name)
print(salutation, first_name, middle_name, Last_name)
# 在print()函数中，在变量之间创建空格
print(salutation + " " + first_name + " " + middle_name + " " + Last_name)



# 技能组 3
# 解决由数据类型不匹配问题引起的 TypeError 错误
# 使用显式转换函数
print("5 * 3 = " + str(5 * 3))