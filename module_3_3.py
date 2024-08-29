def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return


print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [True, 15, "False"]
print_params(*values_list)
values_dict = {'a': "World", 'b': 2025, 'c': False}
print_params(**values_dict)
values_list_2 = ["String", 12345]
print_params(*values_list_2, 42)