# deep copy nested dictionaries, lists

# data = 3
data = {"a": 3, "b": {"x": 2}}


def check_non_nested(ip):
    return isinstance(ip, (str, int, float, bool))


def check_list(ip):
    return isinstance(ip, list)


def check_dict(ip):
    return isinstance(ip, dict)


def deep_copy(ip):
    if check_non_nested(ip):
        return ip

    if check_dict(ip):
        for key, val in ip.items():
            v = deep_copy(val)
            print(id(val), id(v))
            ip[key] = v

        return ip.copy()


output = deep_copy(data)
print(id(output), id(data))
print(id(output["b"]), id(data["b"]))
print(id(output["b"]["x"]), id(data["b"]["x"]))

data["b"]["x"] = 10
print(data)
print(output)
