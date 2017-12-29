'''User input supplies function parameter'''

def happy_birthday(person):
    """string print method """
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

def main():
    """entry func"""
    user_name = input("Enter the Birthday person's name: ")
    happy_birthday(user_name)

main()
