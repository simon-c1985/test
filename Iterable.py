# # # # # # # # number_list = [1, 2, 3, 4, 5]
# # # # # # # #
# # # # # # # # # for number in number_list:
# # # # # # # # #     print(number)
# # # # # # # # #
# # # # # # # # # for letter in 'my sting':
# # # # # # # # #     print(letter)
# # # # # # # #
# # # # # # # # number_list_iterator = iter(number_list)
# # # # # # # # # print(type(number_list_iterator))
# # # # # # # #
# # # # # # # # string_iterator = iter("my string")
# # # # # # # # # print(type(number_list_iterator))
# # # # # # # #
# # # # # # # # # print(number_list_iterator.__next__())
# # # # # # # # # print(number_list_iterator.__next__())
# # # # # # # # # print(number_list_iterator.__next__())
# # # # # # # # # print(number_list_iterator.__next__())
# # # # # # # # # print(number_list_iterator.__next__())
# # # # # # # # # print(number_list_iterator.__next__())
# # # # # # # # # print(number_list_iterator.__next__())
# # # # # # # #
# # # # # # # # # print(string_iterator.__next__())
# # # # # # # # # print(string_iterator.__next__())
# # # # # # # # # print(string_iterator.__next__())
# # # # # # # # # print(string_iterator.__next__())
# # # # # # # #
# # # # # # # # print(next(number_list_iterator))
# # # # # # #
# # # # # # #
# # # # # # # def my_for_loop(iterable):
# # # # # # #     iterator = iter(iterable)
# # # # # # #     while True:
# # # # # # #         try:
# # # # # # #             print(iterator.__next__())
# # # # # # #         except StopIteration:
# # # # # # #             print('Iteration is finish')
# # # # # # #             break
# # # # # # #
# # # # # # #
# # # # # # # my_for_loop('hello')
# # # # # # # my_for_loop([1, 2, 3, 4])
# # # # # #
# # # # # #
# # # # # # # for number in range(1, 10):
# # # # # # #     print(number)
# # # # # #
# # # # # #
# # # # # # class MyRange:
# # # # # #     def __init__(self, start, end):
# # # # # #         self.start = start
# # # # # #         self.end = end
# # # # # #         self.current = start
# # # # # #
# # # # # #     def __iter__(self):
# # # # # #         return self
# # # # # #
# # # # # #     def __next__(self):
# # # # # #         if self.current < self.end:
# # # # # #             number = self.current
# # # # # #             self.current += 1
# # # # # #             return number
# # # # # #         raise StopIteration
# # # # # #
# # # # # #
# # # # # # first_range = MyRange(20, 30)
# # # # # # for num in first_range:
# # # # # #     print(num)
# # # # #
# # # # #
# # # # # def my_function(x):
# # # # #     return x
# # # # #
# # # # #
# # # # # print(my_function(4))
# # # #
# # # # #
# # # # # def count_up_to(x):
# # # # #     count = 1
# # # # #     while count <= x:
# # # # #         yield count
# # # # #         count += 1
# # # # #
# # # # #
# # # # # # print(count_up_to(4))
# # # # # # counter = count_up_to(4)
# # # # # # print (counter.__next__())
# # # # # # print (counter.__next__())
# # # # # # print (counter.__next__())
# # # # # # print (counter.__next__())
# # # # # # print (counter.__next__())
# # # # # # print(next(counter))
# # # # # # print(next(counter))
# # # # # # print(next(counter))
# # # # # # print(next(counter))
# # # # # # print(next(counter))
# # # # #
# # # # # counter = count_up_to(10)
# # # # #
# # # # # for number in counter:
# # # # #     print(number)
# # # #
# # # #
# # # # def get_week_day():
# # # #     week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# # # #     count = 0
# # # #     for day in week:
# # # #         yield day
# # # #
# # # #
# # # # current_day = get_week_day()
# # # #
# # # # for day in current_day:
# # # #     print(day)
# # #
# # #
# # # # def create_patterns():
# # # #     max_patterns_number = 100
# # # #     patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
# # # #     i = 0
# # # #     result_list = []
# # # #     while len(result_list) < max_patterns_number:
# # # #         if i >= len(patterns):
# # # #             i = 0
# # # #         result_list.append(patterns[i])
# # # #         i += 1
# # # #     return result_list
# # # #
# # # #
# # # # print(create_patterns())
# # #
# # #
# # # def get_current_pattern():
# # #     patterns = ('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
# # #     i = 0
# # #     while True:
# # #         if i >= len(patterns):
# # #             i = 0
# # #         yield patterns[i]
# # #         i += 1
# # #
# # #
# # # current_pattern = get_current_pattern()
# # #
# # #
# # # def print_pattern(x):
# # #     str =''
# # #     while x > 0:
# # #         str += f' {current_pattern.__next__()}'
# # #         print(str)
# # #         x -= 1
# # #
# # #
# # # print_pattern(10)
# # #
# # #
# #
# #
# # def even_odd():
# #     value = 'even'
# #     while True:
# #         if value == 'even':
# #             value = 'odd'
# #         else:
# #             value = 'even'
# #         yield value
# #
# #
# # evenOdd = even_odd()
# # print(next(evenOdd))
#
#
# def get_number_from_range():
#     for number in range(10):
#         yield number
#
#
# counter = get_number_from_range()
# # print(next(counter))
#
# counter1 = (number for number in range())
# # print(counter1)
# # print(next(counter1))

#
# # print([number for number in range(10)])
# print(counter)
# print(counter1)


def get_infinite_square_generator():
    num = 1
    while True:
        yield num ** 2
        num += 1


infinite_sqare_generator = get_infinite_square_generator()


def print_pow(x):
    while x > 0:
        print(next(infinite_sqare_generator))
        x -= 1


print_pow(11)