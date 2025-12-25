# calculation of the total amount of employees' salaries and its average value
path = input("Enter the path to the file with user and salary: ") # Enter the path to the file with user and salary

def total_salary(path): # calculation of the total amount of employees' salaries and its average value
    with open(path, "r", encoding='utf-8') as fh: # open the file in read mode in utf-8
        total = 0
        count = 0
        for line in fh:
            name, salary = line.split(",") # split the line into name and salary
            total += int(salary)
            count += 1
            average = int(total / count)
        return total, average

try:
    total, average = total_salary(path)
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
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
