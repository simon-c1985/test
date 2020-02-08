# # # # # # raise ValueError('Invalid value')
# # # # # # raise ValueError()
# # # # #
# # # # #
# # # # # def colorize_text(color_number, text):
# # # # #     """
# # # # #
# # # # #     :param color_number: Parameter color_number must be integer type and
# # # # #     must be in range of integer form 1 to 7
# # # # #     :param text: Parameter text must be string type
# # # # #     :return:
# # # # #     """
# # # # #     color_number_list = [1, 2, 3, 4, 5, 6, 7]
# # # # #     if type(color_number) is not int:
# # # # #         raise TypeError('Parameter color_number must be integer type')
# # # # #
# # # # #     if color_number not in color_number_list:
# # # # #         raise ValueError('Parameter color_number must be in range of integer form 1 to 7')
# # # # #
# # # # #     if type(text) is not str:
# # # # #         raise TypeError('Parameter text must be string type')
# # # # #
# # # # #     if color_number == 1:
# # # # #         print(f'red {text}')
# # # # #     elif color_number == 2:
# # # # #         print(f'orange {text}')
# # # # #     elif color_number == 3:
# # # # #         print(f'yellow {text}')
# # # # #     elif color_number == 4:
# # # # #         print(f'green {text}')
# # # # #     elif color_number == 5:
# # # # #         print(f'blue {text}')
# # # # #     elif color_number == 6:
# # # # #         print(f'indigo {text}')
# # # # #     elif color_number == 7:
# # # # #         print(f'violet {text}')
# # # # #
# # # # #
# # # # # # color = get_rainbow_color(0)
# # # # # # print(color)
# # # # # # help(get_rainbow_color)
# # # # #
# # # # # colorize_text(4, 4)
# # # #
# # # # print('Some code')
# # # # # print((len(23)))
# # # # try:
# # # #     # print((len(23)))
# # # #     print(my_variable)
# # # # except NameError:
# # # #     print('NameError has happen')
# # # # except TypeError:
# # # #     print('TypeError has happen')
# # # # print('Code after error')
# # #
# # # user_dictionary = {'first_name': 'Jack', 'last_name': 'Daniels', 'age': 24}
# # #
# # # # print(user_dictionary['last_name'])
# # # # print(user_dictionary['name'])
# # #
# # # # print(user_dictionary.get('last_name'))
# # # # print(user_dictionary.get('name'))
# # #
# # #
# # # def get_dictionary_value(dictionary, key):
# # #     """
# # #     If dictionary haven't specified key, the function return 'Nope'
# # #     :param dictionary:
# # #     :param key:
# # #     :return:
# # #     """
# # #     try:
# # #         return dictionary[key]
# # #     except KeyError:
# # #         return 'Nope'
# # #
# # #
# # # print(get_dictionary_value(user_dictionary, 'age'))
# # # print(get_dictionary_value(user_dictionary, 'a'))
# # # print(get_dictionary_value(user_dictionary, 'first_name'))
# #
# # # number = input('Enter some number \n')
# # while True:
# #     try:
# #         number = int(input('Enter some number \n'))
# #         print(number / 2)
# #     except:
# #         print('You have to enter a number')
# #     else:
# #         print('Good! This is number!')
# #         break
# #     finally:
# #         print('Finally block')
# #
# # print('Code after error handling')
#
#
# def divide(x, y):
#     try:
#         print(x / y)
#     except ZeroDivisionError:
#         print('You can\'t divide by zero!')
#     except TypeError:
#         print('x and y must be numbers')
#     finally:
#         print('x has divided by y')
#
#
# # print(divide(4, 2))
# divide(4, '3')
