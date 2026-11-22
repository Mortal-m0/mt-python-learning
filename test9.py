print("---魔头施法模拟器---")
skill_name="火球术"
times_str=input("你想连续释放几次技能?(1-10次):")
times=int(times_str)
total_damage=0
if times<=0:
    print(f"次数不能小于1,你被敌人嘲笑了!")
elif times>5:
    print(f"法力值不够支撑这么多次施法,强制退出!")
else:
    for i in range(1,times+1):
        total_damage=total_damage+100
        print(f"第{i}次释放{skill_name},造成100点伤害!")
    print(f"施法结束,累计造成{total_damage}点伤害!")