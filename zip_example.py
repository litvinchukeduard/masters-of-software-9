
'''
Обʼєднати кожного користувача з його віком
'''

# names = input("Enter names: ")
# ages = input("Enter ages: ")

# print(names)
# print(ages)

names_list = ["Ivan", "Igor", "Denys"]
age_list = [32, 44, 13]

# print(list(zip(names_list, age_list)))

# person_dict = {"Ivan": 32, "Igor": 44, "Denys": 13}
# print(person_dict.items())

for name, age, number in zip(names_list, age_list, [1, 2, 3]):
    print(name, age)

[10, 11, 10, 9, 10]
[100, 110, 109, 110]
[10, 9, 10, 10, 10]