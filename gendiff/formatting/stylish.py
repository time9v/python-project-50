def to_str(elem):
    if isinstance(elem, bool):
        if elem:
            return "true"
        else:
            return "false"
    elif elem is None:
        return "null"
    return str(elem)


def make_string(elem, d, new_string=''):
    space = d * '    '
    space2 = f"\n{(d + 1) * '    '}"
    if isinstance(elem, dict):
        for key, value in elem.items():
            if isinstance(value, dict):
                new_string += f"{space2}{str(key)}: {make_string(value, d + 1)}"
            else:
                new_string += f"{space2}{str(key)}: {to_str(value)}"
        return f"{{{new_string}\n{space}}}"
    else:
        return to_str(elem)


def make_stylish(lists, d=1):
    res = []
    for elem in lists:
        key = elem['key']
        value = elem['value']
        value_new = elem['new_value']
        space = d * "    "
        string = space + key
        space2 = (d - 1) * "    "
        string1 = f"{space2}  - {key}: "
        string2 = string1.replace("-", "+")
        match elem['status']:
            case "dict":
                res.append(f"{string}: {make_stylish(value, d + 1)}")
            case "deleted":
                res.append(string1 + make_string(value, d))
            case "added":
                res.append(string2 + make_string(value, d))
            case "updated":
                res.append(string1 + make_string(value, d))
                res.append(string2 + make_string(value_new, d))
            case "without changes":
                res.append(f"{string}: {make_string(value, d)}")
            case _:
                raise ValueError
    string = "\n".join(res)
    return f"{{\n{string}\n{(d - 1) * '    '}}}"
