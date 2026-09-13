a = float(input("Введите значение: "))
if a <= 0 or a >= 360:
    print ("Error")
else: 
    R = 3.14 * a / 180
    print(R)