#函数A:有return,没有print(return,no print)
def add_return(a,b):
    return a+b #把结果交还给调用者(return to caller)

#函数B:有print,没有return(print,no retrun)
def add_print(a,b):
    print(a+b) #只在函数内部打印(print inside function)

#调用A:外面用print接住返回值
print("A的结果(result of A):",add_return(3,5))

#调用B:函数自己打印,外面不接
add_print(3,5)