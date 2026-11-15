def classify(val, ok_line=90, retest_line=80):   # 阈值变成可调参数
    if val >= ok_line:
        return "合格"
    elif val >= retest_line:
        return "复测"
    return "超标"

def report(samples):
    stats = {"合格": 0, "复测": 0, "超标": 0}
    for name, val in samples.items():
        stats[classify(val)] += 1        # 函数调用函数
    return stats

samples = {"A01": 85.2, "A02": 92.1, "B01": 78.9}
print(report(samples))
print(report(samples)) # 再调一次 report，阈值传 85 试试

ok = []
retest = []
fail = []
all_act = []

# 需求①：while True 循环手动录入样本
while True:
    sample_id = input("输入样本编号(输入q退出):")
    if sample_id == "q":
        break
    
    act = float(input("输入样本活性值(U/mL):"))


    samples = {}

    def classify(act, pass_line = 90, retest_line = 80):
        if act >= pass_line:
            return "ok"
        elif act >= retest_line:
            return "retest"
        else:
            return "fail"

    def report(samples):
        stats = {"ok":0, "retest":0, "fail":0}
        for name,act in samples.items():
          stats(classify(act)) += 1
        return  stats
    print(report(samples))

# 汇总输出 + 空数据防护
if all_act:
    print("\n" + "="*30)
    print(f"合格(≥{pass_line}): {len(ok)} 个 → {ok}")
    print(f"复测(80~{pass_line-0.1:.1f}): {len(retest)} 个 → {retest}")
    print(f"超标(<80): {len(fail)} 个 → {fail}")
    
    avg = sum(all_act) / len(all_act)
    print(f"\n共检测{len(all_act)}个样本")
    print(f"平均活性值: {avg:.1f} U/mL")
    
    pass_rate = len(ok) / len(all_act) * 100
    print(f"样本合格率: {pass_rate:.1f}%")
else:
    print("未录入任何样本数据")
