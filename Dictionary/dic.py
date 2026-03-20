# 使用 while 循环和 if else 语句来管理字典
# 写一个简单程序管理联系人
contacts = {}
while True:
    print("1 Add contact:")
    print("2 Show contacts:")
    print("3 Delete contact:")
    print("4 Exit")
    # 用户输入
    choice = input("Choose:")   #input() 得到的是字符串
    
    # 功能1：添加联系方式
    if choice == "1":
        name = input("Name:")
        phone = input("Phone:")
        contacts[name] = phone
        
    # 功能2: 显示联系方式（要遍历字典）
    elif choice == "2":
        for name,phone in contacts.items():
            print(f"{name}:{phone}")
            
    # 功能3: 删除联系方式
    elif choice == "3":
        name = input("Name:")
        del contacts[name]
        
    # 功能4: Exit (单独判断)
    elif choice == "4":
        break 
    else:
        print("Invalid choice")
    