with open("notes.txt", "r", encoding = "utf-8") as f:
    lines = f.readlines()
print(f"共有{len(lines)}行")

total = 0
for line in lines:
    name,val = line.strip().split(",")
    total += float(val)
print(f"平均值为{total/len(lines):.1f}")

with open("summary.txt", "w", encoding = "utf-8") as f:
    f.write(f"样本数:{len(lines)}个\n平均活性:{total/len(lines):.1f}\n")

keyword = "A"
count = 0
with open("notes.txt", "r", encoding = "utf-8") as f:
    lines = f.readlines()

for line in lines:
    clean_line = line.strip()
    if keyword in clean_line:
        count += 1
print(f"关键词{keyword}出现的次数为{count}次")





with open("notes.txt", "r", encoding = "utf-8") as f:
    lines = f.readlines()

clean_line = [line.strip() for line in lines]
clean_line.sort()

with open("summary.txt", "w", encoding = "utf-8") as f:
    for line in lines:
    f.write(line + "\n")

with open("notes.txt", "r", encoding = "utf-8") as f:
    lines = f.readlines()

clean_line = [line.strip() for line in lines]
clean_line.sort(key=lambda x :float(x.strip(",")[1]))

with open("sorted_by_act.txt", "w", encoding = "utf-8") as f:
    for line in lines:
    f.write(line + "\n")