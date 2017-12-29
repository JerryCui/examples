'''Fancier format string example, with locals().'''

def foo(x,y):
    sum = x + y
    prod = x * y
    formatStr = '{x} + {y} = {sum}; {x} * {y} = {prod}.'
    equations = formatStr.format(**locals())
    print(equations)

if __name__ == '__main__':
    foo(20,30)