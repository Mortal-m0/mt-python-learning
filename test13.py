skills=["火球术","雷电术","冰冻术"]
print(skills)
print(skills[0])
print(skills[1])
print(skills[-1])
skills.append("陨石术")
print(f"学会了新技能!当前技能总数:{len(skills)}个")
print("---开始清点技能---")
for s in skills:
    print(f"技能:{s}")