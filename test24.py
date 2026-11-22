with open("members.txt","w",encoding="utf-8") as f:
    f.write("魔头\n")
    f.write("Zero\n")
    f.write("小明\n")
with open("members.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
for line in lines:
    print(line.strip())
print(f"总行数{len(lines)}")