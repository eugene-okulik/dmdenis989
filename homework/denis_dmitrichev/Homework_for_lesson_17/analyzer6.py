import argparse
import os
from datetime import datetime


def extract_datetime_from_line(line):
    """
    Извлекает дату из строки лога
    :param line: строка файла
    :return: возвращает дату в указанном формате, если распарсить не получилось, то возвращает None
    """
    try:
        dt = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S.%f')
        return dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    except (ValueError, IndexError):
        return None


def read_log_files(path):
    """
    Читает все файлы логов и группирует по дате
    :param path: путь до указанного объекта, может быть файлом или папкой с файлами
    :return: словарь, ключ - дата, значения кортеж контент, имя файла, номер строки
    """
    logs_dict = {}

    if os.path.isfile(path):
        filename = os.path.basename(path)
        with open(path, 'r', encoding='UTF-8') as data_file:
            for line_num, line in enumerate(data_file, 1):
                line_content = line.strip()
                datetime_key = extract_datetime_from_line(line_content)
                if datetime_key:
                    if datetime_key not in logs_dict:
                        logs_dict[datetime_key] = []
                    logs_dict[datetime_key].append((line_content, filename, line_num))

    elif os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='UTF-8') as data_file:
                    for line_num, line in enumerate(data_file, 1):
                        line_content = line.strip()
                        datetime_key = extract_datetime_from_line(line_content)
                        if datetime_key:
                            if datetime_key not in logs_dict:
                                logs_dict[datetime_key] = []
                            logs_dict[datetime_key].append((line_content, filename, line_num))
    return logs_dict


def find_text_in_logs(logs_dict, search_text):
    """
    Ищет текст в логах и выводит результаты
    :param logs_dict: словарь
    :param search_text: Текст для поиска в файлах
    """
    found_count = 0

    for date, log_entries in logs_dict.items():
        for line_content, filename, line_num in log_entries:
            if search_text in line_content:
                found_count += 1

                words = line_content.split()
                word_index = None

                for idx, word in enumerate(words):
                    if search_text in word:
                        word_index = idx
                        break

                if word_index is not None:
                    start_index = max(0, word_index - 5)
                    end_index = min(len(words), word_index + 6)
                    context = ' '.join(words[start_index:end_index])

                    print(f"Найдено в файле: {filename}")
                    print(f"Строка: {line_num}")
                    print(f"Дата: {date}")
                    print(f"Текст: {context}")
                    print("-" * 80)

    if found_count == 0:
        print(f"Текст '{search_text}' не найден.")
    else:
        print(f"Всего найдено совпадений: {found_count}")

    return found_count


def main():
    parser = argparse.ArgumentParser(description='Поиск текста в логах')
    parser.add_argument("path", help="Путь до файла или папки с логами")
    parser.add_argument("--text", required=True, help="Текст для поиска в файлах")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Ошибка: путь '{args.path}' не существует.")
        return

    logs_dict = read_log_files(args.path)

    if not logs_dict:
        print("Не найдено файлов для обработки.")
        return

    find_text_in_logs(logs_dict, args.text)


main()
