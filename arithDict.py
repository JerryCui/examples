'''Fancier format string example, with locals().'''

def foo1(x_in, y_in):
    '''just learn for * ** locals and arith method'''
    sum_out = x_in + y_in
    prod_out = x_in * y_in
    format_str = '{x_in} + {y_in} = {sum_out}; {x_in} * {y_in} = {prod_out}.'
    equations_out = format_str.format(**locals())
    print(equations_out)

if __name__ == '__main__':
    foo1(20, 30)
