def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/

    ОТ СЕБЯ: эта версия ориентируется на catalog как часть пути
    и, соответственно, воспринимает строку типа test/catalog
    в качестве удовлетворяющей требованиям.
    Ввиду отсутствия дополнительных требований по проверке URL,
    строка типа test/catalog будет считаться подходящей.
    """
    # your code here
    result_list = list()
    for url in url_list:
        if type(url) is str:
            url_parts = url.split('/')
            for part in url_parts:
                if part == 'catalog':
                    result_list.append(url)
        else:
            continue
    return result_list


def catalog_finder2(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/

    ОТ СЕБЯ: эта версия считывает всю строку разом и, вместо того,
    чтобы раскладывать ее на составляющие, спрашивает, содержит
    ли строка подстроку '/catalog/'.
    При такой реализации строка типа 'test/catalog' не будет считаться
    удовлетворяющей требованиям ввиду отсутствия trailing /.
    По логике первая версия более гибкая с точки зрения применения,
    впрочем, все зависит от того, нужно ли нам потом что-то делать
    с остальными частями пути помимо 'catalog'
    """
    # your code here
    result_list = list()
    for url in url_list:
        if type(url) is str:
            if url.count('/catalog/') > 0:
                result_list.append(url)
        else:
            continue
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    # your code here
    trim_amount = int(len(input_str) / 2) - 1
    output_str = None
    output_str = input_str[trim_amount: len(input_str) - trim_amount]
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    # your code here
    output_dict = dict()
    letter_set = set(input_str)
    while len(letter_set) > 0:
        letter = letter_set.pop()
        count = input_str.count(letter)
        output_dict[letter] = count
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой

    ОТ СЕБЯ: по логике, аналогичной заданию get_str_center(), для нечетного
    количества букв в str1 первая "половина" будет на 1 символ длиннее.
    """
    # your code here
    half = int(len(str1) / 2)
    result_str = str1[0: half] + str2 + str1[half:]
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    # your code here
    even_int_list = list()
    for i in range(0, 101):
        if i % 2 == 0:
            even_int_list.append(i)
    return even_int_list
