import json


def open_json_file(path_to_file):
    with open(path_to_file) as file:
        result = json.load(file)
        return result

def input_dicts(dict1, dict2):
    result = []
    keys = dict1.keys() | dict2.keys()

    for key in sorted(keys):
        if (key in dict1) and (key not in dict2):
            result.append(dict(name=key,
                               value=dict1[key],
                               status='deleted'))

        elif (key in dict2) and (key not in dict1):
            result.append(dict(name=key,
                               value=dict2[key],
                               status='added'))

        elif (key in dict1) and (key in dict2):
            dict1_general = dict1[key]
            dict2_general = dict2[key]

            if dict1_general == dict2_general:
                result.append(dict(name=key,
                                   value=dict1_general,
                                   status='unchanged'))

            elif dict1_general != dict2_general:
                result.append(dict(name=key,
                                   value=(dict1_general, dict2_general),
                                   status='changed'))

    return result

def generate_diff(data):
    result = {}

    for item in data:
        if 'name' in item:
            name = item['name']
            value = item.get('value')
            status = item['status']
            if status == 'deleted':
                result['  - ' + name] = value
            elif status == 'added':
                result['  + ' + name] = value
            elif status == 'changed':
                result['  - ' + name] = value[0]
                result['  + ' + name] = value[1]
            else:
                result['    ' + name] = value
    print('{')
    for key, value in result.items():

        print(f"{key}: {value}")
    print('}')


# def parsing(file1_path, file2_path):
#     file1 = open_json_file(file1_path)
#     file2 = open_json_file(file2_path)
#     a = input_dicts(file1, file2)
#     result = generate_diff(a)
#     return result




# file1 = {
#     "host": "hexlet.io",
#     "timeout": 50,
#     "proxy": "123.234.53.22",
#     "follow": False
# }
#
# file2 = {
#     "timeout": 20,
#     "verbose": True,
#     "host": "hexlet.io"
# }
# keys = file1.keys() | file2.keys()
# print(keys)
#
# file_path = r'\\wsl.localhost\Ubuntu\home\time9\python-project-50\files\file1.json'
#
# print((json.load(open(file_path))))
# print()
#
# print()
# print()
# print(input_dicts(file1,file2))

