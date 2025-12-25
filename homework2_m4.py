
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
    print(cats_info)
except FileNotFoundError:
    print("File not found")