print("---魔头的小卖部---")
def open_shop():
    goods=["红药水","蓝药水","回城卷轴"]
    print (f"欢迎光临！本店共有{len(goods)}件商品")
    for s in goods:
        print (f"本店售卖{s}.")
    buy_item=input ("老板,你想买什么?(请输入商品名):")
    if buy_item in goods:
        print (f"购买成功!魔头赚到了钱!")
    else:
        print (f"抱歉,本店没有这个商品.")
open_shop()