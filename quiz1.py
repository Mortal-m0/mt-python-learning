# 条件判断 + 输入（考 if / elif / else / input / int）
# 要求：写 quiz1.py，实现：
# 用 input() 让用户输入一个分数；
# 用 int() 把输入转成整数，存进变量 score；
# 用 if / elif / else 判断：
# 分数 >= 90，打印 "优秀"
# 分数 >= 60 且 < 90，打印 "及格"
# 分数 < 60，打印 "不及格"
# 约束：必须用 int()，因为 input() 返回的是字符串。写完后分别输入 95、75、50 各跑一次，发三次输出。


score = int(input("请你输入分数:")) # input 返回字符串，必须 int 转换
if score >= 90:
    print("优秀")
elif score >= 60: # 能走到这里说明已 <90，不用再写 and score < 90
    print("及格")
else:
    print("不及格")