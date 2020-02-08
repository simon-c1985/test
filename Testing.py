# def divide(a, b):
#     assert b != 0, 'b must not equals 0'
#     return a / b
#
#
# print(divide(2, 2))
# print(divide(2, 0))


# def multiply_positive_numbers(a, b):
#     assert a > 0 and b > 0, 'a and b must be positive'
#     print(a * b)
#
#
# multiply_positive_numbers(3, -5)


# def get_access(password):
#     password_list = [111, 222, 333]
#     assert int(password) in password_list, 'Password is invalid'
#     print('You can make dangerous stuff')
#
#
# password_1 = int(input('Please input the password'))
#
# get_access(password_1)


# import unittest
# import upper
#
#
# class TestUpper(unittest.TestCase):
#     def test_one_word(self):
#         text = 'hello!'
#         result = upper.upper_text(text)
#         self.assertEqual(result, 'Hello!')
#         self.assertNotEqual(result, 'hello!')
#
#     def test_two_word(self):
#         text = 'hello world!'
#         result = upper.upper_text(text)
#         self.assertEqual(result, 'Hello World!')
#
#
# if __name__ == '__main__':
#     unittest.main()


# from random import choice
#
#
# def greet(name, isEnemy):
#     if not isinstance(isEnemy, bool):
#         raise ValueError('isEnemy must be a boolean type')
#     if isEnemy:
#         return f'Hello {name}! I will kill you, bastard!'
#     else:
#         return f'Hello {name}! How are you?'
#
#
# def eat_burgers(number):
#     if number >= 3:
#         return f'Oh! I overate!'
#     else:
#         return f'Mmm! That was excellent!'
#
#
# def can_fly(name):
#     if name == 'Batman':
#         return True
#     else:
#         return False
#
#
# def get_arsenal():
#     return choice(('knife', 'handgun', 'machine gun'))

# class Shooter:
#     def __init__(self, name, money=1000, guns=None):
#         if guns is None:
#             guns = []
#         self.name = name
#         self.money = money
#         self.guns = guns
#
#     def get_cash(self, cash):
#         self.money = self.money + cash
#         if cash > 1000:
#             return 'Let\'s go to the party!'
#         else:
#             return 'Let\'s go for more money!'
#
#     def greet(self):
#         if self.money > 100:
#             return 'Hello! How are you?'
#         else:
#             return 'Hello! I need cash!'
#
#     def buy_gun(self, new_gun, gun_cost):
#         if self.money >= gun_cost:
#             self.money -= gun_cost
#             self.guns.append(new_gun)
#             return 'Wow! Cool stuff!'
#         else:
#             return 'Sorry:( I have no money for this toy.'





