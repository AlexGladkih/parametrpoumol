def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['1 строка True']
print_params(*values_list, b=' ', c=' ')
values_dict = {'a':1, 'b':'строка ','c':True}
print_params(**values_dict)