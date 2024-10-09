def is_year_leap(year):
    if year % 4 != 0:
        return False
    else:
        return True
try:
    year = int(input("Введите год: "))
    print(f"год {year}:", is_year_leap(year))

except ValueError:
    print("Введите целое число")
