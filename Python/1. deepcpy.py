# deep copy nested dictionaries, lists

# sample input
# data = 2
# data = [1, [2], [3, [4]]]
data = {"a": 3, "b": {"x": {"y": 1}}, "c": [1, [2], [[3]]]}


def check_non_nested(ip):
    return isinstance(ip, (str, int, float, bool))


def check_list(ip):
    return isinstance(ip, list)


def check_dict(ip):
    return isinstance(ip, dict)


# traversing recrusively through each key and return the new object copy
def deep_copy(ip):
    if check_non_nested(ip):
        return ip

    if check_dict(ip):
        ip_cpy = ip.copy()
        for key, val in ip_cpy.items():
            v = deep_copy(val)
            ip[key] = v

        return ip_cpy

    if check_list(ip):
        ip_cpy = ip.copy()
        for i, j in enumerate(ip_cpy):
            ip_cpy[i] = deep_copy(j)
        return ip_cpy


output = deep_copy(data)

data["c"][2][0][0] = [3, 4, 5]
print(data)
print(output)
