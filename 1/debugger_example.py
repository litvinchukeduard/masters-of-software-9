'''
'hello', 'e'
'''

word = input("Enter word: ")
letter = input("Enter letter: ")

val = True

# print(type(val) == int)
# print(isinstance(val, int))

# print(isinstance(val, int))

# if not isinstance(val, int):
#     raise ValueError("val should be an integer")

# if len(letter) > 1:
#     raise ValueError("Please enter letter of length 1")

for i, symbol in enumerate(word):
    if symbol == letter:
        print(i)
        break
