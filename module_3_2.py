def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1, 58.57, 'adf']
values_dict = {'a':586, 'b':'qweerr', 'c': 78.98}
values_list_2 = [54.32, 'Строка']
print_params(1, 'строка', True)
print_params(b=25)
print_params(c=[1, 7, 25])
print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 78995)
