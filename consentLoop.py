'''Illustrate an awkward form of an interactive loop, entering lines,
with an explicit check about continuing before each line.'''

def main():
    """loop"""
    lines = list()
    test_answer = input('Press y if you want to enter more lines: ')
    while test_answer == 'y':
        line = input('Next line: ')
        lines.append(line)
        test_answer = input('Press y if you want to enter more lines: ')

    print('Your lines were:')
    for line in lines:
        print(line)

main()
