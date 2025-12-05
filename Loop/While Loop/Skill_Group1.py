# Skill Group1
# 初始化变量
def count_factors(given_number):
    factor = 1
    count = 1
    if given_number == 0:
        return 0
# 使用while循环，当特定条件为真时运行。
    while factor < given_number:
        # 确保while循环不会变成无限循环
        if given_number % factor == 0:
            count += 1
        #在while循环中递增一个值
        factor += 1
    return count

print(count_factors(0))
print(count_factors(3))
print(count_factors(10))

# Skill Group2
# 在while循环 中使用变量之前，先初始化变量并分配数据类型。
def addition_table(given_number):
    iterated_number = 1
# 使用break关键字作为while循环的退出点
    while iterated_number <= 5:
        my_sum = given_number + iterated_number
        if my_sum > 20:
            break
        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
        iterated_number += 1

addition_table(5)
addition_table(17)
addition_table(30)