
path = input("Enter the path to the file with cats inormation: ") 

def get_cats_info(path):
    cat_list = []
    with open(path, "r", encoding='utf-8') as fh:
        for line in fh:
            id, name, age = line.strip().split(",")
            cat_dict = {"id": id, "name": name, "age": age}
            cat_list.append(cat_dict)
    return cat_list
try:
    cats_info = get_cats_info(path)

except FileNotFoundError:
    print(f"File not found: {path}")
except PermissionError:
    print(f"Permission denied when reading file: {path}")
except IsADirectoryError:
    print(f"Path is a directory, expected a file: {path}")
except UnicodeDecodeError:
    print(f"Cannot decode file (unexpected encoding): {path}")
except OSError as e:
    print(f"Error reading file {path}: {e}")
else:
    print(cats_info)
    