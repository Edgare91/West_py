import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Edgar Nunez
	Module: gladysUserInterface
	Description: This module does the interface and is like the glue to put all the modules working
    together / Also, it contains the menu and the runTests Function //
"""


def runTests():
    """
            tests some module functions
    """

    print("running a few tests")

    average = compute.gpsAverage(4, 5)
    print("average = ", average)

    # delete the remaining code *in this function* and replace it with
    # your code. add more code to do what the assignment asks you to do.
    # add 3 more tests of different functions in different modules
    print("hello!")


def start():
    """
    Start the whole app

    """

    userName = userLogin.login()

    runApp(userName)


def runApp(userName):
    """
            runs the app
    """

    # loop until user types q
    userQuit = False
    while (not userQuit):

        # menu
        """
                create a function to print your menu and simply call it here.
        """
        print("\n--| Welcome to the Gladys West Map App |--")
        print("         User: "+userName)
        print('''\n
1.- Type "C" to set current position
2.- Type "D" to set destination position
3.- Type "M" to map – which tells the distance
4.- Type "T" to run module tests
5.- Type "Q" to quit
		''')
        print()

        # get first character of input for the menu
        userInput = input("Enter a command: ")
        lowerInput = userInput.lower()
        firstChar = lowerInput[0:1]
        global x1
        global y1
        global x2
        global y2
        global sumInitialSat
        global sumFinalSat

        # menu choices, use a switch-like if-elif control structure

        """
			here students need to change and add to this code to
			handle their menu options
		"""
        # quit
        if firstChar == 'q':
            userQuit = True

       # run some tests (this is part 1 of 2)
        elif firstChar == 'c':

            """_summary_

            1.- Type "C" to set current position //
            (x1,y1) values can only be from 0 to 99
            values can only be integer values (whole numbers) //
            output: if input is out of range "Value of out range, please try again"
            output: if input != int, except = "Invalid value, please enter a whole number"
            """

            while True:
                try:
                    global x1
                    x1 = int(
                        input("Please enter an initial value between 0 and 99 for 'X': "))
                    if (x1 >= 0 and x1 <= 99) == True:
                        break
                    else:
                        print("Value of out range, please try again")
                except:
                    print("Invalid value, please enter a whole number")

            while True:
                try:
                    global y1
                    y1 = int(
                        input("Please enter an initial value between 0 and 99 for 'Y': "))
                    if (y1 >= 0 and y1 <= 99) == True:
                        break
                    else:
                        print("Value of out range, please try again")
                except:
                    print("Invalid value, please enter a whole number")

            altitude = satellite.gpsInitialValue(x1, y1, 'altitude')

            # altitud = satValue

            latitude = satellite.gpsInitialValue(x1, y1, 'latitude')
            # latitude = satValue

            longitude = satellite.gpsInitialValue(x1, y1, 'longitude')
            # longitude = satValue

            time = satellite.gpsInitialValue(x1, y1, 'time')
            # time = satValue

            sumInitialSat = (altitude + latitude + longitude + time)

            print(sumInitialSat)

            global initialAverage

            initialAverage = compute.gpsInitialAverage()

        # runTests()

        elif firstChar == 'd':

            """_summary_

            2.- Type "D" to set destination position //
            (x2,y2) values can only be from 0 to 99
            values can only be integer values (whole numbers) //
            output: if input is out of range "Value of out range, please try again"
            output: if input != int, except = "Invalid value, please enter a whole number"
            """

            while True:
                try:

                    x2 = int(
                        input("Please enter a final value between 0 and 99 for 'X': "))
                    if (x2 >= 0 and x2 <= 99) == True:
                        break
                    else:
                        print("Value of out range, please try again")
                except:
                    print("Invalid value, please enter a whole number")

            while True:
                try:
                    y2 = int(
                        input("Please enter a final value between 0 and 99 for 'Y': "))
                    if (y2 >= 0 and y2 <= 99) == True:
                        break
                    else:
                        print("Value of out range, please try again")
                except:
                    print("Invalid value, please enter a whole number")

            altitude = satellite.gpsFinalValue(x2, y2, 'altitude')

            # altitud = satValue

            latitude = satellite.gpsFinalValue(x2, y2, 'latitude')
            # latitude = satValue

            longitude = satellite.gpsFinalValue(x2, y2, 'longitude')
            # longitude = satValue

            time = satellite.gpsFinalValue(x2, y2, 'time')
            # time = satValue

            sumFinalSat = int(altitude + latitude + longitude + time)

            print(sumFinalSat)

            global finalAverage

            finalAverage = compute.gpsFinalAverage()

        elif firstChar == 'm':
            compute.distance()

        elif firstChar == 't':
            runTests()
        elif firstChar == 't':
            runTests()
        elif firstChar == 't':
            runTests()

        else:
            print("ERROR: " + firstChar + " is not a valid command")

    print("\n")
    print("Thank you for using the Gladys West Map App!")
    print("\n")
