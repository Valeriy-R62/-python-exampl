import time
import os

directory = r'C:\Users\Professional\pythonProject4\module_5'
print("Текущая директория: ", os.getcwd())
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join('module_5')
        filetime = os.path.getmtime('module_5')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize('module_5')
        parent_dir = os.path.dirname('module_5')
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,')
        print(f' Время изменения:{formatted_time}, Родительская директория: {parent_dir}')
