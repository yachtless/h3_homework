# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование из строки вида "test string"
# в "<i><b>test string</b></i>"
import os


def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
            result = func(text)
            for tag in tags:
                if tag in tag_base:
                    result = tag_base[tag].replace('%text%', result)
            return result

        return wrapper

    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


# print(get_text('something else'))

# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

logs_dict = dict()


def log_reading(func):
    def wrapper(*args):
        result = func(*args)
        for file in result:
            if file.endswith('.log'):
                with open(file, 'r') as log_file:
                    logs_dict[file] = log_file.read()
        return result

    return wrapper


@log_reading
def get_files(path):
    file_list = list()
    for item in os.listdir(path):
        filename = os.path.join(path, item)
        if os.path.isfile(filename):
            file_list.append(filename)
    return file_list

# test_path = '../'
# print(get_files(test_path))
# print(logs_dict)
