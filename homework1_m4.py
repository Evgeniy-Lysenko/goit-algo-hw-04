# calculation of the total amount of employees' salaries and its average value
path = input("Enter the path to the file with user and salary: ") # Enter the path to the file with user and salary

def total_salary(path): # calculation of the total amount of employees' salaries and its average value
    with open(path, "r", encoding='utf-8') as fh: # open the file in read mode in utf-8
        total = 0
        count = 0
        for line in fh: # read each line from the file
            name, salary = line.split(",") # split the line into name and salary
            total += int(salary)
            count += 1
            average = int(total / count)
        return total, average # return total and average salary

try: # try to calculate the total amount of employees' salaries and its average value
    total, average = total_salary(path)
except FileNotFoundError: # if the file is not found
    print(f"File not found: {path}")
except PermissionError: # if the file cannot be read
    print(f"Permission denied when reading file: {path}")
except IsADirectoryError: # if the path is a directory
    print(f"Path is a directory, expected a file: {path}")
except UnicodeDecodeError: # if the file cannot be decoded
    print(f"Cannot decode file (unexpected encoding): {path}")
except OSError as e: # if there is an error reading the file
    print(f"Error reading file {path}: {e}")
else:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
