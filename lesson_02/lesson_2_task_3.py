import math

a = float(input("Введите сторону квадрата: "))
def squre(a):
    a = a**2
    b = math.ceil(a)
    return b
print("Площадь квадрата = ", squre(a))