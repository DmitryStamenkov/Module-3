def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'cat', False]
values_dict = {'a' : 4, 'b' : 'dog', 'c' : 5.25}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3, 'mouse']
print_params(*values_list_2, 35)
