def _validate_symbols(input_str):
    """
    Проверяет строку на наличие запрещенных символов
    Подсказка: у строк есть метод, проверяющий наличие только був и цифр
    Возвращает True\False
    """
    return input_str.isalnum()


def _validate_letters_even(input_str):
    """
    Проверяет строку на четное количество букв
    Возвращает True\False
    """
    letters_list = [char for char in input_str if char.isalpha()]
    if letters_list:
        return not len(letters_list) % 2
    else:
        return False


def _validate_numbers_odd(input_str):
    """
    Проверяет строку на нечетное количество цифр
    Возвращает True\False
    """
    digits_list = [char for char in input_str if char.isdigit()]
    if digits_list:
        return bool(len(digits_list) % 2)
    else:
        return False


def validate_password(password):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    if not len(password):
        # we don't need to pass any of the checks
        # if the password is empty
        return ['Empty password']
    check_symbols = \
        '' if _validate_symbols(password) \
        else 'Contains improper symbols'
    check_letters_even = \
        '' if _validate_letters_even(password) \
        else 'Number of letters is not even'
    check_digits_odd = \
        '' if _validate_numbers_odd(password) \
        else 'Number of digits is not odd'

    errors_list = list()
    if check_symbols:
        errors_list.append(check_symbols)
    if check_letters_even:
        errors_list.append(check_letters_even)
    if check_digits_odd:
        errors_list.append(check_digits_odd)
    if errors_list:
        return errors_list
    else:
        return True


password = 'ggh_86'
print(_validate_symbols(password))
print(_validate_letters_even(password))
print(_validate_numbers_odd(password))
print('')
print(validate_password(password))
