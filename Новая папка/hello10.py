a = float(input("Введите значение: "))
b = float(input("Введите значение: "))
if a==0 or b==0:
    print ("Error")
M = a**a - b**b
P = a**a + b**b
D = a**a / b**b
print (M)
print (P)
print (D) 