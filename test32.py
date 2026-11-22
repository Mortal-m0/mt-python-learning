#定义函数,C有默认值10(default value)
def add_three(a,b,c=10):
    return a+b+c

#只传两个参数,c用默认值10
print(add_three(1,2))

#传参个参数,c用传进去的100
print(add_three(1,2,100))