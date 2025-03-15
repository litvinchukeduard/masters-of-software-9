from collections import defaultdict
# {}
# Створити список 
# Додати до списку елемент

# {'Document': ['file.doc']}
# Дістати список
# Додати до списку елемент

my_dict_one = dict()
my_dict_two = defaultdict(list)

my_dict_one['a'] = 1
my_dict_one['a'] += 1
print(my_dict_one)

# my_dict_one['b'] += 1
my_dict_two['b'].append('1')
print(my_dict_two)
