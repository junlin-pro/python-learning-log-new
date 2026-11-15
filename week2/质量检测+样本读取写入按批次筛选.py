def classify(val, ok_line=90, retest_line=80):   # 阈值变成可调参数
    if val >= ok_line:
        return "合格"
    elif val >= retest_line:
        return "复测"
    return "不合格"

rows = []
with open ("notes.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        rows.append(parts)


batch_data = {}

with open ("result.csv","w", encoding="utf-8") as f:
    f.write("编号,活性,判定,批次\n")

    for name,val in rows:
        act = float(val)
        level = classify(act)

        batch = name[0]

        f.write(f"{name},{val},{level},{batch}\n")

        if batch not in batch_data:
           batch_data[batch] = []
        batch_data[batch].append(act)
    
with open ("result2.csv","w", encoding ="utf-8") as f:
    f.write("批次,样本数,平均活性(U/mL)\n")

    for batch, act_list in batch_data.items():
        sample_count = len(act_list)
        avg = sum(act_list) / sample_count
        f.write(f"{batch}, {sample_count}, {avg:.1f}\n")

print("处理完成，已生成 result.csv 和 result2.csv")

