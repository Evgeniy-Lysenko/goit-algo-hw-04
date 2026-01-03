# struktura direktorii
import sys
from pathlib import Path
from colorama import Fore, Style

def path_recursion(path: Path, level=0): # recursive directory traversal
    indent = " " * (level * 4)
    for p in path.iterdir():
        if p.is_dir():
            print(f"{indent}{Fore.LIGHTBLUE_EX}{p.name}/{Style.RESET_ALL}") # print directory name in blue
            path_recursion(p, level + 1)
        else:
            print(f"{indent}{Fore.LIGHTGREEN_EX}{p.name}{Style.RESET_ALL}")  # print file name in green

# def main(): #non-recursive directory traversal
#     print(f"Вміст директорії {Fore.LIGHTBLUE_EX}{path}/{Style.RESET_ALL}")    
#     for p in path.iterdir():
#         if p.is_dir():
#             print(f"{Fore.LIGHTBLUE_EX}{p.name}{Style.RESET_ALL}")
#         else:
#             print(f"{Fore.LIGHTGREEN_EX}{p.name}{Style.RESET_ALL}")


path = Path(sys.argv[1])
try:    
    # existence check
    if path.exists():
       print(f"{path} існує")

    # derictory check
    if path.is_dir():
       print(f"{path} є директорією")
    # main()
    print(f"Вміст директорії {Fore.LIGHTBLUE_EX}{path}/{Style.RESET_ALL}")    
    path_recursion(path)
except NotADirectoryError: # if path is not a directory
    print(f"Наданий шлях не є директорією {path}")
except FileNotFoundError: # if path does not exist
    print(f"Директорія не знайдена: {path}")

