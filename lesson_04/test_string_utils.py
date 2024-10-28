import pytest

from string_utils import StringUtils

string_util = StringUtils()

#Тест кейс 1: Проверяет, делает ли функция "capitalize" первую букву заглавной.

#Позитивные тест кейсы:
@pytest.mark.parametrize('string, result', [
    ("kostya", "Kostya"),
    ("kosTya", "KosTya"),
    ("kos tya", "Kos tya"),
    ("kos_tya", "Kos_tya"),
    ("kos'tya", "Kos'tya"),
    ("kostya123", "Kostya123"),
    ("kostya-1", "Kostya-1"),
    ("Kostya", "Kostya"),
    ("kostya ", "Kostya "),

#Негативные тест кейсы:
    ("", ""),
    (" ", " "),
    ("KOSTYA", "KOSTYA"),
    ("123kostya", "123kostya"),
    (" kostya", " kostya"),
    ("_kostya", "_kostya")
])
def test_capitalize(string, result):
    string_util = StringUtils()
    res = string_util.capitilize(string)
    assert res == result

#Тест-кейс 2: Проверяет, удаляет ли функция "trim" пробел перед строкой.

#Позитивные тест кейсы:
@pytest.mark.parametrize('string, result', [
    ("  lera", "lera"),
    (" QWERTY ", "QWERTY "),
    ("  123  ", "123  "),
    (" Konstantin-Pogodin", "Konstantin-Pogodin"),
    ("   kos1", "kos1"),

#Негативные тест кейсы:
    ("", ""),
    ("ko s", "ko s"),
    ("qwerty", "qwerty"),
    ("123  ", "123  "),
])

def test_trim(string, result):
    string_util = StringUtils()
    res = string_util.trim(string)
    assert res == result

#Тест-кейс 3: Проверяет, преобразует ли функция "to_list" строку в список.

# Позитивные тест-кейсы:
@pytest.mark.parametrize('string, div, result', [
    ("cat,fox,dog", ",", ["cat", "fox", "dog"]),
    ("cat;fox;dog", ";", ["cat", "fox", "dog"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),

# Негативные тест-кейсы:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"])
])
def test_to_list(string, div, result):
    if div is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, div)
    assert res == result

#Тест-кейс 4: Проверка функцией contains, содержит ли строка искомый символ.

#Позитивные тест-кейсы:
@pytest.mark.parametrize('string, symbol, result', [
    ("qwerty", "w", True),
    (" test", " ", True),
    ("num  ", "m", True),
    ("Saint-Petersburg", "-", True),
    ("123", "2", True),
    ("GPS", "PS", True),
    ("", "", True),
    (" @#!  #$@", "!", True),

#Негативные тест кейсы:
    ("Moscow", "m", False),
    ("qwerty", "Q", False),
    ("cat", "x", False),
    ("dog", "!", False),
    ("fox", " ", False),
    ("", "t", False),
    ("abc", "xyz", False),
    ("abc", "cba", False),
    ("", " ", False)
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    res = string_util.contains(string, symbol)
    assert res == result

#Тест-кейс 5: Проверяет, удаляет ли функция "delete_symbol" указанный символ

#Позитивные тест-кейсы:
@pytest.mark.parametrize('string, symbol, result', [
    ("test", "t", "es"),
    ("Qwerty", "r", "Qwety"),
    ("Moscow", "M", "oscow"),
    ("123", "2", "13"),
    ("Saint-Petersburg", "-", "SaintPetersburg"),
    ("Sky Pro", " ", "SkyPro"),
    ("Pro", "ro", "P"),
    ("cat ", "", "cat "),
#Негативные тест-кейсы:
    ("dog", "k", "dog"),
    ("", "", ""),
    ("", "d", ""),
    ("fox", "", "fox"),

])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

#Тест-кейс 6: Проверяет, идентифицирует ли функция "starts_with" начальный символ.

#Позитивные тест-кейсы:
@pytest.mark.parametrize('string, symbol, result', [
    ("dog", "d", True),
    ("", "", True),
    ("Moscow", "M", True),
    (" cat", " ", True),
    ("Fox  ", "F", True),
    ("Saint-Petersburg", "S", True),
    ("Sky Pro", "S", True),
    ("123", "1", True),
    ("qwerty", "", True),
    ("!Qwerty", "!", True),

#Негативные тест-кейсы:
    ("Moscow", "m", False),
    ("dog", "D", False),
    ("", "q", False),
    ("Test", "t", False),
    ("cat", "t", False),
    ("fox", "o", False),
    ("012", "2", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

#Тест-кейс 6: Проверяет, идентифицирует ли функция "end_with" конечный символ.

#Позитивные тест-кейсы:
@pytest.mark.parametrize('string, symbol, result', [
    ("dog", "g", True),
    ("CAT", "T", True),
    ("", "", True),
    ("rat ", " ", True),
    ("123", "3", True),
    ("Saint-Petersburg", "g", True),
    ("Sky Pro", "o", True),
    ("qwerty1", "1", True),
    ("test", "", True),
    ("!@#", "#", True),
#Негативные тест-кейсы:
    ("qwerty", "p", False),
    ("ever", "R", False),
    ("", " ", False),
    ("!@#", "!", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

#Тест-кейс 8: Проверяет, идентифицирует ли функция "is_empty" пустую строку.

#Позитивные тест-кейсы:
@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("  ", True),

#Негативные тест-кейсы:
    ("dog", False),
    (" fox", False),
    ("123", False),
    ("cat ", False),
    ("!@#$%", False)
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

#Тест-кейс 9: Проверяет, преобразует ли функция "list_to_string" список в строку с указанным символом.

#Позитивные тест-кейсы:
@pytest.mark.parametrize('lst, join, result', [
    (["a", "b", "c"], ",", "a,b,c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Saint", "Petersburg"], "-", "Saint-Petersburg"),
    (["Sky", "Pro"], " ", "Sky Pro"),
    (["a", "b", "c"], "@", "a@b@c"),

#Негативные тест-кейсы:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, join, result):
    string_util = StringUtils()
    if join == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, join)
    assert res == result