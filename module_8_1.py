def add_everything_up(a, b):
    try:
        rez = a + b
        return (rez)
    except TypeError:
        return (str(a) +  str(b))
print(add_everything_up(3.14, 6))
print(add_everything_up('Pi', 3.14))
print(add_everything_up(16, 'Лет'))
