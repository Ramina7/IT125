class Account:
    def __init__(self, account_number, balance, pin_code):
        self.__account_number = account_number
        self.__balance = balance
        self.__pin_code = pin_code

    def deposit(self, amount, pin):
        if pin == self.__pin_code:
            self.__balance += amount

    def withdraw(self, amount, pin):
        if pin == self.__pin_code and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self, pin):
        if pin == self.__pin_code:
            return self.__balance
        else:
            return "Неверный PIN"


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def set_discount(self, percent):
        if percent < 0:
            print("Процент скидки не может быть отрицательным")
        else:
            new_price = self.__price * (1 - percent / 100)
            if new_price < 0:
                self.__price = 0
            else:
                self.__price = new_price

    def final_price(self):
        return self.__price


class Course:
    def __init__(self, name, students, max_places):
        self.__name = name
        self.__students = students
        self.__max_places = max_places

    def add_student(self, name):
        if len(self.__students) < self.__max_places:
            self.__students.append(name)
            print(f"{name} добавлен(а)")
        else:
            print("Нет мест")

    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)
            print(f"{name} удалён(а)")
        else:
            print(f"{name} не найден(а)")

    def get_students(self):
        return self.__students.copy()


class SmartWatch:
    def __init__(self, battery):
        self.__battery = battery

    def use(self, minutes):
        decrease = minutes / 10
        self.__battery -= decrease
        if self.__battery < 0:
            self.__battery = 0

    def charge(self, percent):
        self.__battery += percent
        if self.__battery > 100:
            self.__battery = 100

    def get_battery(self):
        return self.__battery


class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def travel_time(self, distance):
        return distance / self.speed


class Bus(Transport):
    pass


class Train(Transport):
    pass


class Airplane(Transport):
    def travel_time(self, distance):
        time = super().travel_time(distance)
        return time * 0.8


class Order:
    def __init__(self, food, base_price):
        self.food = food
        self.base_price = base_price

    def calculate_total(self):
        return self.base_price


class DineInOrder(Order):
    def calculate_total(self):
        tip = self.base_price * 0.1
        return self.base_price + tip


class TakeAwayOrder(Order):
    def calculate_total(self):
        discount = self.base_price * 0.05
        return self.base_price - discount


class DeliveryOrder(Order):
    def calculate_total(self):
        delivery = self.base_price * 0.15
        return self.base_price + delivery


class Character:
    def __init__(self, name, HP, ATK):
        self.name = name
        self.hp = HP
        self.atk = ATK

    def attack(self):
        pass

    def __str__(self):
        return f"{self.name} HP:{self.hp}"


class Warrior(Character):
    def attack(self):
        print(f"{self.name} атакует мечом.")


class Mage(Character):
    def attack(self):
        print(f"{self.name} атакует магией.")


class Archer(Character):
    def attack(self):
        print(f"{self.name} атакует луком.")


class MediaFile:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        pass


class AudioFile(MediaFile):
    def play(self):
        print(f"Воспроизводится аудио: {self.title} {self.duration} минут.")


class VideoFile(MediaFile):
    def play(self):
        print(f"Воспроизводится видео с изображением: {self.title} {self.duration} минут.")


class Podcast(MediaFile):
    def play(self):
        print(f"Воспроизводится эпизод подкаста: {self.title} {self.duration} минут.")


from abc import ABC, abstractmethod


class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} кредитной картой прошла успешно.")


class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} криптовалютой прошла успешно.")


class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата {amount} банковским переводом прошла успешно.")


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Lion(Animal):
    def eat(self):
        print("Лев ест мясо.")

    def sleep(self):
        print("Лев спит вытянувшись.")


class Elephant(Animal):
    def eat(self):
        print("Слон ест орехи.")

    def sleep(self):
        print("Слон спит спокойно.")


class Snake(Animal):
    def eat(self):
        print("Змея ест что хочет.")

    def sleep(self):
        print("Змея спит свернувшись клубком.")


class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def save(self):
        pass


class WordDocument(Document):
    def open(self):
        print("Открыт документ Word.")

    def edit(self):
        print("Редактируется документ Word.")

    def save(self):
        print("Файл Word сохранён.")


class PdfDocument(Document):
    def open(self):
        print("Открыт PDF документ.")

    def edit(self):
        print("Редактируется PDF документ.")

    def save(self):
        print("Файл PDF сохранён.")


class SpreadsheetDocument(Document):
    def open(self):
        print("Открыта таблица.")

    def edit(self):
        print("Редактируется таблица.")

    def save(self):
        print("Файл таблицы сохранён.")


class Lesson(ABC):
    @abstractmethod
    def start(self):
        pass


class VideoLesson(Lesson):
    def start(self):
        print("Начинается видеоурок.")


class QuizLesson(Lesson):
    def start(self):
        print("Начинается тест.")


class TextLesson(Lesson):
    def start(self):
        print("Начинается текстовый урок.")


class EmailNotification:
    def send(self, message):
        print(f"Отправка Email: {message}")


class SMSNotification:
    def send(self, message):
        print(f"Отправка SMS: {message}")


class PushNotification:
    def send(self, message):
        print(f"Отправка Push-уведомления: {message}")


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        print(4 * self.side)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print(2 * 3.14 * self.radius)


class Triangle:
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3

    def perimeter(self):
        print(self.a + self.b + self.c)


class Manager:
    def work(self):
        print("Менеджер планирует и управляет.")


class Developer:
    def work(self):
        print("Разработчик пишет код.")


class Designer:
    def work(self):
        print("Дизайнер создаёт дизайн.")


class FireSpell:
    def cast(self, target):
        print(f"{target} получает урон огнём!")


class IceSpell:
    def cast(self, target):
        print(f"{target} заморожен!")


class HealingSpell:
    def cast(self, target):
        print(f"{target} восстанавливает здоровье!")


target = "Волан-де-Морт"

spells = [FireSpell(), IceSpell(), HealingSpell()]
for spell in spells:
    spell.cast(target)