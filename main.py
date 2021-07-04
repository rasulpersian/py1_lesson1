"""
1.	Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
явно, в программе.
"""

ex_list = [1, "Test", None, 2.2, (1, "Test", None, 2.2)]
for n, a in enumerate(ex_list):
    print(n, ": ", type(a))

"""
2.	Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно 
 использовать функцию input().
"""
list_w = input("Введите элементы списка: ").split()
list_w[:-1:2], list_w[1::2] = list_w[1::2], list_w[:-1:2]
print(list_w)
"""
3.	Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, 
весна, лето, осень). Напишите решения через list и dict.
"""

months = {
    1: 'Январь, часто морозный, довольно суровый. ',
    2: 'Февраль, то с метелями, то с оттепелями. ',
    3: 'Март, первый месяц весны, всё еще холодный, часто смахивает на зиму. ',
    4: 'Апрель, весенняя капель! Всё тает, пробуждается жизнь. ',
    5: 'Май, почти лето, ночи холодные, дни теплые, как летом. ',
    6: 'Июнь. Первый месяц лета. Зелень в самом соку, яркая.',
    7: 'Июль. Серединка лета, тепло, солнечно.',
    8: 'Август. Пошли фрукты, ягоды, витаминный месяц.',
    9: 'Сентябрь. Еще больше фруктов и овощей, детям в школу. ',
    10: 'Октябрь, днем всё еще тепло, по ночам холодно.',
    11: 'Ноябрь. Зима на носу и это чувствуется, утепляемся! ',
    12: 'Декабрь. Зима. Первый ее месяц. Скоро Новый год! '
}
while True:
    ans = int(input("Введите число месяца: "))
    if ans > 12 or ans < 1:
        print("Такой месяц не существует. "
              "Введите месяц в виде целого числа от 1 до 12!!!")
    else:
        print(months.get(ans))
        break

"""
4.	Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. 
Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
"""
worlds = input("Вводит строку из нескольких слов, разделённых пробелами: ")
list_worlds = worlds.split()
for num, a in enumerate(list_worlds, 1):
    print(num, ':', a[:10])

"""
5.	Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя
нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый 
элемент с тем же значением должен разместиться после них. Подсказка. 
Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

reting = [2, 3, 5]
print('Рейтинг:')
reting.sort(reverse=True)
for a in reting:
    print(a, end=', ')
check = 1
while check:
    print('\nДля выхода нажмите Enter ')
    new_el_r = int(input('Введите новй элемент рейтинга: '))
    if new_el_r == 0:
        check = False
    else:
        reting.append(new_el_r)
        print('Новый рейтинг:')
        reting.sort(reverse=True)
        for a in reting:
            print(a, end=', ')


"""
6.	*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, 
то есть характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. 
Тогда значение — список значений-характеристик, например, список названий товаров.

Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}

"""