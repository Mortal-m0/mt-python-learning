#全局变量(global variable)
x=100

def read_x():
    #函数内部只读,不赋值
    print("函数内部读到x=",x)

#调用函数
read_x()

#函数外部再打印
print("函数外部x=",x)