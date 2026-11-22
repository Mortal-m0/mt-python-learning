with open("diary.txt","w",encoding="utf-8") as f:
    f.write("魔头\n")
    f.write("Zero\n")
    f.write("改变世界\n")
with open("diary.txt","r",encoding="utf-8") as f:
    print(f.read())
with open("diary.txt","a",encoding="utf-8") as f:
    f.write("第6课A+B\n")
with open("diary.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
for line in lines:
    print(line.strip())
print(f"总行数{len(lines)}")