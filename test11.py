print("---魔头的任务结算系统---")
def settle_mission(base_money,hours):
    total_gold=base_money+(hours*50)
    print(f"基础金币{base_money},加班{hours}小时,总计获得{int(total_gold)}金币!")
    if total_gold>=500:
        print(f"今晚可以加个大鸡腿了!")
    else:
        print(f"继续努力,离改变世界不远了!")
m=input("请输入任务基础金币:")
money=float(m)
h=input("请输入加班小时数:")
hour=float(h)
settle_mission(money,hour)