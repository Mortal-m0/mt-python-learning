print("---魔头的装备栏---")
weapon="键盘"
attack_power="999"
weight="1.5"
print(f"我的武器是{weapon},攻击力是{attack_power},重量是{weight}公斤。")
print("---网吧准入判定系统---")
age_str=input("请输入你的年龄:")
age=int(age_str)
if age >= 18:
    print(f"欢迎来到改变世界网吧，请开始你的代码修行！")
elif age >= 12 and age < 18:
    print(f"未成年需要家长陪同才能进入哦。")
else:
    print(f"小朋友，快回家写作业吧！")