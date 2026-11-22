with open("notes.txt","w",encoding="utf-8") as f:
    f.write("魔头\n")
    f.write("Zero\n")
    f.write("改变世界\n")
with open("notes.txt","r",encoding="utf-8") as f:
    print(f.read())
with open("notes.txt","a",encoding="utf-8") as f:
    f.write("第6课文件读写\n")
with open("notes.txt","r",encoding="utf-8") as f:
    print(f.read())