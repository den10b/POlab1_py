import os
import json
import xml.etree.ElementTree as ET
import zipfile
import psutil


def get_logical_drives():
    drives = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        drives.append({
            'Диск': partition.device,
            'Общий размер': usage.total,
            'Свободное место': usage.free,
            'Тип файловой системы': partition.fstype,
        })
    return drives


def create_text_file(filename):
    with open(filename, 'w') as file:
        print(f"Создан текстовый файл: {filename}")


def write_text_to_file(filename):
    text = input("Введите текст для записи в файл: ")
    with open(filename, 'a') as file:
        file.write(text + '\n')
    print("Текст успешно записан в файл.")


def read_text_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(f"Содержимое файла {filename}:\n{data}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"Файл {filename} успешно удален.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")


def create_json_file(filename):
    data = {
        'Name': 'Example',
        'Value': 42
    }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Создан JSON файл: {filename}")


def write_json_to_file(filename):
    data = {
        'Name': input("Введите имя: "),
        'Value': int(input("Введите значение: "))
    }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Данные успешно записаны в JSON файл.")


def read_json_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Данные из JSON файла {filename}:\n{data}")
    except FileNotFoundError:
        print(f"Файл {filename} не найден или не содержит данных JSON.")


def create_xml_file(filename):
    xml_data = '''<XMLData>
    <Name>Example</Name>
    <Value>42</Value>
</XMLData>
'''
    with open(filename, 'w') as file:
        file.write(xml_data)
    print(f"Создан XML файл: {filename}")


def write_xml_to_file(filename):
    data = {
        'Name': input("Введите имя: "),
        'Value': input("Введите значение: ")
    }
    root = ET.Element("XMLData")
    name_element = ET.SubElement(root, "Name")
    value_element = ET.SubElement(root, "Value")
    name_element.text = data['Name']
    value_element.text = data['Value']
    tree = ET.ElementTree(root)
    tree.write(filename)
    print("Данные успешно записаны в XML файл.")


def read_xml_from_file(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {
            'Name': root.find('Name').text,
            'Value': root.find('Value').text
        }
        print(f"Данные из XML файла {filename}:\n{data}")
    except (FileNotFoundError, ET.ParseError):
        print(f"Файл {filename} не найден или не содержит данных XML.")


def create_zip_archive(zip_filename, filename_to_add):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(filename_to_add, os.path.basename(filename_to_add))
    print(f"Создан ZIP архив: {zip_filename}")


def unzip_file(zip_filename):
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extractall()
    print(f"Разархивирован файл {zip_filename}")


def delete_zip_archive(zip_filename):
    try:
        os.remove(zip_filename)
        print(f"ZIP архив {zip_filename} успешно удален.")
    except FileNotFoundError:
        print(f"ZIP архив {zip_filename} не найден.")


if __name__ == "__main__":
    print("Информация о логических дисках:")
    drives = get_logical_drives()
    for drive in drives:
        print(f"Диск: {drive['Диск']}, "
              f"Общий размер: {drive['Общий размер'] / (2 ** 20):0.2f} МБ, "
              f"Свободное место: {drive['Свободное место'] / (2 ** 20):0.2f} МБ, "
              f"Тип ФС: {drive['Тип файловой системы']}")

    text_filename = "textfile.txt"
    print("\nРабота с текстовым файлом:")
    create_text_file(text_filename)
    write_text_to_file(text_filename)
    read_text_from_file(text_filename)
    # delete_file(text_filename)

    json_filename = "data.json"
    print("\nРабота с JSON файлом:")
    create_json_file(json_filename)
    write_json_to_file(json_filename)
    read_json_from_file(json_filename)
    # delete_file(json_filename)

    xml_filename = "data.xml"
    print("\nРабота с XML файлом:")
    create_xml_file(xml_filename)
    write_xml_to_file(xml_filename)
    read_xml_from_file(xml_filename)
    # delete_file(xml_filename)

    zip_filename = "archive.zip"
    file_to_add_to_zip = "to_zip.txt"
    print("\nСоздание архива ZIP:")
    create_zip_archive(zip_filename, file_to_add_to_zip)
    unzip_file(zip_filename)
    # delete_zip_archive(zip_filename)
    # delete_file(file_to_add_to_zip)
