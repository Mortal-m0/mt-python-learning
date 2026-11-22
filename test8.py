print("---魔头初战大魔王---")
player_hp=100 
boss_hp=150
attack=input("请输入你的攻击力(1-50):")
player_attack=float(attack)
for i in range(1,4):
    boss_hp=boss_hp-player_attack
    print(f"第{i}回合,你砍了Boss{attack}滴血,Boss还剩{boss_hp}滴血!")
    player_hp=player_hp-20
    print(f"Boss反击,扣你的血,你还剩{player_hp}滴血!")
if boss_hp<=0:
    print(f"太强了魔头!大魔王被你砍死了!")
else:
    print(f"你没能杀掉大魔王,快回家继续修炼吧!")