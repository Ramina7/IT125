class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def info(self):
        return 'Животное: ' + self.name + '\nВозраст: ' + str(self.age) + '\nСреда обитания: ' + self.habitat


class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_color):
        super().__init__(name, age, habitat)
        self.fur_color = fur_color

    def feed_young(self):
        return self.name + ' кормит детёнышей молоком'

    def __str__(self):
        return self.info() + '\nЦвет шерсти: ' + self.fur_color


class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_type):
        super().__init__(name, age, habitat)
        self.scale_type = scale_type

    def warm_up(self):
        return self.name + ' греется на солнце'

    def __str__(self):
        return self.info() + '\nТип чешуи: ' + self.scale_type


mammal1 = Mammal('Лев', 5, 'Саванна', 'Золотистый')
reptile1 = Reptile('Крокодил', 12, 'Река', 'Жёсткая')

print(mammal1)
print(mammal1.feed_young())
print()
print(reptile1)
print(reptile1.warm_up())
class Zoo_show:
    def __init__(self): self.shows = {'Млекопитающие': {'price': 500, 'description': 'Шоу с участием львов, тигров и других животных с шерстью.'}, 'Пресмыкающиеся': {'price': 300, 'description': 'Шоу с крокодилами, змеями и другими пресмыкающимися.'}}

    def show_info(self):
        info = 'Информация о шоу:\n'
        for name in self.shows:
            desc = self.shows[name]['description']
            price = self.shows[name]['price']
            info += '\n' + name + '\n' + desc + '\nЦена: ' + str(price) + ' рублей\n'
        return info

    def choose_ticket(self, show_name):
        if show_name in self.shows:
            show = self.shows[show_name]
            return '\nВы выбрали шоу: ' + show_name + '\nЦена билета: ' + str(show['price']) + ' рублей\n' + show['description']
        else:
            return '\nТакого шоу нет. Попробуйте выбрать другое.'


zoo = Zoo_show()

print()
print(zoo.show_info())

chosen_show = input('Введите название шоу, которое вы хотите посетить с заглавной буквы: ')
print(zoo.choose_ticket(chosen_show)) 


