from pathlib import Path
my_file = Path('names.txt')

if my_file.exists():
    with open(my_file) as file:
        for name in file:
            print(name)
