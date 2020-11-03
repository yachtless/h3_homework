# Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости.
# Декоратор должен перехватывать аргументы оборачиваемой функции
# Декоратор должен иметь хранилище, где будут сохраняться все перехваченные аргументы и результаты выполнения
# декорируемой функции
# Декоратор должен проверять наличие перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась
# с такими аргументами, она не будет вызываться снова, вместо этого декоратор вернет сохраненное значение.
# Декоратор должен принимать один аргумент - максимальный размер хранилища.
# Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под новый.

dict_cache_results = dict()


def do_cache(maxsize):
    def decorator_cache(func):
        def trim_cache():
            removal_key = set(dict_cache_results).pop()
            dict_cache_results.pop(removal_key)

        def wrapper_cache(*args):
            if not (func, tuple(args)) in dict_cache_results:
                if len(dict_cache_results) == maxsize:
                    trim_cache()
                dict_cache_results[(func, tuple(args))] = func(*args)
            return dict_cache_results[(func, tuple(args))]
        return wrapper_cache

    return decorator_cache


@do_cache(maxsize=3)
def get_value(a, b):
    return a ** b


@do_cache(maxsize=3)
def get_value_power(a, b):
    return a ** b


@do_cache(maxsize=3)
def get_value_multi(a, b):
    return a * b


@do_cache(maxsize=3)
def get_value_add(a, b):
    return a + b


get_value_add(2, 2)
get_value_multi(3, 2)
get_value_add(48, 3)
get_value_power(10, 3)
get_value_add(48, 3)
