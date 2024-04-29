def unique_list(lst):
    """
    Удаляет дубликаты из списка
    """
    return list(set(lst))


def is_simple(i):
    """Проверяет простое ли число"""
    delitel = 2
    while delitel ** 2 <= i and i % delitel != 0:
        delitel += 1
    return delitel ** 2 > i


def simple_sort(a, b):
    """
    Возвращает простые числа в диапазоне от а до б
    """
    # а и б входят в диапазон?
    if a < b:
        return [i for i in range(a, b + 1) if is_simple(i)]
    elif a == b:
        return is_simple(a)
    else:
        c = b
        b = a
        return [i for i in range(c, b + 1) if is_simple(i)]


simple_sort(100, 1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """Расстояние до другой точки"""
        # проверяем, что other является экземпляром Point
        if not isinstance(other, Point):
            raise ValueError('other должен быть экземпляром Point')
        # возвращаем корень из суммы квадратов разницы координат
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def get_coords(self):
        """Координаты точки"""
        return self.x, self.y

    def set_coords(self, x, y):
        self.x = x
        self.y = y


def sort_by_length(lst):
    """
    Сортирует список строк по длине
    """
    # сортируем по длине
    for i in lst:
        if str == type(i):
            continue
        else:
            raise ValueError("элемент не является строкой")
    # если убрать reverse список строк будет сортироваться по возрастанию длины
    return sorted(lst, key=len, reverse=True)
