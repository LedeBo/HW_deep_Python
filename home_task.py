import os
from os import path, walk, getcwd
import logging
import argparse
from collections import namedtuple


HW_15 = path.dirname(path.realpath(__file__))+'\\hw\\test.txt'

FORMAT = '{levelname:<4}: {msg}'

logging.basicConfig(format=FORMAT, style='{', filename=HW_15,
                    filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


FileType = namedtuple(
    'FileType', ['name', 'extension', 'catalogue_flag', 'main_catalogue'])


def catalogue_way():
    parser = argparse.ArgumentParser(prog="Работа с каталогом")
    parser.add_argument('-p', metavar='Путь к каталогу', type=str, nargs=1,
                        help='Необходимо ввести абсолютный или относительный путь к каталогу', default=[getcwd()])
    args = parser.parse_args()
    return find_way(args.p[0])


def find_way(fold):
    catalogue = path.abspath(fold)
    if path.isdir(catalogue):
        return catalogue_extract(catalogue)
    elif path.isfile(catalogue):
        logger.warning(f'По адресу: {catalogue} расположен файл!')
        return f'По адресу: {catalogue} расположен файл!'
    elif path.exists(catalogue) == False:
        logger.error(f'Каталога: {catalogue} не найдено!')
        return f'Каталога: {catalogue} не найдено!'


def catalogue_extract(catalogue):
    list_of_files = []
    for i, params in enumerate(walk(catalogue), start=1):
        path_catalogue, catalogues, files = params
        for j, item in enumerate(catalogues + files, start=1):
            abs_path = path.join(path_catalogue, item)
            if path.isfile(abs_path):
                name = ".".join(item.split(".")[:-1])
                extension = item.split(".")[-1]
                catalogue_flag = False
            elif path.isdir(abs_path):
                name = item
                extension = "is_catalogue"
                catalogue_flag = True
            main_catalogue = abs_path.split('\\')[-2]
            timing = FileType(name, extension, catalogue_flag, main_catalogue)
            if timing.catalogue_flag:
                logger.info(f'{i}.{j} - Каталог: {timing.name} ' +
                            f'| Флаг каталога: {timing.catalogue_flag} ' +
                            f'| Главный каталог: {main_catalogue}')
            else:
                logger.info(f'{i}.{j} - Файл: {timing.name} ' +
                            f'| Расширение: {timing.extension} ' +
                            f'| Главный каталог: {main_catalogue}')
            list_of_files.append(timing)
    return list_of_files


if __name__ == "__main__":
    print(catalogue_way())