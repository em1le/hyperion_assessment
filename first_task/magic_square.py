import numpy

def user_interaction():
    """ Fonction that take care of user input

    Check if:
        - Positive
        - Odd integer
        - Type (ValueError)
    """

    while True:
        try:
            user_input = int(input("Please enter a positive odd integer: "))

            if user_input < 0:
                print("Enter a positive odd integer, try again")
                continue

            elif user_input%2 != 1:
                print("Enter an odd integer")
                continue

            elif user_input%2 == 1:
                return user_input
        except ValueError as e:
            print("{} is not an integer".format(e))



def magic_square():
    pass


print(user_interaction())