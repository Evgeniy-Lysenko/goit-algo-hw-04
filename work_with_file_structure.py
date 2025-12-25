# from pathlib import PurePath

# p = PurePath("/home/lysenkoe/Desktop/python_start/first/goit-algo-hw-04/goit-algo-hw-04/cat_info.txt")
# print("Name:", p.name)  
# print("Suffix:", p.suffix) 
# print("Parent:", p.parent)

# from pathlib import Path

# p = Path("test.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 


# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()
# print(absolute_path)


# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()

# current_working_directory = Path("/home/lysenkoe/Desktop/python_start/first/goit-algo-hw-04/goit-algo-hw-04")
# relative_path = absolute_path.relative_to(current_working_directory)
# print(relative_path)


# from pathlib import Path

# # Початковий шлях до файлу
# original_path = Path("documents/example.txt")

# # Зміна імені файлу
# new_path = original_path.with_name("report.txt")
# print(new_path)

# from pathlib import Path

# # Початковий шлях до файлу
# original_path = Path("documents/example.txt")

# # Зміна імені файлу
# new_path = original_path.with_suffix(".md")
# print(new_path)


# from pathlib import Path

# original_path = Path("documents/example.txt")

# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report.txt")

# print(original_path)
# print(new_path)


# from pathlib import Path

# original_path = Path("/home/lysenkoe/Desktop/python_start/first/test/test.py")

# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report2.py")
# original_path.rename(new_path)

# print(original_path)
# print(new_path)


# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Запис тексту у файл
# file_path.write_text("Привіт світ!", encoding="utf-8")

# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Читання тексту з файлу
# text = file_path.read_text(encoding="utf-8")
# print(text)



# from pathlib import Path

# # Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# # Бінарні дані для запису
# data = b"Python is great!"

# # Запис байтів у файл
# file_path.write_bytes(data)


# from pathlib import Path

# # Створення об'єкту Path для бінарного файлу
# file_path = Path("example.bin")

# # Читання байтів з файлу
# binary_data = file_path.read_bytes()
# print(binary_data)



# from pathlib import Path

# # Створення об'єкту Path для директорії
# directory = Path("./test")

# # Виведення переліку всіх файлів та піддиректорій
# for path in directory.iterdir():
#     print(path)


# from pathlib import Path
# directory = Path('./my_directory/new_folder')
# directory.mkdir(mode=0o777, parents=True, exist_ok=True)


from pathlib import Path

path = Path("./test/test.txt")

# Перевірка існування
if path.exists():
    print(f"{path} існує")

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією")

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")
