from pprint import pprint
string = ["Этот текст является тестом.",
"Text for tell*",
"Используется кодировка utf-8.",
"It is file for writing"]
number = len(string) - 1
bayron_1 ="seyver.txt"
file_name = open(bayron_1,'r+', encoding='utf-8')
i = 0
strings_positions = {}
def custom_write(file_name,string):
    i = 0
    while i <= number:
        n = i
        string_n = str(string[n])
        key = (file_name.tell())
        file_name.write(string_n + '\n')
        strings_positions[n, key]= (string_n)
        i += 1
    else:
        return strings_positions

custom_write(file_name,string)
pprint(strings_positions)
file_name.close()


