print(f"---改造你的“火球术模拟器”---")
def cast_spell(times):
    total_damage=0
    for i in range(1,times+1):
        total_damage=total_damage+100
        print(f"第{i}次释放火球,造成100点伤害!")
    print(f"施法结束,累计造成{total_damage}点伤害!")
cast_spell(3)