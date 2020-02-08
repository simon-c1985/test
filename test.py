# import unittest
# import Testing
#
#
# class FunctionTest(unittest.TestCase):
#     def test_greet(self):
#         """greet() have return 'Hello {name}! How are you?' if isEnemy == False"""
#         self.assertEqual(Testing.greet('Jack', False), 'Hello Jack! How are you?')
#
#     def test_greet_enemy(self):
#         """greet() have return 'Hello {name}! I will kill you, bastard!' if isEnemy == True"""
#         self.assertEqual(Testing.greet('Ivan', True), 'Hello Ivan! I will kill you, bastard!')
#
#     def test_greet_enemy_boolean(self):
#         with self.assertRaises(ValueError):
#             Testing.greet('Ivan', 'Bla-bla')
#
#     def test_eat_burgers(self):
#         """eat_burgers() have to return 'Mmm! That was excellent!' if burgers < 3 """
#         self.assertEqual(Testing.eat_burgers(2), 'Mmm! That was excellent!')
#
#     def test_eat_too_much_burgers(self):
#         """eat_burgers() have to return 'Oh! I overate! if burgers >= 3 """
#         self.assertEqual(Testing.eat_burgers(3), 'Oh! I overate!')
#
#     def test_can_fly_batman(self):
#         self.assertTrue(Testing.can_fly('Batman'), 'Batman have to be able to fly')
#
#     def test_can_fly_not_batman(self):
#         self.assertEqual(Testing.can_fly('Bob'), False)
#         self.assertEqual(Testing.can_fly('Jim'), False)
#         self.assertEqual(Testing.can_fly('Kevin'), False)
#         # self.assertFalse(Testing.can_fly('Kevin'), 'Anyone else have to not be able to fly')
#
#     def test_get_arsenal(self):
#         self.assertIn(Testing.get_arsenal(), ('knife', 'handgun', 'machine gun'))
#
#
# if __name__ == '__main__':
#     unittest.main()
#

# import unittest
# from Testing import Shooter
#
#
# class ShooterTest(unittest.TestCase):
#
#     moc_data = []
#
#     def setUp(self):
#         print(self.moc_data)
#         self.jake = Shooter('Jake')
#         self.moc_data = [1, 2, 3, 4, 5]
#
#     def tearDown(self):
#         print(self.moc_data)
#         self.moc_data = []
#
#     def test_get_cash(self):
#         # jake = Shooter('Jake')
#         self.jake.get_cash(500)
#         self.assertEqual(self.jake.money, 1500)
#         print(self.moc_data)
#
#     def test_greet(self):
#         # jake = Shooter('Jake')
#         self.assertEqual(self.jake.greet(), 'Hello! How are you?')
#         self.jake.money = 50
#         self.assertEqual(self.jake.greet(), 'Hello! I need cash!')
#         # print(self.moc_data)
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
