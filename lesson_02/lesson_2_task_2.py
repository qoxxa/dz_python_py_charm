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






    # def qater_of_year(month):
    #     if 1 <= month <= 3:
    #         return ("I квартал")
    #     elif 4 <= month <= 6:
    #         return ("II квартал")
    #     elif 7 <= month <= 9:
    #         return ("III квартал")
    #     elif 10 <= month <= 12:
    #         return ("IV квартал")
    #     else:
    #         return ("Неверно указан номер месяца")
    #
    # try:
    #     month = int(input("Введите номер месяца (1-12): "))
    #     print(qater_of_year(month))
    #
    # except ValueError:
    #     print("Введите целое число")