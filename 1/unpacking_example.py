
def my_function(number, word, floating_number):
    print(number)
    print(word)
    print(floating_number)

def my_function_two(number=0, word="", floating_number=0.0):
    print(number)
    print(word)
    print(floating_number)

my_list = [3.14, "hello", 1]

# my_function(my_list[0], my_list[1], my_list[2])
# my_function(*my_list)

# print("Ihor", 1243, [1, 2, 4], 1, 2, 3, 5)

# print(*my_list, sep="-")
my_function_two()
my_function_two("Ihor", 1243, [1, 2, 4])
my_function_two(word="Andriy", number=1243, floating_number=12.1)

my_dict = {"word": "Andriy", "number": 54321, "floating_number": 13.3}
my_function_two(**my_dict)
