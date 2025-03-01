
def my_print(*args, **kwargs):
    print(kwargs)
    for element in args:
        print(element)

# print(*[1, 2, 3])

my_print(1, 2, 3, 4, hello="world", one=1)

print()

# my_print(*[1, 2, 3, 4])
