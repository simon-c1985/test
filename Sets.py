rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}

print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56]
text_tuple = ('asfas', 'asfasqe', 'qweqw')
set_from_tuple = set(text_tuple)
set_from_list = set(number_list)
print(set_from_list, set_from_tuple)
set_from_list.add(777)
set_from_tuple.add(999)
print(set_from_list, set_from_tuple)
list_from_tuple = list(set_from_list)
print(list_from_tuple)

x = set_from_list.pop()
print(set_from_list, x)

set_from_list.remove(777)
set_from_list.discard(43)
set_from_list.discard(432)

print(set_from_list)

# Exercise

print('///////////////////Exercise///////////////////')

letters_set = set('Создайте множество при помощи функции set()'
                  ' из текста, чтобы получить уникальные символы, '
                  'содержащиеся в тексте.')
print(letters_set)
print(type(letters_set))