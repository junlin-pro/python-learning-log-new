def calc_concentration(mass_g, mw, volume_l):
    """由质量、分子量、体积计算摩尔浓度"""
    c = mass_g / mw / volume_l
    return c

c1 = calc_concentration(0.9, 180.16, 0.5)
c2 = calc_concentration(1.8, 180.16, 1.0)
print(f"{c1:.4f} / {c2:.4f} mol/L")   # 同样的活，两行搞定

