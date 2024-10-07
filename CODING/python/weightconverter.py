weight = int(input('Weight: '))
lb_kg = input('L(bs) or K(g): ')

if lb_kg.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")
    