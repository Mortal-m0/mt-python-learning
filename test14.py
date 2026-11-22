print("---魔头的背包管理系统---")
inventory=["木剑","红药水","回城卷轴"]
print(inventory)
print(inventory[0])
print(inventory[-1])
inventory.append("屠龙刀")
print(f"添加一件新物品!当前物品总数:{len(inventory)}个")
print("---开始清点物品:---")
for s in inventory:
    print(f"物品{s}")