X = float(input("Кг шоколадных конфет: "))
A = float(input("цена шоколадных конфет: "))
Y = float(input("Кг карамальных кофет: "))
B = float(input("Цена карамельных конфет: "))
PPkgC = A / X
PPkgK = B / Y
R = PPkgC / PPkgK
print ("Цена за 1 кг шок. конф. : " ,PPkgC )
print ("Цена за 1 кг кар. конф. : " ,PPkgK )
print ("Разница: " ,R )