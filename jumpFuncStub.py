'''Save as jumpFunc.py and complete it for the Strange Function Exercise.'''

def jump(n):
    '''Assume n is an integer.  If n is even, return n//2.
    Otherwise (n is odd) return 3*n + 1.
    '''
    # write!
    if n%2 != 0 :
        return 3*n + 1
    else:
        return n/2

def main():
    '''Print out jump(n) for n in 0, 1, ..., 10.'''
    # write!
    print(jump(10))


main()
