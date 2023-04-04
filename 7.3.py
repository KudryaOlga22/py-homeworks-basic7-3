import os


# Создание функцию для работы с заданными файлами
def create_file_list(folder):
    file_list = os.listdir(folder)  # Получение списка имен файлов в папке
    union_file_list = []  # Создание списка для хранения содержимого файлов
    for file in file_list:
        with open(folder + "/" + file) as _temp_file:  # Поочередно считываем файлы
            # Добавление в список название файла, значение для числа строк и список для содержимого файла
            union_file_list.append([file, 0, []])
            for line in _temp_file:
                union_file_list[-1][2].append(line.strip())  # Добавляем в список содержимое файла построчно
                union_file_list[-1][1] += 1  # Увеличениезначение для числа строк
    # Возвращение предварительно отсортированный по значению числа строк список с содержимым файлов
    return sorted(union_file_list, key=lambda x: x[1], reverse=False)


# Создадание функции для записи итогового файла
def create_merget_file(folder, filename, union_file=None):
    with open(filename + '.txt', 'w+') as union_file:  # Создадание итогового файла с именем "filename".txt
        union_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            union_file.write(f'Назввание файла: {file[0]}\n')  # Записываем в итоговый файл имена начальных файлов
            union_file.write(f'Количество строк: {file[1]}\n')  # Записываем в итоговый файл число строк файлов
            for string in file[2]:
                union_file.write(string + '\n')  # Записываем в итоговый файл содержимое начальных файлов построчно
            union_file.write('\n')
    return print('Файл создан')


def create_union_file(param, param1):
    pass


create_union_file('txt', 'union_file')