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
            user_input = int(input("\nPlease enter a positive odd integer: "))

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

    Take a positive odd integer as argument
    """

    # create a square filled with zeros with square_edge as size and int as data type
    square = numpy.zeros((square_edge, square_edge), dtype=int)

    # square is a "matix" of N (square_edge) list
    # we use list index to place the numbers
    current_list = 0
    list_index = square_edge // 2

    # magic square logic
    for number in range(1, square_edge**2+1, 1):

        # we place our first number
        square[current_list, list_index] = number

        # we update how the next number will be placed in the square
        update_current_list = (current_list - 1) % square_edge
        update_list_index = (list_index + 1) % square_edge

        # if value of the index are not 0 we will increment current_list
        if square[update_current_list, update_list_index]:
            current_list += 1

        # else we simply update the index
        else:
            current_list = update_current_list
            list_index = update_list_index

    return square


def check_magic_square(square, square_edge):
    """ Check if the magic square is magic...

    arguments:
        square: our numpy square object
        square_edge: an int number (from user_input)
    """

    def check(square_edge, list_to_check):
        # NB There is many ways to that:
        # as the zen said simple is better than complex...

        # The formula is M = (n²(n²+1)/2) / n
        constant = ((square_edge**2) * (square_edge**2 + 1) / 2) / square_edge

        for el in list_to_check:
            # We compare that each iterator elements is equal to the magic constant
            assert el == constant, "{} is not magic".format(list_to_check)

    # Check constant for each row
    check(square_edge, numpy.sum(square, axis=0))

    # Check constant for each column
    check(square_edge, numpy.sum(square, axis=1))

    # Check constant for diagonal
    check(square_edge, [numpy.sum(square.diagonal())])

    return print("Correct \n")


def magic_square():
    """ Wrap functions into one

    Steps:
        1 - user input
        2 - draw square
        3 - print square
        4 - check square validity
    """
    square_edge = user_input()
    square = draw_square(square_edge)
    print("\n", square, "\n")
    check_magic_square(square, square_edge)


magic_square()