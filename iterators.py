class FlatIterator:
    """
    Задание 1:
    Итератор для списка списков (1 уровень вложенности).
    """

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        self.outer_index = 0
        self.inner_index = 0
        return self

    def __next__(self):
        while self.outer_index < len(self.list_of_lists):
            current_list = self.list_of_lists[self.outer_index]

            if self.inner_index < len(current_list):
                item = current_list[self.inner_index]
                self.inner_index += 1
                return item

            self.outer_index += 1
            self.inner_index = 0

        raise StopIteration


class FlatIteratorAny:
    """
    Задание 3:
    Итератор для списков с любым уровнем вложенности.
    Реализация через стек итераторов.
    """

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.stack = [iter(self.list_of_list)]
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if isinstance(item, list):
                self.stack.append(iter(item))
                continue

            return item

        raise StopIteration
