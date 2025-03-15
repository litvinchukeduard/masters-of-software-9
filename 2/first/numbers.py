'''

У файлі записані числа 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

Потрібно написати функцію, яка буде читати їх та виводити усі парні числа
'''

# Прочитати
# Перевірити чи парні
# Вивести парні
# 4 / 2 = 2, 5 / 2 = 4 + 1

def read_numbers_from_file(path: str) -> list[int]:
    numbers = []
    with open(path, encoding='utf-8') as file:
        for line in file:
            string_numbers = line.split(' ')
            # print(string_numbers)
            for string_number in string_numbers:
                numbers.append(int(string_number))
    return numbers

numbers_list = read_numbers_from_file('2/first/numbers.txt')
# print(numbers_list)

def print_even_numbers(numbers_list: list[int]):
    for number in numbers_list:
        if number % 2 == 0:
            print(number)

print_even_numbers(numbers_list)

# print(4 % 2)


