def a_function(first_name, last_name):
    '''
    Docstring explains function
    '''
    return f'Somethingaaa, whats up {first_name} {last_name}'

print(a_function(first_name='Henry', last_name='Albuquerque'))

def calculator(a, b, operator):
    return eval(f'{a} {operator} {b}') 

print(calculator(1, 1, '+'))