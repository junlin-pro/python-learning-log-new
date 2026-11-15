molecular_weight = 180.16 # 葡萄糖分子量 g/mol
mass_g = 0.9              # 称取质量
volume_l = 0.5            # 定容体积
moles = mass_g / molecular_weight
c = moles / volume_l
print(f"物质的量 = {moles:.4f}mol")
print(f"摩尔浓度={c:.4f} mol/L, 即 {c *1000:.2f} mmol/L")