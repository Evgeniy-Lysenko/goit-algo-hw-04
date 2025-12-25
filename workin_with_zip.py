import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='/home/lysenkoe/Desktop/python_start/first/test')

# import shutil

# # Створення TAR.GZ-архіву
# shutil.make_archive('example', 'gztar', root_dir='/home/lysenkoe/Desktop/python_start/first/test')

import shutil

# Розпакування ZIP-архіву в певну директорію
shutil.unpack_archive('example.zip', '/home/lysenkoe/Desktop/python_start/first/test/1')
