# -*- coding: utf-8 -*-
"""
Для каждого регулярного выражения, которое требуется написать,
указана строка, в которой нужно найти подстроки, а следом
после стрелки (--->) указан список подстрок, которые нужно найти.

Для корректной работы автоматических тестов не переименовывайте переменные
REGEXP_1, REGEXP_2, ..., REGEXP_8!

Задача была взята из курса http://cs.mipt.ru/advanced_python/lessons/lab12.html.
"""


# Пример:


# ввод         вывод
# a b A B ---> A, B
# cdeFGH  ---> FGH
_REGEXP_0 = r"[A-Z]"  # регулярное выражение


# Ваше решение:


# 1 a 1 2 b ---> a, b
# z 2 y     ---> z, y
REGEXP_1 = r"[a-z]"

# aaa bbb ccc ---> aaa, bbb, ccc
# ddd eee fgh ---> ddd, eee, fgh
# a1b c2d e3f ---> a1b, c2d, e3f
REGEXP_2 = r"\w+"

# a aa aaa ---> aa, aaa
# b bb bbb ---> bb, bbb
# a bb aaa ---> bb, aaa
REGEXP_3 = r"[a-z]{2,}"

# 1.1.1.1 aaaa bbbbb      ---> 1.1.1.1
# a.a.a.a bbbb 2.2.2.2    ---> 2.2.2.2
# 3.3.3.3 cccc 4.4.4.4    ---> 3.3.3.3, 4.4.4.4
# 255.23.0.1 cccc 4.4.4.4 ---> 255.23.0.1, 4.4.4.4
# 255.0.23.1 cccc 4.4.4.4 ---> 255.0.23.1, 4.4.4.4
REGEXP_4 = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# aaa Abbb ccc ---> Abbb
# Aaa Abbb ccc ---> Aaa, Abbb
# Caa Cbb Accc ---> Accc
REGEXP_5 = r"[A][a-z]+"

# a b c d e f ---> a, b, e, f
# abcdef      ---> a, b, e, f
# adf         ---> a, f
# acf         ---> a, f
REGEXP_6 = r"[abef]"

# aaa +1.0 bb              ---> +1.0
# aaa -1.0 bb              ---> -1.0
# aaa -123.234 bb +111.999 ---> -123.234, +111.999
REGEXP_7 = r"[-+]?[0-9]*\.?[0-9]+"

# aaa 18-04-2016 bbb            ---> 18-04-2016
# aaa 18.04.2016 bbb            ---> 18.04.2016
# aaa 18-04-ABCD bbb 18.04.2016 ---> 18.04.2016
# aaa 18/04/ABCD bbb 18/04/2016 ---> 18/04/2016
# aaa 18/04/ABCD bbb 18/4/2016  ---> 18/4/2016
REGEXP_8 = r"\d{1,2}[\.\-/]\d{1,2}[\.\-/]\d{4}"
