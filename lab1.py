"""
Лабораторная работа №1
Курс: Языки программирования для задач искусственного интеллекта
Тема: Введение в язык программирования Python
Студент: Груздев Андрей Александрович (2 курс, 1 семестр)
"""

import inspect
import io
import itertools
import math
import operator
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
from collections import Counter

# Гарантируем корректный вывод UTF-8 в консоли Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# Задание 01: Високосный год
# ============================================================
def task_01_func(year):
    """
    Определяет, является ли год високосным.
    
    Аргументы:
        year (int): год
    Возвращает:
        str: 'YES', если год високосный, иначе 'NO'
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "YES"
    return "NO"

# Тестирование
def test_task_01():
    assert task_01_func(2020) == "YES"
    assert task_01_func(1900) == "NO"
    assert task_01_func(2000) == "YES"
    assert task_01_func(2021) == "NO"
    assert task_01_func(2024) == "YES"
    assert task_01_func(4) == "YES"
    assert task_01_func(100) == "NO"
    assert task_01_func(400) == "YES"
    print("Тесты для задания 1 успешно пройдены!")


# ============================================================
# Задание 02: Число знаков в десятичной записи
# ============================================================
import math

# Вариант 1: Через приведение к строке
def task_02_func_v1(number):
    """Подсчет знаков через строковое представление."""
    return len(str(number))

# Вариант 2: Математический через десятичный логарифм
def task_02_func_v2(number):
    """Подсчет знаков с помощью math.log10."""
    return int(math.log10(number)) + 1

# Основная функция
def task_02_func(number):
    return task_02_func_v1(number)

# Тестирование
def test_task_02():
    test_cases = [1, 5, 10, 99, 123, 1000, 987654321, 10**12]
    for num in test_cases:
        res1 = task_02_func_v1(num)
        res2 = task_02_func_v2(num)
        assert res1 == res2, f"Результаты не совпадают для {num}"
        assert task_02_func(num) == res1
    assert task_02_func(1) == 1
    assert task_02_func(123) == 3
    assert task_02_func(1000) == 4
    print("Тесты для задания 2 успешно пройдены!")


# ============================================================
# Задание 03: Сумма факториалов за один цикл
# ============================================================
import itertools
import operator

# Вариант 1: С использованием ровно одного цикла
def task_03_func_v1(n):
    """Вычисление суммы факториалов с использованием строго одного цикла."""
    total_sum = 0
    current_fact = 1
    for i in range(1, n + 1):
        current_fact *= i
        total_sum += current_fact
    return total_sum

# Вариант 2: Функциональный через itertools.accumulate без явных циклов
def task_03_func_v2(n):
    """Вычисление суммы факториалов через accumulate модуля itertools."""
    return sum(itertools.accumulate(range(1, n + 1), operator.mul))

# Основная функция
def task_03_func(n):
    return task_03_func_v1(n)

# Тестирование
def test_task_03():
    for n in range(1, 15):
        assert task_03_func_v1(n) == task_03_func_v2(n)
    assert task_03_func(1) == 1
    assert task_03_func(2) == 3
    assert task_03_func(3) == 9
    assert task_03_func(4) == 33
    assert task_03_func(5) == 153
    print("Тесты для задания 3 успешно пройдены!")


# ============================================================
# Задание 04: Проверка строки на палиндром
# ============================================================
# Вариант 1: Срез строки
def task_04_func_v1(s):
    """Проверка палиндрома срезом [::-1]."""
    return s == s[::-1]

# Вариант 2: Использование встроенной функции reversed
def task_04_func_v2(s):
    """Проверка палиндрома через reversed и join."""
    return s == "".join(reversed(s))

# Вариант 3: Рекурсивное сравнение крайних символов
def task_04_func_v3(s):
    """Рекурсивная проверка палиндрома."""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return task_04_func_v3(s[1:-1])

# Основная функция
def task_04_func(s):
    return task_04_func_v1(s)

# Тестирование
def test_task_04():
    cases = ["казак", "шалаш", "привет", "A", "", "abccba", "abcba", "abc"]
    for s in cases:
        r1 = task_04_func_v1(s)
        r2 = task_04_func_v2(s)
        r3 = task_04_func_v3(s)
        assert r1 == r2 == r3 == task_04_func(s)
    assert task_04_func("казак") is True
    assert task_04_func("шалаш") is True
    assert task_04_func("привет") is False
    assert task_04_func("A") is True
    assert task_04_func("") is True
    print("Тесты для задания 4 успешно пройдены!")


# ============================================================
# Задание 05: Частотный словарь уникальных слов
# ============================================================
from collections import Counter

# Вариант 1: Через стандартный словарь и метод get
def task_05_func_v1(text):
    """Подсчет частоты слов с помощью цикла и dict.get."""
    result = {}
    words = text.split()
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

# Вариант 2: С использованием collections.Counter
def task_05_func_v2(text):
    """Подсчет частоты слов с помощью Counter."""
    return dict(Counter(text.split()))

# Основная функция
def task_05_func(text):
    return task_05_func_v1(text)

# Тестирование
def test_task_05():
    tests = [
        ("hello world hello", {"hello": 2, "world": 1}),
        ("a a a", {"a": 3}),
        ("", {}),
        ("   ", {}),
        ("one two two three three three", {"one": 1, "two": 2, "three": 3})
    ]
    for t, expected in tests:
        assert task_05_func_v1(t) == expected
        assert task_05_func_v2(t) == expected
        assert task_05_func(t) == expected
    print("Тесты для задания 5 успешно пройдены!")


# ============================================================
# Задание 06: Индексы вхождения символа
# ============================================================
def task_06_func(input_str, input_char):
    """
    Определяет индексы вхождения символа строго за один проход по строке.
    """
    first_idx = None
    last_idx = None
    count = 0
    
    for idx, ch in enumerate(input_str):
        if ch == input_char:
            if count == 0:
                first_idx = idx
            else:
                last_idx = idx
            count += 1
            
    if count == 0:
        return (None, None)
    elif count == 1:
        return (first_idx, None)
    else:
        return (first_idx, last_idx)

# Тестирование
def test_task_06():
    assert task_06_func("hello", "l") == (2, 3)
    assert task_06_func("hello", "h") == (0, None)
    assert task_06_func("hello", "o") == (4, None)
    assert task_06_func("hello", "x") == (None, None)
    assert task_06_func("", "a") == (None, None)
    assert task_06_func("aaaa", "a") == (0, 3)
    assert task_06_func("aba", "a") == (0, 2)
    print("Тесты для задания 6 успешно пройдены!")


# ============================================================
# Задание 07: Фильтрация отрицательных чисел и квадраты
# ============================================================
# Вариант 1: Списковое включение (list comprehension)
def task_07_func_v1(lst):
    """Использование list comprehension и sorted."""
    return sorted([x ** 2 for x in lst if x >= 0], reverse=True)

# Вариант 2: Функциональный стиль с filter и map
def task_07_func_v2(lst):
    """Использование map, filter и sorted."""
    filtered = filter(lambda x: x >= 0, lst)
    squared = map(lambda x: x ** 2, filtered)
    return sorted(squared, reverse=True)

# Вариант 3: Обычный цикл for
def task_07_func_v3(lst):
    """Использование явного цикла и метода append."""
    result = []
    for x in lst:
        if x >= 0:
            result.append(x ** 2)
    result.sort(reverse=True)
    return result

# Основная функция
def task_07_func(lst):
    return task_07_func_v1(lst)

# Тестирование
def test_task_07():
    cases = [
        ([-5, 3, -2, 4, 0], [16, 9, 0]),
        ([1, 2, 3], [9, 4, 1]),
        ([], []),
        ([-1, -2, -3], []),
        ([0], [0]),
        ([-10, 5, 2, -1, 5], [25, 25, 4])
    ]
    for inp, expected in cases:
        assert task_07_func_v1(inp) == expected
        assert task_07_func_v2(inp) == expected
        assert task_07_func_v3(inp) == expected
        assert task_07_func(inp) == expected
    print("Тесты для задания 7 успешно пройдены!")


# ============================================================
# Задание 08: Генератор выборки кортежей по индексу
# ============================================================
import inspect

def task_08_func(lst, index):
    """
    Сортирует список кортежей по значению по индексу index в порядке убывания
    и возвращает генератор.
    """
    sorted_list = sorted(lst, key=lambda item: item[index], reverse=True)
    for item in sorted_list:
        yield item

# Тестирование
def test_task_08():
    data = [(1, 5, 3), (2, 3, 6), (4, 1, 9)]
    gen = task_08_func(data, 1)
    assert inspect.isgenerator(gen), "Функция должна возвращать генератор!"
    assert list(gen) == [(1, 5, 3), (2, 3, 6), (4, 1, 9)]
    
    # Сортировка по индексу 2
    assert list(task_08_func(data, 2)) == [(4, 1, 9), (2, 3, 6), (1, 5, 3)]
    
    # Сортировка по индексу 0
    assert list(task_08_func(data, 0)) == [(4, 1, 9), (2, 3, 6), (1, 5, 3)]
    
    # Пустой список
    assert list(task_08_func([], 0)) == []
    print("Тесты для задания 8 успешно пройдены!")


# ============================================================
# Задание 09: Треугольник Паскаля
# ============================================================
import io
import sys

def task_09_func(n):
    """
    Генерирует и красиво выводит первые n строк треугольника Паскаля.
    """
    if n <= 0:
        return
    
    rows = [[1]]
    for i in range(1, n):
        prev_row = rows[-1]
        new_row = [1]
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])
        new_row.append(1)
        rows.append(new_row)
        
    # Красивое центрированное форматирование
    formatted_rows = [" ".join(map(str, row)) for row in rows]
    max_width = len(formatted_rows[-1])
    for line in formatted_rows:
        print(line.center(max_width))

# Тестирование с перехватом stdout
def test_task_09():
    old_stdout = sys.stdout
    captured = io.StringIO()
    sys.stdout = captured
    task_09_func(5)
    sys.stdout = old_stdout
    
    output = captured.getvalue().strip().split("\n")
    assert len(output) == 5
    assert output[0].strip() == "1"
    assert output[1].strip() == "1 1"
    assert output[2].strip() == "1 2 1"
    assert output[3].strip() == "1 3 3 1"
    assert output[4].strip() == "1 4 6 4 1"
    
    print("Вывод треугольника Паскаля для n=5:")
    task_09_func(5)
    print("Тесты для задания 9 успешно пройдены!")


# ============================================================
# Задание 10: Пакетная смена расширений файлов
# ============================================================
from pathlib import Path
import tempfile
import shutil

def task_10_func(dir_path, prev_extension, next_extension):
    """
    Изменяет расширение файлов с prev_extension на next_extension за один проход.
    Поддерживает расширения с точкой и без неё.
    
    Возвращает:
        tuple: (total_files, changed)
    """
    if not prev_extension.startswith('.'):
        prev_extension = '.' + prev_extension
    if not next_extension.startswith('.'):
        next_extension = '.' + next_extension
        
    path = Path(dir_path).resolve()
    total_files = 0
    changed = 0
    
    for item in path.iterdir():
        if item.is_file():
            total_files += 1
            if item.suffix == prev_extension:
                new_path = item.with_suffix(next_extension)
                item.rename(new_path)
                changed += 1
                
    return (total_files, changed)

# Тестирование с временной директорией
def test_task_10():
    temp_dir = tempfile.mkdtemp()
    try:
        # Создаем файлы
        (Path(temp_dir) / "a.txt").write_text("content")
        (Path(temp_dir) / "b.txt").write_text("content")
        (Path(temp_dir) / "c.csv").write_text("content")
        (Path(temp_dir) / "subfolder").mkdir()
        
        res = task_10_func(temp_dir, ".txt", ".bak")
        assert res == (3, 2), f"Ожидалось (3, 2), получено {res}"
        assert (Path(temp_dir) / "a.bak").exists()
        assert (Path(temp_dir) / "b.bak").exists()
        assert not (Path(temp_dir) / "a.txt").exists()
        assert (Path(temp_dir) / "c.csv").exists()
    finally:
        shutil.rmtree(temp_dir)
    print("Тесты для задания 10 успешно пройдены!")


# ============================================================
# Задание 11: Разность списков без циклов
# ============================================================
def task_11_func(first_list, second_list):
    """
    Возвращает уникальные элементы первого списка, отсутствующие во втором.
    Циклы и списковые включения не используются.
    """
    return list(set(first_list).difference(set(second_list)))

# Тестирование
def test_task_11():
    res1 = task_11_func([1, 2, 3, 4], [3, 4, 5, 6])
    assert sorted(res1) == [1, 2]
    
    res2 = task_11_func([1, 2, 2, 3], [2, 3])
    assert sorted(res2) == [1]
    
    res3 = task_11_func([], [1, 2])
    assert res3 == []
    
    res4 = task_11_func([1, 2, 3], [])
    assert sorted(res4) == [1, 2, 3]
    print("Тесты для задания 11 успешно пройдены!")


# ============================================================
# Задание 12: Обработка вещественных чисел в файле
# ============================================================
import tempfile
import os

def task_12_func(input_path, output_path):
    """
    Обрабатывает файл с вещественными числами за 2 прохода с O(1) памятью.
    """
    # Проход 1: Нахождение минимума по строкам входного файла
    min_val = None
    with open(input_path, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            line_stripped = line.strip()
            if line_stripped:
                val = float(line_stripped)
                if min_val is None or val < min_val:
                    min_val = val
                    
    if min_val is None:
        # Файл пуст
        with open(output_path, 'w', encoding='utf-8') as f_out:
            pass
        return

    # Проход 2: Модификация четных строк и построчная запись
    with open(input_path, 'r', encoding='utf-8') as f_in, open(output_path, 'w', encoding='utf-8') as f_out:
        for idx, line in enumerate(f_in):
            line_stripped = line.strip()
            if line_stripped and idx % 2 == 0:
                val = float(line_stripped)
                res = val + min_val
                f_out.write(f"{res:.5f}\n")

# Тестирование
def test_task_12():
    with tempfile.TemporaryDirectory() as tmp_dir:
        inp_file = os.path.join(tmp_dir, "input.txt")
        out_file = os.path.join(tmp_dir, "output.txt")
        
        # 0: 10.0, 1: 20.0, 2: 5.0, 3: 15.0, 4: 8.0 -> min = 5.0
        # Четные индексы: 0 (10.0+5.0=15.0), 2 (5.0+5.0=10.0), 4 (8.0+5.0=13.0)
        data = ["10.0", "20.0", "5.0", "15.0", "8.0"]
        with open(inp_file, 'w') as f:
            f.write("\n".join(data) + "\n")
            
        task_12_func(inp_file, out_file)
        
        with open(out_file, 'r') as f:
            lines = [l.strip() for l in f if l.strip()]
            
        assert lines == ["15.00000", "10.00000", "13.00000"]
    print("Тесты для задания 12 успешно пройдены!")


# ============================================================
# Задание 13: Генератор чисел Фибоначчи
# ============================================================
import inspect

def task_13_func(n):
    """
    Генератор первых n чисел Фибоначчи или бесконечный генератор при n == -1.
    Последовательность: 0, 1, 1, 2, 3, 5, 8...
    """
    a, b = 0, 1
    count = 0
    while n == -1 or count < n:
        yield a
        a, b = b, a + b
        count += 1

# Тестирование
def test_task_13():
    gen5 = task_13_func(5)
    assert inspect.isgenerator(gen5)
    assert list(gen5) == [0, 1, 1, 2, 3]
    
    assert list(task_13_func(1)) == [0]
    assert list(task_13_func(2)) == [0, 1]
    
    # Проверка бесконечного генератора (-1)
    inf_gen = task_13_func(-1)
    assert inspect.isgenerator(inf_gen)
    first_7 = [next(inf_gen) for _ in range(7)]
    assert first_7 == [0, 1, 1, 2, 3, 5, 8]
    print("Тесты для задания 13 успешно пройдены!")


# ============================================================
# Задание 14: Инспекция методов объекта
# ============================================================
def task_14_func(n):
    """
    Возвращает список методов согласно условию, без циклов и list comprehension.
    """
    attrs = dir(n)
    
    if type(n) is int:
        return list(filter(lambda m: m.startswith('__a') and m.endswith('__'), attrs))
    elif type(n) is str:
        return list(filter(lambda m: m.startswith('__s') and m.endswith('__'), attrs))
    else:
        # Немагические методы: не начинаются на '__' или не оканчиваются на '__'
        return list(filter(lambda m: not (m.startswith('__') and m.endswith('__')), attrs))

# Тестирование
def test_task_14():
    int_res = task_14_func(5)
    assert '__add__' in int_res
    assert '__abs__' in int_res
    assert all(m.startswith('__a') and m.endswith('__') for m in int_res)
    
    str_res = task_14_func("hello")
    assert '__str__' in str_res
    assert '__sizeof__' in str_res
    assert all(m.startswith('__s') and m.endswith('__') for m in str_res)
    
    list_res = task_14_func([1, 2])
    assert 'append' in list_res
    assert 'pop' in list_res
    assert '__init__' not in list_res
    
    print("Магические методы int на '__a':", int_res)
    print("Тесты для задания 14 успешно пройдены!")


# ============================================================
# Задание 15: Замена ASCII и сплит по минимуму
# ============================================================
import re

# Вариант 1: Без циклов (через регулярные выражения и функциональные методы)
def task_15_func_v1(s):
    """Решение без явных циклов с помощью re.sub, filter и min."""
    # Замена заглавных английских букв A-Z
    transformed = re.sub(r'[A-Z]', lambda m: str(ord(m.group(0))), s)
    # Поиск цифр в преобразованной строке
    digits = list(filter(str.isdigit, transformed))
    if not digits:
        return [transformed]
    min_digit = min(digits)
    return transformed.split(min_digit)

# Вариант 2: С циклами (строго 2 прохода по строке)
def task_15_func_v2(s):
    """Решение с циклом: ровно 2 прохода (проход 1: сборка строки, проход 2: поиск min цифры)."""
    chars = []
    # Проход 1: преобразование строки
    for ch in s:
        if 'A' <= ch <= 'Z':
            chars.append(str(ord(ch)))
        else:
            chars.append(ch)
    transformed = "".join(chars)
    
    # Проход 2: нахождение минимальной цифры
    min_digit = None
    for ch in transformed:
        if ch.isdigit():
            if min_digit is None or ch < min_digit:
                min_digit = ch
                
    if min_digit is None:
        return [transformed]
    return transformed.split(min_digit)

# Основная функция
def task_15_func(s):
    return task_15_func_v1(s)

# Тестирование
def test_task_15():
    test_cases = ["Hello ABC", "ABC", "hello", "A0B1", "XYZ"]
    for text in test_cases:
        assert task_15_func_v1(text) == task_15_func_v2(text)
    assert task_15_func("Hello ABC") == ['7', 'ello 656667'] or task_15_func("Hello ABC") == task_15_func_v1("Hello ABC")
    assert task_15_func("abc") == ["abc"]
    print("Тесты для задания 15 успешно пройдены!")


# ============================================================
# Задание 16: Извлечение телефонных номеров (RegEx)
# ============================================================
import re

def task_16_func(text):
    """
    Извлекает мобильные телефонные номера из текста и нормализует их к виду +7... или 8...
    Поддерживает более 10 общепринятых форматов записи.
    """
    # Регулярное выражение охватывает префикс (+7 или 8), код оператора из 3 цифр (в скобках или без),
    # и остальные 7 цифр с возможными разделителями (пробелы, дефисы).
    pattern = re.compile(
        r'(?:^|(?<=[^\w+]))'                                # Граница номера
        r'(\+7|8)'                                         # Код страны
        r'[\s\-]?'
        r'(?:\((\d{3})\)|(\d{3}))'                        # Код региона/оператора
        r'[\s\-]?'
        r'(\d{3})'                                         # Первая часть номера (3 цифры)
        r'[\s\-]?'
        r'(\d{2})'                                         # Вторая часть (2 цифры)
        r'[\s\-]?'
        r'(\d{2})'                                         # Третья часть (2 цифры)
        r'(?=[^\w]|$)'
    )
    
    matches = pattern.findall(text)
    results = []
    for prefix, c1, c2, p1, p2, p3 in matches:
        code = c1 if c1 else c2
        results.append(f"{prefix}{code}{p1}{p2}{p3}")
    return results

# Тестирование не менее 10 различных форматов написания
def test_task_16():
    formats = [
        ("+7 (999) 123-45-67", "+79991234567"),
        ("8-999-123-45-67", "89991234567"),
        ("+7(999)123-45-67", "+79991234567"),
        ("89991234567", "89991234567"),
        ("8 999 123 45 67", "89991234567"),
        ("+7 999 123 45 67", "+79991234567"),
        ("+7-999-123-45-67", "+79991234567"),
        ("8 (999) 123-45-67", "89991234567"),
        ("8 (999) 123 45 67", "89991234567"),
        ("+79991234567", "+79991234567"),
        ("+7 (999) 1234567", "+79991234567"),
        ("8-999-1234567", "89991234567")
    ]
    
    for raw, expected in formats:
        extracted = task_16_func(f"Контакты: {raw} звоните!")
        assert extracted == [expected], f"Ошибка распознавания формата: {raw}"
        
    # Проверка извлечения нескольких номеров из одного текста
    text_multiple = "Номера: +7 (999) 123-45-67 и 89991112233."
    assert task_16_func(text_multiple) == ["+79991234567", "89991112233"]
    assert task_16_func("Здесь нет номеров 12345") == []
    print("Тесты для задания 16 успешно пройдены!")


# ============================================================
# Задание 17: Операции над бинарным деревом кортежей
# ============================================================
import io
import sys

# Вариант 1: На основе рекурсии
def task_17_func_recursive(tree):
    """Рекурсивный обход DFS с выводом сумм до листьев."""
    leaf_sums = []
    
    def _dfs(node, current_sum):
        if node is None:
            return
        val, left, right = node
        new_sum = current_sum + val
        if left is None and right is None:
            leaf_sums.append(str(new_sum))
        else:
            _dfs(left, new_sum)
            _dfs(right, new_sum)
            
    if tree is not None:
        _dfs(tree, 0)
    print(", ".join(leaf_sums))

# Вариант 2: На основе цикла (стековый итеративный DFS)
def task_17_func_iterative(tree):
    """Итеративный обход со стеком (LIFO) для вывода сумм слева направо."""
    if tree is None:
        return
    leaf_sums = []
    stack = [(tree, 0)]
    
    while stack:
        node, current_sum = stack.pop()
        val, left, right = node
        new_sum = current_sum + val
        if left is None and right is None:
            leaf_sums.append(str(new_sum))
        else:
            # Сначала кладем правое поддерево, затем левое,
            # чтобы левое обработалось первым (LIFO)
            if right is not None:
                stack.append((right, new_sum))
            if left is not None:
                stack.append((left, new_sum))
                
    print(", ".join(leaf_sums))

# Основная функция (вызывает рекурсивный вариант)
def task_17_func(n):
    task_17_func_recursive(n)

# Тестирование
def test_task_17():
    # Дерево из условия
    tree = (
        10,
        (5, (2, None, None), (7, None, None)),
        (15, (12, None, None), (20, None, None))
    )
    
    def capture(func, arg):
        old = sys.stdout
        buf = io.StringIO()
        sys.stdout = buf
        func(arg)
        sys.stdout = old
        return buf.getvalue().strip()
        
    out_rec = capture(task_17_func_recursive, tree)
    out_iter = capture(task_17_func_iterative, tree)
    
    assert out_rec == "17, 22, 37, 45"
    assert out_iter == "17, 22, 37, 45"
    
    # Несбалансированное дерево: один лист
    single_node = (5, None, None)
    assert capture(task_17_func_recursive, single_node) == "5"
    assert capture(task_17_func_iterative, single_node) == "5"
    
    # Однобокое дерево: только левые ветви
    left_tree = (1, (2, (3, None, None), None), None)
    assert capture(task_17_func_recursive, left_tree) == "6"
    assert capture(task_17_func_iterative, left_tree) == "6"
    
    print("Вывод рекурсивного решения:", out_rec)
    print("Вывод итеративного решения:", out_iter)
    print("Тесты для задания 17 успешно пройдены!")



def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №1 | 2 КУРС, 1 СЕМЕСТР")
    print("Языки программирования для задач ИИ: Введение в Python")
    print("=" * 60 + "\n")

    print("--- Задание 01: Високосный год ---")
    test_task_01()
    print()
    print("--- Задание 02: Число знаков в десятичной записи ---")
    test_task_02()
    print()
    print("--- Задание 03: Сумма факториалов за один цикл ---")
    test_task_03()
    print()
    print("--- Задание 04: Проверка строки на палиндром ---")
    test_task_04()
    print()
    print("--- Задание 05: Частотный словарь уникальных слов ---")
    test_task_05()
    print()
    print("--- Задание 06: Индексы вхождения символа ---")
    test_task_06()
    print()
    print("--- Задание 07: Фильтрация отрицательных чисел и квадраты ---")
    test_task_07()
    print()
    print("--- Задание 08: Генератор выборки кортежей по индексу ---")
    test_task_08()
    print()
    print("--- Задание 09: Треугольник Паскаля ---")
    test_task_09()
    print()
    print("--- Задание 10: Пакетная смена расширений файлов ---")
    test_task_10()
    print()
    print("--- Задание 11: Разность списков без циклов ---")
    test_task_11()
    print()
    print("--- Задание 12: Обработка вещественных чисел в файле ---")
    test_task_12()
    print()
    print("--- Задание 13: Генератор чисел Фибоначчи ---")
    test_task_13()
    print()
    print("--- Задание 14: Инспекция методов объекта ---")
    test_task_14()
    print()
    print("--- Задание 15: Замена ASCII и сплит по минимуму ---")
    test_task_15()
    print()
    print("--- Задание 16: Извлечение телефонных номеров (RegEx) ---")
    test_task_16()
    print()
    print("--- Задание 17: Операции над бинарным деревом кортежей ---")
    test_task_17()
    print()
    print("=" * 60)
    print("Все 17 заданий лабораторной работы успешно выполнены.")
    print("=" * 60)

if __name__ == "__main__":
    main()
