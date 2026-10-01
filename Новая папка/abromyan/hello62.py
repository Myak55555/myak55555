N = int(input("Введите значение: "))
d = 2
is_prime = N > 1                 # Зачем Евгений прайм задал это?
while d * d <= N:
    if N % d == 0:
        is_prime = False
        break
    d += 1
print( is_ prime)