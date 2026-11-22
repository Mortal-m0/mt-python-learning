def evaluate_energy():
    sleep_hours=float(input("请输入你昨晚睡了几个小时:"))
    energy=int(input("请输入你现在的精力值(1-10):"))
    if sleep_hours>=7 and energy>=8:
        print("---状态:满血复活!---")
        for i in range(1,4):
            print(f"第{i}次提醒:今天必须干翻大项目!")
    elif sleep_hours<7 or energy<5:
        print("---状态:极度疲惫---")
        print("今天别卷了,早点休息!")
    else:
        state="勉强能战"
        print(f"---状态：{state}.建议泡杯咖啡!---")
evaluate_energy() 