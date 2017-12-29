'''Fancier format string example with
parameter identification numbers
-- useful when some parameters are used several times.'''

X = int(input('Enter an integer: '))
Y = int(input('Enter another integer: '))
FORMATSTR = '{0} + {1} = {2}; {0} * {1} = {3}.'
EQUATIONS = FORMATSTR.format(X, Y, X+Y, X*Y)
print(EQUATIONS)
print(FORMATSTR)
