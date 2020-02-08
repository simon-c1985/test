# # # # # # # # # class Car:
# # # # # # # # #     def __init__(self, name, door, color, year):
# # # # # # # # #         self.name = name
# # # # # # # # #         self.door = door
# # # # # # # # #         self.color = color
# # # # # # # # #         self.year = year
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # mazda_car = Car(name='Mazda CX-9', door='4', year='2019', color='white')
# # # # # # # # # print(f'The car is {mazda_car.name} \nthey have {mazda_car.door} door\'s'
# # # # # # # # #       f'\nthe color is {mazda_car.color}\n{mazda_car.year} year')
# # # # # # # # # help(Car)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class BlogPost:
# # # # # # # # #     def __init__(self, user_name, text, number_of_likes):
# # # # # # # # #         self.user_name = user_name
# # # # # # # # #         self.text = text
# # # # # # # # #         self.number_of_likes = number_of_likes
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # jack = BlogPost('Jack', 'asfgsfdgsd\nwergwer\n\tsdfgsdf', '12')
# # # # # # # # # john = BlogPost(user_name='John', number_of_likes='5', text='dfsd')
# # # # # # # # # print(jack)
# # # # # # # # # print(john)
# # # # # # # # # print(john.number_of_likes)
# # # # # # # # # john.number_of_likes = 20
# # # # # # # # # print(john.number_of_likes)
# # # # # # # #
# # # # # # # #
# # # # # # # # class Car:
# # # # # # # #     wheels_number = 4
# # # # # # # #
# # # # # # # #     def __init__(self, name, door, color, year):
# # # # # # # #         self.name = name
# # # # # # # #         self.door = door
# # # # # # # #         self.color = color
# # # # # # # #         self.year = year
# # # # # # # #
# # # # # # # #     def drive(self, city):
# # # # # # # #         print(f'car {self.name} is driving in {city}')
# # # # # # # #
# # # # # # # #     def change_color(self, new_color):
# # # # # # # #         self.color = new_color
# # # # # # # #
# # # # # # # #
# # # # # # # # opel_car = Car('Opel Tigra', '4', 'grey', '2000')
# # # # # # # # opel_car.drive('Spb')
# # # # # # # # # print(opel_car.year)
# # # # # # # # # print(opel_car.door)
# # # # # # # # print(opel_car.color)
# # # # # # # # # print(opel_car.name)
# # # # # # # # opel_car.change_color('blue')
# # # # # # # # print(opel_car.color)
# # # # # # #
# # # # # # #
# # # # # # # class Circle:
# # # # # # #     pi = 3.14
# # # # # # #
# # # # # # #     def __init__(self, radius=1):
# # # # # # #         self.radius = radius
# # # # # # #         self.circumference = 2 * self.pi * self.radius
# # # # # # #
# # # # # # #     def get_area(self):
# # # # # # #         return self.pi * self.radius ** 2
# # # # # # #
# # # # # # #     # def get_circumference(self):
# # # # # # #     #     return 2 * self.pi * self.radius
# # # # # # #
# # # # # # #
# # # # # # # circle_area = 3
# # # # # # # circle_1 = Circle(circle_area)
# # # # # # # print(circle_1.get_area())
# # # # # # # circle = Circle()
# # # # # # # print(circle.get_area())
# # # # # # # print(Circle(5).circumference)
# # # # # #
# # # # # #
# # # # # # # class BankAccount:
# # # # # # #     def __init__(self, client_id, client_first_name, client_last_name):
# # # # # # #         self.client_id = client_id
# # # # # # #         self.client_first_name = client_first_name
# # # # # # #         self.client_last_name = client_last_name
# # # # # # #         self.balance = 0.0
# # # # # # #
# # # # # # #     def add(self, value):
# # # # # # #         self.balance += value
# # # # # # #
# # # # # # #     def withdraw(self, value):
# # # # # # #         self.balance -= value
# # # # # # #
# # # # # # #     def balance_account(self):
# # # # # # #         print(self.balance)
# # # # # # #
# # # # # # #
# # # # # # # account_1 = BankAccount(1, 'Jack', 'Black')
# # # # # # # account_2 = BankAccount(2, 'Jim', "Worm")
# # # # # # #
# # # # # # # account_1.add(123.32)
# # # # # # # account_2.add(33)
# # # # # # # account_1.withdraw(12)
# # # # # # #
# # # # # # # print(account_1.balance)
# # # # # # # print(account_2.balance)
# # # # # # # account_1.balance_account()
# # # # # #
# # # # # #
# # # # # # class Car:
# # # # # #     wheels_number = 4
# # # # # #
# # # # # #     def __init__(self, name, door, color, year):
# # # # # #         self.name = name
# # # # # #         self.door = door
# # # # # #         self.color = color
# # # # # #         self.year = year
# # # # # #         print('Car is created')
# # # # # #
# # # # # #     def drive(self, city):
# # # # # #         print(f'car {self.name} is driving in {city}')
# # # # # #
# # # # # #     def change_color(self, new_color):
# # # # # #         self.color = new_color
# # # # # #         print(f'Color is changed to {new_color}')
# # # # # #
# # # # # #
# # # # # # class Truck(Car):
# # # # # #
# # # # # #     wheels_number = 6
# # # # # #
# # # # # #     def __init__(self, name, door, color, year, is_crashed):
# # # # # #         self.is_crashed = is_crashed
# # # # # #         Car.__init__(self, name, door, color, year)
# # # # # #         print('Truck is created')
# # # # # #
# # # # # #     def drive(self, city):
# # # # # #         print(f'Truck {self.name} is driving in {city}')
# # # # # #
# # # # # #     def load_cargo(self, weight):
# # # # # #         print(f'The cargo is loaded. Weight is {weight} kg')
# # # # # #
# # # # # #
# # # # # # man_truck = Truck('Man', 4, 'white', 2015, True)
# # # # # # man_truck.drive('msk')
# # # # # # print(man_truck.wheels_number)
# # # # # # man_truck.change_color('red')
# # # # # # print(man_truck.is_crashed)
# # # # # # man_truck.load_cargo(100)
# # # # # #
# # # # # #
# # # # #
# # # # #
# # # # # class Animal:
# # # # #     def __init__(self, name):
# # # # #         self.name = name
# # # # #
# # # # #     def speak(self):
# # # # #         raise NotImplementedError('Class successor must implementes this method')
# # # # #
# # # # #
# # # # # class Dog(Animal):
# # # # #     def __init__(self, name):
# # # # #         Animal.__init__(self, name)
# # # # #
# # # # #
# # # # #     def speak(self):
# # # # #         print(f'{self.name} is saying woof')
# # # # #
# # # # #
# # # # # class Cat(Animal):
# # # # #     def __init__(self, name):
# # # # #         Animal.__init__(self, name)
# # # # #
# # # # #     def speak(self):
# # # # #         print(f'{self.name} is saying meow')
# # # # #
# # # # #
# # # # # class Mouse(Animal):
# # # # #     def __init__(self, name):
# # # # #         Animal.__init__(self, name)
# # # # #
# # # # #     def speak(self):
# # # # #         print(f'{self.name} is saying pee-pee-pee')
# # # # #
# # # # #
# # # # # class Fish(Animal):
# # # # #     def __init__(self, name):
# # # # #         Animal.__init__(self, name)
# # # # #
# # # # #     def speak(self):
# # # # #         print(f'{self.name} is saying nothing')
# # # # #
# # # # #
# # # # # spike = Dog('Spike')
# # # # # tom = Cat('Tom')
# # # # # jerry = Mouse('Jerry')
# # # # # freddy = Fish('Freddy')
# # # # # pet_list = [spike, tom, jerry, freddy]
# # # # #
# # # # # for pet in pet_list:
# # # # #     pet.speak()
# # # # #
# # # # #
# # # # # def pet_voice(pet):
# # # # #     pet.speak()
# # # # #
# # # # #
# # # # # pet_voice(spike)
# # # # # pet_voice(tom)
# # # # # pet_voice(freddy)
# # # # #
# # # #
# # # #
# # # # class Swimmable:
# # # #     def __init__(self, name):
# # # #         print('Method init of Swimmable')
# # # #         self.name = name
# # # #
# # # #     def greeting(self):
# # # #         print(f'Hello! My name is {self.name} and I can swim')
# # # #
# # # #     def swim(self):
# # # #         print(f'I\'m swimming')
# # # #
# # # #
# # # # class Walkable:
# # # #     def __init__(self, name):
# # # #         print('Method init of Walkable')
# # # #         self.name = name
# # # #
# # # #     def greeting(self):
# # # #         print(f'Hello! My name is {self.name} and I can walk')
# # # #
# # # #     def walk(self):
# # # #         print(f'I\'m walking')
# # # #
# # # #
# # # # class Flyable:
# # # #     def __init__(self, name):
# # # #         print('Method init of Flyable')
# # # #         self.name = name
# # # #
# # # #     def greeting(self):
# # # #         print(f'Hello! My name is {self.name} and I can fly')
# # # #
# # # #     def fly(self):
# # # #         print(f'I\'m flying')
# # # #
# # # #
# # # # class GameCharacter(Swimmable, Walkable, Flyable):
# # # #     def __init__(self, name):
# # # #         print('Method init of GameCharacter')
# # # #         self.name = name
# # # #         Swimmable.__init__(self, name)
# # # #         Walkable.__init__(self, name)
# # # #         Flyable.__init__(self, name)
# # # #
# # # #     # def greeting(self):
# # # #     #     print(f'Hello! My name is {self.name}!')
# # # #
# # # #
# # # # james = GameCharacter('James')
# # # # james.greeting()
# # # # james.swim()
# # # # james.fly()
# # # # print(isinstance(james, Walkable))
# # #
# # #
# # # class A:
# # #     def some_method(self):
# # #         print('Method of class A')
# # #
# # #
# # # class B(A):
# # #     def some_method(self):
# # #         print('Method of class B')
# # #
# # #
# # # class C(A):
# # #     def some_method(self):
# # #         print('Method of class C')
# # #
# # #
# # # class D(B, C):
# # #     def some_method(self):
# # #         print('Method of class D')
# # #
# # #
# # # help(D)
# # # # some_object = D()
# # # # some_object.some_method()
# #
# #
# # class GameCharacter:
# #     def __init__(self, name, health, level):
# #         self.name = name
# #         self.health = health
# #         self.level = level
# #
# #     def speak(self):
# #         print(f'Hi, my name is {self.name}')
# #
# #
# # class Villain(GameCharacter):
# #     def __init__(self, name, health, level):
# #         GameCharacter.__init__(self, name, health, level)
# #
# #     def speak(self):
# #         print(f'Hi? my name is {self.name} and I will kill you')
# #
# #     def kill(self, other):
# #         other.health = 0
# #         print('Bang-bang, now you\'re dead')
# #
# #
# # james = GameCharacter('James', 100, 1)
# # jim = Villain('jim', 100, 2)
# # james.speak()
# # jim.speak()
# # print(james.health)
# # jim.kill(james)
# # print(james.health)
#
#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def __len__(self):
#         return self.age
#
#     def __del__(self):
#         self.age = 1
#         print(f'{self.first_name} {self.last_name} is age {self.age}')
#
#     def __add__(self, other):
#         return self.age + other.age
#
#
# jack = Person('Jack', 'Black', 45)
# jane = Person('Jane', 'White', 25)
#
# # print(jack)
# # print(len(jack))
# # # del jack
# # # print(jack)
# #
# # x = 5
# # y = 3
# #
# # a = '5'
# # b = '3'
#
# # print(x.__add__(y))
# # print(a.__add__(b))
# print(jack.__add__(jane))
#
# print(jack)


class Chain:
    def __init__(self, numbers_of_item):
        self.number_of_items = numbers_of_item

    def __str__(self):
        return f'Chain with {self.number_of_items} items'

    def __len__(self):
        return self.number_of_items


jack = Chain(19)

print(jack)
print(len(jack))
