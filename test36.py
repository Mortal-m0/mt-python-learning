# 定义函数:检查分数是否及格
def check_score(score):
    # 如果分数少于60,直接return返回"不及格“,函数到此结束
    if score<60:
        return "不及格"
    # 能走到这一行,说明上面没return,分数>=60
    return "及格"

# 调用:传50
print(check_score(50))

# 调用:传80
print(check_score(80))