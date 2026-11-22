print("---魔头超市收银系统---")
cart = [
    {"name": "苹果", "price": 5, "qty": 2},
    {"name": "牛奶", "price": 15, "qty": 1},
    {"name": "面包", "price": 8, "qty": 3}
]
total_price=0
for p in cart:
    item_total=p['price']*p['qty']
    print(f"商品:{p['name']},小计:{item_total}元.")
    total_price=total_price+item_total
print(f"购物车总价:{total_price}元.")
budget=input("请输入你口袋里的预算:")
budget=float(budget)
if budget>total_price:
    print(f"支付成功!找零{budget-total_price}元.")
else:
    print(f"余额不足!还差:{total_price-budget}元.")