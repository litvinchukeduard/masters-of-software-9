from pathlib import Path


p = Path('/Users/eddielitvinchuk/Documents/Repositories/masters-of-software-9/2/cat.py')
# print(p.)

print(__file__)

current_dir = Path(__file__).parent
# print(p)
# __file__

# print(__name__)
# if __name__ == '__main__':
#     print("Hello")

# './.gitignore' -> Якщо в межах проекту
# '/Users/elitv/Documents/file.doc' -> Абсолютний

# filepath = current_dir / 'hello' / 'text.txt'

filepath = current_dir / 'text.txt'
print(filepath)

with open(filepath) as file:
    print(file.readlines())
