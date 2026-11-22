#全局变量(global variable),函数外面定义的
x=100

def change():
    #函数内部重新给x赋值
    x=200
    print("函数内部x=",x)

#调用函数
change()

#函数外面再看x
print("函数外部x=",x)