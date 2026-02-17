def flat_generator_1(list_of_lists):
    """
    Задание 2:
    Генератор для списка списков (1 уровень вложенности).
    """
    for inner in list_of_lists:
        for item in inner:
            yield item


def flat_generator_any(list_of_list):
    """
    Задание 4 (необязательное):
    Генератор для списков с любым уровнем вложенности.
    Рекурсивная реализация через `yield from`.
    """
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator_any(item)
        else:
            yield item
