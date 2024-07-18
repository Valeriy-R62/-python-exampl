from pprint import pprint


name = 'проба.txt'
file = open(name, 'r')
pprint(file.read())
file.close()