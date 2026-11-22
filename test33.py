#定义函数,name,age必须传,city有默认值
def introduce(name,age,city="广州"):
    print("我叫",name,"今年",age,"岁,住在",city)

#写法1:位置参数(positional argument),接顺序传
introduce("魔头",48)

#写法2:关键字参数(keyword argument),按名字传
introduce(age=48,name="魔头")

#写法3:混合,位置参数在前,关键字参数在后
introduce("魔头",city="深圳",age=48)    