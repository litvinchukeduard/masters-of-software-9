'''

В нас є перелік імен файлів

'file.txt', 'picture.png', 'file.pdf', 'file.doc'

Потрібно написати функцію, яка посортує файли за типом та виведе їх

Text, Picture, Document
['file.txt', 'picture.png', 'picture_two.jpeg', 'file.pdf', 'file.doc']

'''

# picture_extensions = ['png', 'jpeg', 'jpg', 'gif']
# text_extensions = ['txt']
# document_extensions = ['doc', 'pdf']

types_dict = {
    'Document': ['doc', 'pdf'],
    'Picture': ['png', 'jpeg', 'jpg', 'gif'],
    'Text': ['txt']
}

# print(types_dict.items())

files_list = ['file.txt', 'picture.png', 'picture_two.jpeg', 'file.pdf', 'file.doc', 'file.one.txt', 'unknown.file']


def sort_file(result_dict: dict[str, list[str]], filename: str):
    extension = filename.split('.')[-1]
    for extension_type, extension_list in types_dict.items():
        if extension in extension_list:
            if extension_type not in result_dict:
                result_dict[extension_type] = []
            result_dict[extension_type].append(filename)
    return result_dict

def sort_files(file_names_list: list[str]) -> dict[str, list[str]]:

    result_dict = {}

    # {'Text': ['file1.txt', 'file2.txt'], 'Document': ['file.doc', 'file.pdf']}

    # {}
    # Створити список 
    # Додати до списку елемент

    # {'Document': ['file.doc']}
    # Дістати список
    # Додати до списку елемент
    for file in file_names_list:
        print(sort_file(result_dict, file))


# def sort_file(result_dict: dict[str, list[str]], filename: str):
#     extension = filename.split('.')[-1]

    # if extension in picture_extensions:
    #     print('Picture', filename)
    #     if 'Picture' not in result_dict:
    #         result_dict['Picture'] = []
    #     result_dict['Picture'].append(filename)
            

    # elif extension in text_extensions:
    #     print('Text', filename)
    #     if 'Text' not in result_dict:
    #         result_dict['Text'] = []
    #     result_dict['Text'].append(filename)
        
    # elif extension in document_extensions:
    #     print('Document', filename)
    #     if 'Document' not in result_dict:
    #         result_dict['Document'] = []
    #     result_dict['Document'].append(filename)
    # else:
    #     print('Unknown', filename)

# def sort_files(file_names_list: list[str]) -> dict[str, list[str]]:

#     result_dict = {}

    # {'Text': ['file1.txt', 'file2.txt'], 'Document': ['file.doc', 'file.pdf']}

    # {}
    # Створити список 
    # Додати до списку елемент

    # {'Document': ['file.doc']}
    # Дістати список
    # Додати до списку елемент
    # for file in file_names_list:
    #     sort_file(result_dict, file)
    #     extension = file.split('.')[-1]
    #     if extension in picture_extensions:

    #         print('Picture', file)
    #         if 'Picture' not in result_dict:
    #             result_dict['Picture'] = []
    #         result_dict['Picture'].append(file)
            

    #     elif extension in text_extensions:
    #         print('Text', file)
    #     elif extension in document_extensions:
    #         print('Document', file)
    #     else:
    #         print('Unknown', file)

    # print(result_dict)
        # if extension == 'txt':
        #     print('Text')
        # elif extension == 'png' or extension == 'jpeg':
        #     print('Picture')

sort_files(files_list)


# my_dict = {'a': 1, 'b': 2}
# print('c' in my_dict)
