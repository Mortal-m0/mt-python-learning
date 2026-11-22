army = [
    {"name": "魔头", "job": "法师", "attack": 500, "hp": 80},
    {"name": "Zero", "job": "刺客", "attack": 800, "hp": 120},
    {"name": "小明", "job": "战士", "attack": 300, "hp": 200}
]
for p in army:
    print(f"英雄：{p['name']},职业:{p['job']}")
total_attack=0
for p in army:
    total_attack=total_attack+p['attack']
    if p['hp']>100:
        print(f"{p['name']}是个血牛,血量高达{p['hp']}!")
print(f"远征军总攻击力为:{total_attack}")