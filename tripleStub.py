'''Stub for triple exercise.'''

def tripleAll(nums):
    ''' print triple each of the numbers in the list nums.
    >>> tripleAll([2, 4, 1, 5])
    6
    12
    3
    15
    >>> tripleAll([-6])
    -18
    '''
    # code here
    for item in nums:
        tripleitems = 3*item
        printout = '{} s triple is {}'.format(item, tripleitems)
        print(printout)
    
      
    
tripleAll([2, 4, 1, 5])
tripleAll([-6])    
    
