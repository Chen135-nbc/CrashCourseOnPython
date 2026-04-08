# 使用 while 循环和 if else 语句来管理字典
# 商品库存管理系统
inventory = {} #商品名 → 数量
while True:
    # 显示菜单
    print("1 Add product")
    print("2 Show inventory")
    print("3 Update quantity")
    print("4 Delete product")
    print("5 Exit")
    
    # 用户输入
    choice = input("Choose:")
    
    # Function 1: Add product
    if choice == "1":
        name = input("Product name:")
        quantity = int(input("Quantity:"))
        inventory[name] = quantity
    
    # Function 2: Show inventory
    elif choice == "2":
        if not inventory:
            print("Inventory is empty")
        else:
            for name, quantity in inventory.items():
                print(f"{name} : {quantity}")

    
    # Function 3: Update quantity (判断是否存在)
    elif choice == "3":
        name = input("Product name:")
        if name in inventory:
            inventory[name] = int(input("New quantity:"))
        else:
            print("Product doesn't exist")
    
    # Function 4: Delete product (判断是否存在)
    elif choice == "4":
        name = input("Name:")
        if name in inventory:
            del inventory[name]
        else:
            print("Product doesn't exist")
    
    # Function 5: Exit
    elif choice == "5":
        break
    
    else:
        print("Invilid choice")