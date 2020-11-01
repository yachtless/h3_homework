from datetime import date
# d = date(1969, 6, 26) - конструктор даты
# d.year < 2020 - проверка даты

# database - список словарей, эмулирующий базу данных со строками и полями
database = list()


def _validate_input(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей, валидирует каждый из словарей на наличие
    всех необходимых полей и тип их данных. Возвращает bool в зависимости от результатов проверки.
    Правила валидации:
    first_name - string, не пустой, короче 48 символов
    last_name - string, не пустой, короче 64 символов
    birth - date, не пустой, не в будущем, не старше 100 лет
    email - string, формат строка, затем @, затем опять строка, точка,
    строка от 2 до 3 символов
    Допустимые символы в email: буквы, цифры
    """
    first_name_len = 48
    last_name_len = 64
    max_age = 100
    for row in data:
        if not _validate_name(row['first_name'], first_name_len):
            return False
        if not _validate_name(row['last_name'], last_name_len):
            return False
        if not _validate_birth(row['birth'], max_age):
            return False
        if not _validate_email(row['email']):
            return False
    return True


def _validate_name(name, max_len):
    if not type(name) is str:
        return False
    if not 0 < len(name) < max_len:
        return False
    return True


def _validate_birth(birth, max_age):
    if not type(birth) is date:
        return False
    if birth > date.today():
        return False
    if date.today().year - birth.year > max_age:
        return False
    return True


def _validate_email(email):
    if not type(email) is str:
        return False
    email_parts = email.split('@')
    if len(email_parts) != 2:
        return False
    if not email_parts[0].isalnum():
        return False
    domain_parts = email_parts[1].split('.')
    if len(domain_parts) == 1:
        return False
    if not 2 <= len(domain_parts[-1]) <= 3:
        return False
    return True


def insert_to_db(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей с данными, валидирует каждую запись с
    помощью вспомогательной функции validate_input, и если данные валидны,
    добавляет их в database.
    Возвращает bool по результатам успешного/неуспешного выполнения.
    """
    if _validate_input(data):
        database.extend(list(data))
        return True
    return False


def _format_output(data):
    """
    Принимает тапл диктов с данными из БД.
    Форматирует данные в таблицу вида:
    ---------------------------------------
    | название колонки | название колонки |
    ---------------------------------------
    | значение строки  | значение колонки |
    Возвращает таблицу строкой.
    """
    if not data:
        return
    table = ""
    dict_widths = {header: len(header) for header in data[0]}
    for entry in data:
        for value in entry:
            if len(str(entry[value])) > dict_widths[value]:
                dict_widths[value] = len(str(entry[value]))
    total_len = sum(dict_widths.values(), len(dict_widths) + 1)
    horiz_row = ''.join(['-' for i in range(total_len)])
    headers_row = f"|{'|'.join([header.ljust(dict_widths[header]) for header in dict_widths])}|"
    table = f"{horiz_row}\n{headers_row}\n{horiz_row}"
    for entry in data:
        upacked_lst = [str(entry[header]).ljust(dict_widths[header]) for header in entry]
        entry_str = f"|{'|'.join(upacked_lst)}|"
        table = f"{table}\n{entry_str}"
    return f"{table}\n{horiz_row}"


def select_from_db(field, value):
    """
    Функция возвращает таблицу (строка) с релевантными результатами, где переданное значение встречается в переданном ключе.
    Форматирование результатов выполняет вспомогательная функция _format_output
    """
    result_coll = (item for item in database if item[field] == value)
    return _format_output(tuple(item for item in result_coll))


in_data = ({"first_name": "Guido", "last_name": "Van Rossum",
            "birth": date(1969, 6, 27), "email": "iamguido@python.org"},
            {"first_name": "Guido", "last_name": "Not Van Rossum",
            "birth": date(1969, 6, 28), "email": "iamanotherguido@python.org"})
result = insert_to_db(in_data)
#print(result)
#print(database)
print(select_from_db('first_name', 'Guido'))
