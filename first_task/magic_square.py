import numpy


def user_input():
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


def draw_square(square_edge):
    """ Return a square (numpy matrix)

    Take the user positive odd integer as argument
    """

    # We create a square with square_edge as size and set the default value to be int
    square = numpy.zeros((square_edge, square_edge),dtype=int)

    # square is a "matix" of N list
    # we use list index to place our first number
    current_list = 0
    list_index = square_edge // 2

    for number in range(1, square_edge**2+1, 1):
        square[current_list, list_index] = number

        update_current_list = (current_list - 1) % square_edge
        update_list_index = (list_index + 1) % square_edge

        if square[update_current_list, update_list_index]:
            current_list += 1

        else:
            current_list = update_current_list
            list_index = update_list_index

def magic_square():
    """  """
    square_edge = user_input()
    return draw_square(square_edge)


print(magic_square())