# # # # # def print_greetings():
# # # # #     '''
# # # # #     only print 'Hello' on console
# # # # #     :return: None
# # # # #     '''
# # # # #     print('Hello')
# # # # # print_greetings()
# # # # # help(print_greetings)
# # # #
# # # # def print_greetings_with_name(name = 'Noname'):
# # # #     '''
# # # #     :param name - name on screen
# # # #     :argument def = Noname
# # # #     :return: None
# # # #     '''
# # # #     print(f'Hello {name}!')
# # # # jack = 'Jack'
# # # # print_greetings_with_name(jack)
# # # # print_greetings_with_name()
# # # # def sum_of_two_numbers(a = 0, b = 0):
# # # #     '''
# # # #
# # # #     :param a: first param
# # # #     :param b: second param
# # # #     :return: sum of a and b
# # # #     '''
# # # #     return print(a + b)
# # # # sum_of_two_numbers(1, 2)
# # #
# # #
# # # def is_hello_in_text(text):
# # #     return print('hello' in text.lower())
# # #
# # #
# # # is_hello_in_text('Hello everyone')
# # #
# # #
# # # def is_string_in_text(string, text):
# # #     print(string in text)
# # #
# # #
# # # is_string_in_text('he', 'the apple')
# # # is_string_in_text('he', 'in apple')
# #
# #
# # # def greeting_depends_on_gender(name, gender):
# # #     if gender == 'male':
# # #         print(f'Hello {name}! You are man!!!')
# # #         return
# # #     elif gender == 'female':
# # #         print(f'Hello {name}! You are girl')
# # #         return
# # #     else:
# # #         print(f'Hello {name}! What are fuck are you!!!!')
# # #         return
# # #
# # #
# # # name_input = input('What is you name?:  ')
# # # gender_input = input('your gender?:  ')
# # # greeting_depends_on_gender(name_input, gender_input)
# #
# #
# # def cat_voice():
# #     print('Meow!')
# #     return 'Meow!'
# #
# #
# # def dog_voice():
# #     print('Woof!')
# #     return 'Woof!'
# #
# #
# # print(cat_voice())
# # print(dog_voice())
# #
# #
# # def get_voice(voice):
# #     return f'{voice}!'
# #
# #
# # print(get_voice('dfd'))
# #
# #
# # def sequence_of_a_and_b(a, b):
# #     list =[]
# #     for num in range(a, b + 1):
# #         if num % 2 == 1:
# #             list.append(num)
# #     return list
# #
# #
# # print(sequence_of_a_and_b(1, 11))
# #
# #
# # def sequence_of_a_and_b(a, b):
# #     list2 =[num for num in range(a, b + 1)
# #             if num % 2 != 0]
# #     return list2
# #
# #
# # print(sequence_of_a_and_b(11, 21))
#
#
# x = 10
# y = 15
# z = 5
# w = 3
#
#
# def ten_percent(percent, *args):
#     print(args)
#     product = 1
#     for num in args:
#         product *= num
#     return print(int(product / percent))
#
#
# ten_percent(x, y, z, w)
#
# gender = 'male'
# age = 24
# name = 'Jack'
#
#
# def func_with_kwargs(**kwargs):
#     print(kwargs)
#     if 'name' in kwargs:
#         print(f'Hello! {kwargs["name"]}')
#     else:
#         print('Hello! What is your name?')
#
#
# func_with_kwargs(gender ='male', age=24, name='Jack')
# func_with_kwargs(gender='male', age=24, names='Jack')
# jack = {'gender': 'male',
#         'age': 24,
#         'names': 'Jack'}
#
# jacky = {'gender': 'male',
#          'age': 27,
#          'names': 'Jacky'}
#
# func_with_kwargs(jack, jacky)


# def is_cat_here(item, *args):
#     if item in args:
#         return True
#     else:
#         return False
#
#
# def your_favorite_color(my_color, **kwargs):
#     if 'color' in kwargs:
#         print(f'May favorite color is {my_color}, but {kwargs["color"]}, is also pretty good!')
#     else:
#         print(f'My favorite color if {my_color}, what is your favorite color?')
#
#
# your_favorite_color('blue', gender='male', age=24, colors='red')


def sum_of_two_numbers(x, y):
    print(x + y)
    return x + y


number_list = [1, 2, 3, 4, 5, 6, 7]

list(map(sum_of_two_numbers, number_list))

