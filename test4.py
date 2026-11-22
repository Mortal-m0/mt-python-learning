print("---你加班到凌晨，肚子饿了想去吃顿宵夜。---")
money_str=input("请输入你口袋里有多少钱：")
money=float(money_str)
cost_str=input("请输入这顿宵夜要花多少钱：")
cost=float(cost_str)
left_money=money-cost
short_money=cost-money
if money >= cost:
    print(f"太好了！买得起，吃完还剩{left_money}块钱！")
else:
    print(f"钱不够啊兄弟，还差{short_money}块钱！")