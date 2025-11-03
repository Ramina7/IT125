from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Оплата {amount} с кредитной карты выполнена."
    def refund(self, amount):
        return f"Возврат {amount} на кредитную карту выполнен."

class CryptoPayment(Payment):
    def pay(self, amount):
        return f"Оплата {amount} криптовалютой выполнена."
    def refund(self, amount):
        return f"Возврат {amount} криптовалютой выполнен."

payments = [CreditCardPayment(), CryptoPayment()]
for p in payments:
    print(p.pay(1000))
    print(p.refund(300))


class Course(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def get_materials(self):
        pass
    @abstractmethod
    def end(self):
        pass

class PythonCourse(Course):
    def start(self):
        print("Курс Python запущен.")
    def get_materials(self):
        return ["Переменные", "Циклы", "ООП"]
    def end(self):
        print("Курс Python завершён.")

class MathCourse(Course):
    def start(self):
        print("Курс Математики запущен.")
    def get_materials(self):
        return ["Алгебра", "Геометрия"]
    def end(self):
        print("Курс Математики завершён.")

courses = [PythonCourse(), MathCourse()]
for c in courses:
    c.start()
    print("Материалы:", c.get_materials())
    c.end()


class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass
    @abstractmethod
    def deliver(self):
        pass

class AirDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 10
    def deliver(self):
        return "Воздушная доставка завершена."

class GroundDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 5
    def deliver(self):
        return "Наземная доставка завершена."

class SeaDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 3
    def deliver(self):
        return "Морская доставка завершена."

deliveries = [AirDelivery(), GroundDelivery(), SeaDelivery()]
for d in deliveries:
    print(f"{d.__class__.__name__}: Стоимость {d.calculate_cost(100)} — {d.deliver()}")


class BankAccount:
    def __init__(self, owner, balance, pin):
        self.__owner = owner
        self.__balance = balance
        self.__pin = pin
    def deposit(self, amount, pin):
        if pin == self.__pin and amount > 0:
            self.__balance += amount
            return f"Баланс пополнен. Новый баланс: {self.__balance}"
        return "Ошибка!"
    def withdraw(self, amount, pin):
        if pin == self.__pin and 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Выдано {amount}. Остаток: {self.__balance}"
        return "Ошибка!"
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "PIN изменён."
        return "Ошибка PIN!"

acc = BankAccount("Рамина", 1000, 1234)
print(acc.deposit(500, 1234))
print(acc.withdraw(200, 1234))
print(acc.change_pin(1234, 4321))


class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self._status = "Обычный"
    def login(self, email, password):
        if email == self.__email and password == self.__password:
            return "Вход выполнен."
        return "Ошибка входа!"
    def upgrade_to_premium(self):
        self._status = "Премиум"
    def get_info(self):
        return {"email": self.__email, "status": self._status}

user = UserProfile("test@mail.com", "12345")
print(user.login("test@mail.com", "12345"))
user.upgrade_to_premium()
print(user.get_info())


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0
    def set_discount(self, percent, is_admin=False):
        if is_admin and 0 <= percent <= 100:
            self.__discount = percent
    def get_price(self):
        return self.price * (1 - self.__discount / 100)

p = Product("Телефон", 50000)
p.set_discount(10, is_admin=True)
print(f"Цена со скидкой: {p.get_price()}")


class TextFile:
    def open(self):
        print("Открыт текстовый файл.")
class ImageFile:
    def open(self):
        print("Открыт файл изображения.")
class AudioFile:
    def open(self):
        print("Открыт аудиофайл.")

def open_all(files):
    for f in files:
        f.open()

open_all([TextFile(), ImageFile(), AudioFile()])


class Car:
    def move(self, distance):
        speed = 100
        time = distance / speed
        print(f"Машина проехала {distance} км за {time} ч.")
class Truck:
    def move(self, distance):
        speed = 60
        time = distance / speed
        print(f"Грузовик проехал {distance} км за {time} ч.")
class Bicycle:
    def move(self, distance):
        speed = 20
        time = distance / speed
        print(f"Велосипед проехал {distance} км за {time} ч.")

def simulate_transport(transport_list):
    for t in transport_list:
        t.move(100)

simulate_transport([Car(), Truck(), Bicycle()])


class Student:
    def access_portal(self):
        return "Студент: просмотр расписания."
class Teacher:
    def access_portal(self):
        return "Преподаватель: выставление оценок."
class Administrator:
    def access_portal(self):
        return "Администратор: управление пользователями."

users = [Student(), Teacher(), Administrator()]
for u in users:
    print(f"{u.__class__.__name__}: {u.access_portal()}")
