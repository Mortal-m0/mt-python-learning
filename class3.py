print("--- 欢迎使用魔头战报评估器 ---")
money_in=input("请输入今天拼单赚了多少钱:")
money=float(money_in)
time_in=input("请输入今天敲代码学了几个小时:")
hours=float(time_in)
if money>=500 and hours >=2:
    print("太牛了魔头!今天既赚了大钱,又给人参浇了水,双线大捷!")
elif money >=500 and hours <2:
    print("今天赚得不少!但别忘了,副业转主业还要靠每天积累,明天多学一会儿!")
elif money <500 and hours >=2:
    print("今天没有接到大单没关系,你学了很久代码,距离改变世界又近了一步!")
else:
    print ("今天有点摸鱼哦,明天得加倍干回来!")