some_list = [12, 35.334, 'hello']
print(some_list)
print(len(some_list))
print(some_list[1])
another_some_list = some_list[:2]
print(another_some_list)
some_list[2] = 'hello'
print(some_list)
new_list = some_list + another_some_list
print(some_list)

# Adding items

new_list.append('new item')
new_list.insert(0, 'start')
new_list.insert(2, 13)
print(new_list)

# Removing items

# new_list.pop(-4)
# print(new_list)
deleted_item = new_list.pop(-4)
new_list.remove('start')
print(deleted_item)
print(new_list)

number_list = [45, 12, 3, -455, 22]
letter_list = ['s', 'w', 't', 'a']

number_list.sort()
letter_list.sort()

print(number_list)
print(letter_list)



