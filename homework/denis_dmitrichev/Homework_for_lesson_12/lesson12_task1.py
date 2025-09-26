class Flowers:
    def __init__(self, name, color, live_time, price, stem_length):
        self.name = name
        self.color = color
        self.live_time = live_time
        self.price = price
        self.stem_length = stem_length


class Roses(Flowers):
    def __init__(self, name, color, live_time, price, stem_length):
        super().__init__(name, color, live_time, price, stem_length)


red_rose = Roses('Роза красная', 'red', 5, 300, 30)
white_rose = Roses('Роза белая', 'white', 4, 350, 32)
black_rose = Roses('Роза черная', 'black', 6, 400, 31)


class Herbers(Flowers):
    def __init__(self, name, color, live_time, price, stem_length):
        super().__init__(name, color, live_time, price, stem_length)


yellow_herber = Herbers('Желтый гербер', 'yellow', 3, 315, 25)
red_herber = Herbers('Красный гербер', 'red', 6, 320, 27)
orange_herber = Herbers('Оранжевый гербер', 'orange', 4, 310, 33)


class Tulips(Flowers):
    def __init__(self, name, color, live_time, price, stem_length):
        super().__init__(name, color, live_time, price, stem_length)


red_tulip = Tulips('Красный тюльпан', 'red', 2, 130, 25)
yellow_tulip = Tulips('Желтый тюльпан', 'yellow', 3, 145, 26)
white_tulip = Tulips('Белый тюльпан', 'white', 2, 150, 24)


class Buket:
    def __init__(self, lst):
        self.lst = lst

    def price(self):
        """
        Подсчитываем общую стоимость всех цветов в букете
        возвращает int стоимость всех цветов в букете
        :param self: принимает экземпляр список класса Buket,
        заполненный экземплярами дочерних классов родительского класса Flowers
        """
        return sum(map(lambda x: x.price, self.lst))

    def sorting(self, param, kind):
        """
        Сортируем список экземпляров класса по заданному параметру,
        возвращаем новый список из аттрибутов name каждого экземпляра класса
        :param self: принимает список экземпляров класса
        :param param: принимает строковое значение аттрибута экземпляра по которому будет происходить сортировка
        :param kind: bool - определяет как сортировать: по возрастанию или убыванию
        """
        # тут у меня был другой код и он мне отдавал список объектов питона, а нужен был список аттрибутов name
        # для идентификации цветов в списке, поэтому пришлось воспользоваться помощью нейросети
        # и она мне подсказала как можно с помощью key=lambda и функции getattr достать нужное значение
        # про магический метод позже посмотрел, домашку начал параллельно делать с просмотром 12 урока
        lst2 = sorted(self.lst, key=lambda item: getattr(item, param), reverse=kind)
        return [getattr(item, 'name') for item in lst2]

    def find_flower(self, time_of_life):
        """
        Поиск цветов по аттрибуту время жизни цветка
        возвращаем новый список из аттрибутов name цветов подходящих под условия поиска
        :param self: принимает список экземпляров класса
        :param time_of_life: принимает параметр int - время жизни цветка
        """
        return [flower.name for flower in self.lst if flower.live_time == time_of_life]

    def buket_death(self):
        """
        определяем время увядания букета по среднему времени жизни всех цветов в букете
        возвращаем float сумму дней жизни каждого цветка, деленное на количество
        :param self: принимает список экземпляров класса
        """
        live_lst = list(map(lambda x: x.live_time, self.lst))
        return sum(live_lst) / len(live_lst)


buket = Buket([red_rose, black_rose, white_rose, white_tulip,
              yellow_tulip, red_tulip, yellow_herber, red_herber, orange_herber])


print(buket.price())
print(buket.find_flower(6))
print(buket.buket_death())
print(buket.sorting('live_time', False))
