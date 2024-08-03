import io
from pprint import pprint

my_soul = "проба.txt"
my_soul_F = open('проба.txt')
name = str(my_soul_F.read())
file = open('Байрон.txt', 'w', encoding = 'utf-8')
file.write(name)
my_soul_F.close()
file.close()
file = 'Байрон.txt'
with open(file,) as file_1:
    for line in file_1:
        print(line, end="")