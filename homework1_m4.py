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
        average = total / count
        return total, average


total, average = total_salary(path) # call the function 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # print the total amount of employees' salaries and its average value