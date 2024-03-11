from gendiff.parse import parsing_files, path_file
from gendiff.formatting.stylish import make_stylish
from gendiff.formatting.plain import make_plain
from gendiff.formatting.json_form import make_json


def make_dict(status, k, value, new_value=None):
    dictr = {
        "status": status,
        'key': k,
        'value': value,
        'new_value': new_value
    }
    return dictr


def check_key(k, file1, file2):
    if k in file1 and k in file2 and file1[k] == file2[k]:
        res = make_dict("without changes", k, file1[k])
    elif k in file1 and k in file2 and file1[k] != file2[k]:
        res = make_dict("updated", k, file1[k], file2[k])
    elif k in file1:
        res = make_dict("deleted", k, file1[k])
    elif k in file2:
        res = make_dict("added", k, file2[k])
    else:
        raise ValueError("There is no such key in files")
    return res


def make_diff(file1, file2):
    args = {**file1, **file2}
    diff = []
    for k in sorted(args.keys()):
        child1 = file1.get(k)
        child2 = file2.get(k)
        if isinstance(child1, dict) and isinstance(child2, dict):
            res = make_dict("dict", k, make_diff(child1, child2))
            diff.append(res)
        else:
            diff.append(check_key(k, file1, file2))
    return diff


def generate_diff(first_file, second_file, form="stylish"):
    file1, format1 = path_file(first_file)
    file2, format2 = path_file(second_file)
    dict1 = parsing_files(file1, format1)
    dict2 = parsing_files(file2, format2)
    lists = make_diff(dict1, dict2)
    if form == 'stylish':
        return make_stylish(lists)
    elif form == 'plain':
        return make_plain(lists)
    elif form == 'json':
        return make_json(lists)
    else:
        raise ValueError("Input correct argument")
