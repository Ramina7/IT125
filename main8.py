class Account:
    def __init__(self, account_number, balance, pin_code):
        self.__account_number = account_number
        self.__balance = balance
        self.__pin_code = pin_code

    def deposit(self, amount, pin):
        if pin == self.__pin_code:
            self.__balance += amount
        else:
            print("Неверный PIN-код. Пополнение невозможно.")

    def withdraw(self, amount, pin):
        if pin == self.__pin_code:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Недостаточно средств.")
        else:
            print("Неверный PIN-код. Снятие невозможно.")

    def get_balance(self, pin):
        if pin == self.__pin_code:
            return self.__balance
        else:
            print("Неверный PIN-код. Доступ к балансу запрещен.")
            return None


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def set_discount(self, percent):
        if percent < 0:
            print("Процент скидки не может быть отрицательным.")
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
            print(f"{name} был/а добавлен/а в список.")
        else:
            print("Нет мест.")

    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)
            print(f"{name} был/а удален/а из списка.")
        else:
            print("Не найден/а в списке.")

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
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        pass

    def __str__(self):
        return f"{self.name} HP:{self.hp}"


class Warrior(Character):
    def attack(self):
        print(f"{self.name} атакует клинком.")


class Mage(Character):
    def attack(self):
        print(f"{self.name} атакует магией.")


class Archer(Character):
    def attack(self):
        print(f"{self.name} атакует из лука.")


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
        print(f"Воспроизводится видео: {self.title} {self.duration} минут.")


class Podcast(MediaFile):
    def play(self):
        print(f"Воспроизводится эпизод: {self.title} {self.duration} минут.")


from abc import ABC, abstractmethod


class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата в сумму {amount} кредитной картой прошла успешно.")


class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата в сумму {amount} криптовалютой прошла успешно.")


class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата в сумму {amount} банковским переводом прошла успешно.")


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Lion(Animal):
    def eat(self):
        print("Кошка ест мясо.")

    def sleep(self):
        print("Кошка спит вытянувшись на животе.")


class Elephant(Animal):
    def eat(self):
        print("Слон питается орехами.")

    def sleep(self):
        print("Слон спит с кайфом.")


class Snake(Animal):
    def eat(self):
        print("Змея питается чем ей по кайфу.")

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
        print("Файл сохранён.")


class PdfDocument(Document):
    def open(self):
        print("Открыт PDF документ.")

    def edit(self):
        print("Редактируется PDF документ.")

    def save(self):
        print("Файл сохранён.")


class SpreadsheetDocument(Document):
    def open(self):
        print("Открыта таблица.")

    def edit(self):
        print("Редактируется таблица.")

    def save(self):
        print("Файл сохранён.")


class Lesson(ABC):
    @abstractmethod
    def start(self):
        pass


class VideoLesson(Lesson):
    def start(self):
        print("Видео урок начался.")


class QuizLesson(Lesson):
    def start(self):
        print("Викторина началась.")


class TextLesson(Lesson):
    def start(self):
        print("Текстовый урок начался.")


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
        print("Менеджер. Планирует и управляет проектами.")


class Developer:
    def work(self):
        print("Разработчик. Пишет код и фиксит баги.")


class Designer:
    def work(self):
        print("Дизайнер. Создаёт дизайн интерфейсов.")


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

#ramina_samina_imran
