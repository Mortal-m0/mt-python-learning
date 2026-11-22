hero_name="Zero"
power_level=99
speed=8.5
print(f"我是{hero_name},我的战斗力是{power_level},速度是{speed}.")
print("---游戏准入判定---")
level_str=input("请输入你的角色等级：")
level=int(level_str)
if level >=50:
    print(f"欢迎进入高级副本，BOSS在里面等你！")
elif level >=20 and level<50:
    print(f"你已进入中级区，请继续打怪升级。")
else:
    print(f"新手村欢迎你，先去砍几只史莱姆吧。")