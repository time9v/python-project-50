def check_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def make_plain(lists, path=''):
    res = []
    for elem in lists:
        key = elem['key']
        value = elem['value']
        valuen = elem['new_value']
        string = f"Property '{path}{key}' was"
        match elem['status']:
            case "dict":
                res.append(make_plain(value, f"{path}{key}."))
            case "deleted":
                res.append(f"{string} removed")
            case "added":
                res.append(f"{string} added with value: {check_val(value)}")
            case "updated":
                res.append(f"{string} updated. "
                           f"From {check_val(value)} to {check_val(valuen)}")
            case "without changes":
                continue
            case _:
                raise ValueError
    return "\n".join(res)
