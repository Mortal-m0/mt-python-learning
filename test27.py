# test27 - 第6课C 异常处理（文件不存在FileNotFoundError / 无权限PermissionError / 编码错误UnicodeDecodeError）
try:
    with open("test.txt","r",encoding="utf-8") as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print("文件不存在，检查路径")
except PermissionError:
    print("没有权限打开这个文件")
except UnicodeDecodeError:
    print("编码不对，试试别的encoding")
finally:
    print("不管成不成，这句都会执行")

try:
    with open("chinese.txt","w",encoding="utf-8") as f:
        f.write("你好，魔头")
    with open("chinese.txt","r",encoding="ascii") as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print("文件不存在，检查路径")
except PermissionError:
    print("没有权限打开这个文件")
except UnicodeDecodeError:
    print("编码不对，试试别的encoding")
finally:
    print("不管成不成，这句都会执行")

try:
    with open("chinese.txt","w",encoding="utf-8") as f:
        f.write("你好，魔头")
    with open("chinese.txt","r",encoding="utf-8") as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print("文件不存在，检查路径")
except PermissionError:
    print("没有权限打开这个文件")
except UnicodeDecodeError:
    print("编码不对，试试别的encoding")
finally:
    print("不管成不成，这句都会执行")
   