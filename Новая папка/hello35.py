V = float(input("Скорость лодки в стоячей воде (V): "))
U = float(input("Скорость течения реки (U): "))
T1 = float(input("Время движения лодки по озеру (T1): "))
T2 = float(input("Время движения лодки по реке (T2): "))
if V < U:
    print ("Error")
else:
    S_all = V * T1 + V * T2
    print ("Путь пройденный лодкой: " , S_all)