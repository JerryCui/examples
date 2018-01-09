'''stub for savings.py exercise.'''

def savingGrowth(deposit, interestPercentage, goal):
    '''Print the account balance for each year until it reaches
    or passes the goal.
    >>> savingGrowth(100, 8.0, 125)
    Year 0: $100.00
    Year 1: $108.00
    Year 2: $116.64
    Year 3: $125.97
    '''
    # code here!
    year_count = 0
    while deposit <= goal:
        deposit = deposit*(1 + interestPercentage/100)
        print("Year ", year_count, "$%.2f"%deposit)
        year_count = year_count + 1



    
savingGrowth(100, 8.0, 125)
