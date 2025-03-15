
'''
Є список з імен, потрібно знайти на якому місці є певне імʼя 
'''

# names_list = ["Denys", "Ivan", "Igor" ]

# range
# enumerate

# for name in names_list:
#     print(name)

# for i in range(len(names_list)):
#     name = names_list[i]
#     if name == 'Denys':
#         print(i)
#         break

# print(enumerate(names_list))

# for i, name in enumerate(names_list):
#     if name == 'Denys':
#         print(i)
#         break

# enumeration = enumerate(names_list)
# print(next(enumeration))

# print("Hello, world!")
# print(next(enumeration))
# print(next(enumeration))
# print(next(enumeration))

# for i, name in enumerate(names_list):

numbers = [1, 2, 3]
names = ["Ihor", "Andriy"]

for pair in zip(numbers, names, strict=True):
    print(pair)

