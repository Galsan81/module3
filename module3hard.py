data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(list_):
    res = 0
    if isinstance(list_, (int, float)):
        return list_
    if isinstance(list_, str):
        return len(list_)
    if isinstance(list_, list):
        for item in list_:
            res += calculate_structure_sum(item)
    if isinstance(list_, tuple):
        for ite in list_:
            res += calculate_structure_sum(ite)
    if isinstance(list_, dict):
        slovar = list_
        list_1 = slovar.items()
        for kitem in list_1:
            res += calculate_structure_sum(kitem)
    if isinstance(list_, set):
        for tem in list_:
            res += calculate_structure_sum(tem)
    return res

res = calculate_structure_sum(data_structure)
print(res)
