# struktura direktorii
from pathlib import PurePath
path = input("Enter the path to the folder : ") # Enter the path to the folder
p = PurePath(path)
print("Name:", p.name)  
print("Suffix:", p.suffix) 
print("Parent:", p.parent)

