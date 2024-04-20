def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, 'строка', True)

print_params(1, "строка")

print_params()

print_params(b=25)

print_params(c=[1, 2, 3])
print_params(a=1, b='строка', c=True)
print_params()

value_list = (2, 'буква', False)
print_params(*value_list)
value_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**value_dict)
value_list_2 = (5, 'строчка')
print_params(*value_list_2, 42)
