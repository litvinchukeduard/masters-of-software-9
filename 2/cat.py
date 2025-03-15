import sys

import pathlib_example

# from pathlib import Path

'''
Потрібно написати код, який буде виводити усі рядки з файлу

cat.py file1.txt


'''

print(sys.argv)
# if len(sys.argv) < 2:
#     print('Please provide filename')
# else:
#     print('Working on file...')

if len(sys.argv) < 2:
    print('Please provide filename')
    sys.exit(1)

print('Working on file...')
with open(sys.argv[1]) as file:
    for line in file:
        print(line, end='')
