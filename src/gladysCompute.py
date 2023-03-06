import io

import math
# math.sqrt(x) Return the square root of x.

"""
	Student: Edgar Nunez
	Module: gladysCompute
	Description: This module does the matemathical operations for Average and the formula
    for the distance. After getting the SUM of the Gps Values comming from the Stellite
    Module.
"""


def gpsInitialAverage():
    """
            document your function definition here. what does it do?
    """

    """
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.
	"""
    from gladysUserInterface import sumInitialSat

    average = sumInitialSat / 4

    print(average)
    return average


def gpsFinalAverage():
    """
            document your function definition here. what does it do?
    """

    """
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.
	"""
    from gladysUserInterface import sumFinalSat

    average = sumFinalSat / 4

    print(average)
    return average


def distance():
    """_summary_ Function that determines the distance between inicial and final coordenates.

    Args:
        gpsInitialAverage: Initial avereged of the SUM of all satellites for Initial Point
        gpsFinalAverage: Final avereged of the SUM of all satellites for Final Point

    Returns:
        Distance between arguments. (Squre root of the SUM os the Avereges^2)
    """

    from gladysUserInterface import initialAverage, finalAverage

    initialPower = initialAverage**2
    finalPower = finalAverage**2

    distance = math.sqrt(initialPower+finalPower)

    print(round(distance, 2))

    return distance
