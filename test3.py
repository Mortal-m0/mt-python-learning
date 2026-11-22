print("---Zero,我来了!---")
sleep_hours=input("请输入你昨晚睡了几个小时:")
sleep=float(sleep_hours)
energy_level=input("请输入你现在的精力值（1-10分）:")
energy=int(energy_level)
if sleep >=7 and energy >=8:
    print("满血复活!今晚必须干翻大项目!")
elif sleep >=7 and energy <8:
    print("睡得不错,但可能需要泡杯咖啡提提神.")
elif sleep <7 and energy >=8:
    print("虽然没睡够,但精神状态极佳,冲!")
else:
    print("极度疲惫,建议今晚只做轻量复习,早点休息.")