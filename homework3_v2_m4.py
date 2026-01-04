# struktura direktorii
import sys
from pathlib import Path
from colorama import init,  Fore, Style
init(strip=False, convert=False)

def path_recursion(path: Path, level=1): # recursive directory traversal
    indent = " " * (level * 4)
    for p in  sorted(path.iterdir()):
        if p.is_dir():
            print(f"{indent}{Fore.LIGHTBLUE_EX}{p.name}/{Style.RESET_ALL}") # print directory name in blue
            path_recursion(p, level + 1)
        else:
            print(f"{indent}{Fore.LIGHTGREEN_EX}{p.name}{Style.RESET_ALL}")  # print file name in green

def main(): # main function to handle input and exceptions
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії черерез аргумент командного рядка")
        return

    path = Path(sys.argv[1]) # get path from command line argument

    if not path.exists(): # check if path exists
        print("Директорія не знайдена")
        return

    if not path.is_dir(): # check if path is a directory
        print("Шлях не є директорією")
        return
    print(f"{Fore.RED}{path}/")
    path_recursion(path)

if __name__ == "__main__":
    main()
