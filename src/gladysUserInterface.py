
import gladysCompute as compute
import gladysUserLogin as userLogin

"""
	Student: Edgar Nunez
	Module: gladysUserInterface
	Description: This module does the interface and is like the glue to put all the modules working
    together / Also, it contains the menu and the runTests Function //
"""


def start():
    """ Starts the app getting the userName from the login module (lowerEmail)
    """
    user_name = userLogin.login()

    run_app(user_name)


def coordinate_validator(input):
    """Function which validates the coordinates.

    Args:
        input: _input type str for any coordinate (x1,y1,x2,y2)_

    Returns:
        boolean. True if the coordinate is valid
    """

    try:
        input_converted = int(input)

        if isinstance(input_converted, int) == True:

            if (input_converted >= 0 and input_converted <= 99) == True:
                return input_converted
            else:
                print("Value out of range, please try again")
                return False
        else:
            print("Invalid value, please type a WHOLE number")
            return False

    except ValueError:
        print('You cannot enter characters')


def run_app(user_name):
    """
    Boddy of the app / Menu / Switches cases
    """

    # loop until user types q
    user_quit = False
    # While userQuit not True still printing the Menu
    while not user_quit:

        print("\n--| Welcome to the Gladys West Map App |--")
        print("         User: "+user_name)
        print("\n1.- Type 'C' to set current position")
        print("2.- Type 'D' to set destination position")
        print(
            "3.- Type 'M' to calculate the distance between current & destination position")
        print("4.- Type 'Q' to quit\n")

        # get first character of input for the menu
        user_input = input("Enter a command: ")
        lower_input = user_input.lower()
        first_char = lower_input[0:1]

        if first_char == 'q':
            user_quit = True

        elif first_char == 'c':
            line = f"\n------------------------------------------"

            x1 = input(
                "Please enter an initial value between 0 and 99 for 'X': ")
            coordinate_validator(x1)

            y1 = input(
                "Please enter an initial value between 0 and 99 for 'Y': ")
            coordinate_validator(y1)

            print(line)

            current_string = f"\n   Your current position is X= {x1}, Y={y1}"

            print(current_string)
            print(line)

        elif first_char == 'd':

            line = f"\n------------------------------------------"

            x2 = input(
                "Please enter a final value between 0 and 99 for 'X': ")
            coordinate_validator(x2)

            y2 = input(
                "Please enter a final value between 0 and 99 for 'Y': ")
            coordinate_validator(y2)

            print(line)

            destination_string = f"\n  Your destination position is X= {x2}, Y= {y2}"

            print(destination_string)
            print(line)

        elif first_char == 'm':
            try:
                distance = compute.distance(x1, y1, x2, y2)
                distance_string = f"\n        The distance is: {round(distance, 2)}"

                print(line)
                print(current_string)
                print(destination_string)
            except UnboundLocalError:
                line = f"\n--------------------------------------------------------------"
                print(line)
                print("\nPlease enter first current location, second final destination \nand finally select the option to calculate distance. \nPlease try again")
                print(line)
                run_app(user_name)

            print(distance_string)
            print(line)

        else:
            print("ERROR: " + first_char + " is not a valid command")

    print("\n")
    print("Thank you for using the Gladys West Map App!")
    print("\n")
