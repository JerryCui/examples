'''Illustrate a global constant being used inside functions.'''

PI = 3.14159265358979   # global constant -- only place the value of PI is set

def circle_area(radius):
    """circle area caculate"""
    return PI*radius*radius    # use value of global constant PI

def circle_circumference(radius):
    """circumference caculate"""
    return 2*PI*radius         # use value of global constant PI

def main():
    """constant"""
    print('circle area with radius 5:', circle_area(5))
    print('circumference with radius 5:', circle_circumference(5))

main()
