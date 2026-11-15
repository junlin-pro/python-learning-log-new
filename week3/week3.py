def load_file(path):
    rows = []
    with open(path, encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, val = line.split(",")
            rows.append((name, float(val), path))
    return rows

def classify(val, ok_line=90, retest_line=80):
    if val >= ok_line:
        return "合格"
    elif val >= retest_line:
        return "复测"
    else:
        return "不合格"

def main():
    all_rows = []
    for path in ["lab1.txt", "lab2.txt", "lab3.txt"]:
        all_rows += load_file(path)

    unique_rows = {}
    for name, val ,source in all_rows:
        if name not in unique_rows:
            unique_rows[name] = (val, source)

    with open("total_result.csv", "w", encoding= "utf-8") as f:
        f.write("编号,活性,判定,来源文件\n")
        for name, (val, source) in unique_rows.items():
            level = classify(val)
            f.write(f"{name},{val},{level},{source}\n")

    total_count = len(unique_rows)
    pass_count = 0
    for name, (val, source) in unique_rows.items():
        if classify(val) == "合格":
            pass_count += 1
    if total_count > 0:
        pass_rate = pass_count / total_count * 100
    else:
        pass_rate = 0

    file_stats = {}
    for name, (val, source) in unique_rows.items():
        if source not in file_stats:
            file_stats[source] = []
        file_stats[source].append(val)

    with open("report.txt", "w", encoding= "utf-8") as f:
        f.write("===== 实验数据统计表 =====\n")
        f.write(f"总样本数(去重后):{total_count}\n")
        f.write(f"合格数:{pass_count}\n")
        f.write(f"合格率:{pass_rate}%\n\n")
        f.write("===== 各文件统计 =====\n")
        for path, act_list in file_stats.items():
            avg = sum(act_list) / len(act_list)
            f.write(f"{path}:{len(act_list)}条, 平均活性:{avg:.1f}\n")

    print("处理完成，已生成 total_result.csv 和 report.txt")


main()
