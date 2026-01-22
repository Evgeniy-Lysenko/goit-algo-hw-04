# calculation of the total amount of employees' salaries and its average value
path = input("Enter the path to the file with user and salary: ") # Enter the path to the file with user and salary

def total_salary(path): # calculation of the total amount of employees' salaries and its average value
    with open(path, "r", encoding='utf-8') as fh: # open the file in read mode in utf-8
        total = 0
        count = 0
        for line in fh: # read each line from the file
            name, salary = line.strip().split(",") # split the line into name and salary
            total += float(salary) # add the salary to the total
            count += 1
        if count == 0:
           return 0, 0
        average = total // count 
        return total, average # return total and average salary

try: # try to calculate the total amount of employees' salaries and its average value
   total, average = total_salary(path)
except UnicodeDecodeError: # if the file cannot be decoded
    print(f"Файл не в форматі UTF-8: {path}")
except OSError as e: # if there is an error reading the file
    print(f"Помилка читання файлу {path}: {e}")
except ValueError: # if the salary is not a number
    print(f"Файл не відповідає шаблону \"ім'я, заробітна плата\": {path}")
else:
     if total == 0:
        print("Файл не містить інфіормацію про заробітну плату")
     else:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
