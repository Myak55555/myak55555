A = float(input("Введите значение: "))
B = float(input("Введите значение: "))
C = float(input("Введите значение: "))
if C > A and C < B:
    AC = (abs(C - A))
    BC = (abs(C - B))
    print (AC)
    print (BC)
     else:
         print(" C должно быть между A и B")