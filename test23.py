with open("study_log.txt","w",encoding="utf-8") as f:
    f.write("第6课文件读写\n")
    f.write("魔头\n")
    f.write("Zero\n")
with open("study_log.txt","r",encoding="utf-8") as f:
    print(f.read())
with open("study_log.txt","a",encoding="utf-8") as f:
    f.write("今天开始改变世界\n")
with open("study_log.txt","r",encoding="utf-8") as f:
    print(f.read())
print("---文件读写测试完成---")