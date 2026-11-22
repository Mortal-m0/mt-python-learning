print("---游戏倒计时开始---")
for i in range(3,0,-1):
    print(f"第{i}遍")
print("---开始闯关---")
hp=3
while hp >0:
    print(f"我还活着，继续战斗！{hp}")
    hp = hp-1
print("---Game Over。---")