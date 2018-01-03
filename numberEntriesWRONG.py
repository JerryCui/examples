def numberList(items): #WRONG code for illustration
    '''Print each item in a list items, numbered in order.'''
    number = 1
    for item in items:
        #number = 1
        print(number, item)
        number = number + 1

numberList(['apples', 'pears', 'bananas'])
