# list of dictionaries with cats information from file
path = input("Enter the path to the file with cats inormation: ") 

def get_cats_info(path):
    cat_list = [] # epty list
    with open(path, "r", encoding='utf-8') as fh:
        for line in fh:
            id, name, age = line.strip().split(",") # split the line into id, name and age
            cat_dict = {"id": id, "name": name, "age": age} # create dictionary
            cat_list.append(cat_dict) # add dictionary to list
    return cat_list
try:
    cats_info = get_cats_info(path)

except UnicodeDecodeError: # if the file cannot be decoded
    print(f"Файл не в форматі UTF-8: {path}")
except ValueError: # if the salary is not a number
    print(f"Файл не відповідає шаблону \"ID, ім'я, вік\": {path}")
except OSError as e: # if there is an error reading the file
    print(f"Error reading file {path}: {e}")
else:
    print(cats_info)
    