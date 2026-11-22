with open("log.txt","w",encoding="utf-8") as f:
    f.write("魔头\n")
    f.write("Zero\n")
with open("log.txt","a",encoding="utf-8") as f:
    f.write("改变世界\n")
with open("log.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
for line in lines:
    print(line.strip())
print(f"总行数{len(lines)}")