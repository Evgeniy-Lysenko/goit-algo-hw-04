# working with file
# import os

# path = '/home/lysenkoe/Desktop/python_start/first/goit-algo-hw-04/working_with_file.py'
# print(os.path.exists(path))

# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# all_file = fh.read()
# print(all_file)  # 'hello!'

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1) # читаємо один символ
#     if len(symbol) == 0: # якщо символу немає
#         break
#     print(symbol)

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)

# fh.close()


# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# lines = fh.readlines()
# print(lines)

# fh.close()


# fh = open("test.txt", "w")
# fh.write("first line\nsecond line\nthird line")
# fh.close()

# fh = open("test.txt", "r")
# lines = [el.strip() for el in fh.readlines()]
# print(lines)

# fh.close()

# fh = open("test.txt", "w+")
# fh.write("hello!")

# position = fh.tell()

# print("end str", position)  # 6
# print(fh.read(1))   

# fh.seek(1)
# position = fh.tell()
# print(position)  # 1
# print(fh.read(1)) 


# position = fh.tell()
# print(position) 
# print(fh.read(1)) # 3
# position = fh.tell()
# print(position) 
# print(fh.read())

# fh.close()


# fh = open('text.txt', 'w')
# try:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# finally:
#     # Закриття файлу в блоці finally гарантує, що файл закриється навіть у разі помилки
#     fh.close()


# with open('text.txt', 'w') as fh:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# # Файл автоматично закриється після виходу з блоку with

# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)

# s = b'Hello!'
# print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

# s = 'Hello!' 
# print(s[1])  # Виведе: 'e'


# byte_str = 'some text'.encode()
# print(byte_str) #

# byte_str = b'some text'=
# print(byte_str.decode())


# # Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел

# # Перетворення байт-рядка у список чисел
# numbers = list(byte_numbers)
# print(numbers)

# for num in [127, 255, 156]:
#   print(hex(num))



# s = "Привіт!"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)

# s_from_cp1251 = cp1251.decode("cp1251")
# print(s_from_cp1251 == s)

# s_from_utf8 = utf8.decode("utf-8")
# print(s_from_utf8 == s)

# print(b'Hello world!'.decode('utf-16'))

# print(b'Hello world!'.decode('cp1251'))

# print(b'Hello world!'.decode('utf-8'))  


# Відкриття текстового файлу з явними вказівками UTF-8 кодування
# with open('User_salary.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# byte_array = bytearray(b'Kill Bill')
# print(byte_array)

# byte_array[0] = ord('B')
# byte_array[5] = ord('K')
# print(byte_array[0:5])
# print(byte_array)
# print(list(byte_array))
# print(byte_array.decode())
# byte_array_dic = {}
# for i in range(len(byte_array)):
#     byte_array_dic[i] = byte_array[i]
# print(byte_array_dic)

# byte_array_dic2 = {}
# byte_array_decode = byte_array.decode()
# for i in range(len(byte_array_decode)):
#     byte_array_dic2[i] = byte_array_decode[i]
# print(byte_array_dic2)


# combined_dict = {v: k for k, v in byte_array_dic.items()}
# print(combined_dict)

# combined_dict2 = {v: k for k, v in byte_array_dic2.items()}
# print(combined_dict2)

# final_dict = {str(combined_dict.get(k, None)): v for k, v in combined_dict2.items()}
# print(final_dict)

# byte_array = bytearray(b"Hello")
# byte_array.append(ord("!"))  
# print(byte_array)

# byte_array = bytearray(b"Hello World")
# string = byte_array.decode("utf-8")
# print(string)  # Виведе: 'Hello World'


# string1 = "Hello World"
# string2 = "hello world"
# if string1.lower() == string2.lower():
#     print("Рядки однакові")
# else:
#     print("Рядки різні")


# text = "Python Programming"
# print(text.casefold())

german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")
print(f"Порівняння з casefold(): {casefold_comparison}")
