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





def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    # your code here
    lst = [input_str[i].upper() if i%2 else input_str[i] for i in range(0, len(input_str))]
    return ''.join(lst)


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    # your code here
    return list(set(input_list))


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    # your code here
    avg_scores = list()
    dct = {i.split("|")[0] : i.split("|")[1].split(',') for i in score_list}
    for key in dct.keys():
        avg = 0
        for i in dct[key]:
            avg += int(i)
        avg = avg / len(dct[key])
        avg_scores.append(f"{key}|{avg}")
    return avg_scores


def DNA_pair(chain):
    """
    Дана одна цепь ДНК. Найти вторую цепь ДНК зная, что связи
    аденин (A) возможны с тимином (T), а гуанина (G) с цитозином (C).

    A <-> T, G <-> C

    in: "ATTGC" out: "TAACG"
    in: "GTAT" out: "CATA"
    """

    # your code here
    dict_conn = {"A": "T", "T": "A", "G": "C", "C": "G"}
    result_lst = [dict_conn[l] for l in chain]
    return ''.join(result_lst)


def domain_retrieval(url):
    parts = url.split('/')
    for part in parts:
        if '.' in part:
            domain_list = part.split('.')
            *_, name, domain_zone = domain_list
            return f"{name}.{domain_zone}."


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    # your code here
    input_list.sort()
    return input_list[-1:-4:-1]


print(three_biggest_int([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]))
