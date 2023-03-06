import math
import gladysSatellite as satellite
import gladysUserInterface
# math.sqrt(x) Return the square root of x.


"""
Student: Edgar Nunez
Module: gladysCompute
Description: This module does the matemathical operations
             for Average and the formula for the distance.
             After getting the SUM of the Gps Values comming
             from the Stellite Module.
"""


def gpsInitialAverage():
    """Function that determines the averege gps data from 
    the INITIAL point ('C') coming from the interface.

    Returns:
        Average of the INICIAL values (SUM of the 4 satellites / 4)
    """

    try:
        from gladysUserInterface import x1, y1

        altitude = satellite.gpsInitialValue(x1, y1, 'altitude')

        latitude = satellite.gpsInitialValue(x1, y1, 'latitude')

        longitude = satellite.gpsInitialValue(x1, y1, 'longitude')

        time = satellite.gpsInitialValue(x1, y1, 'time')

        sumInitialSat = (altitude + latitude + longitude + time)

        global average

        average = sumInitialSat / 4

        return average

    except ImportError:
        line = f"\n---------------------------------------------------------------------------"
        print(line)
        print("\nYou need to enter a CURRENT coordenates in order to calculate the distance. \nPlease try again. ")
        print(line)
        from gladysUserInterface import userName
        gladysUserInterface.runApp(userName)


def gpsFinalAverage():
    """Function that determines the averege gps data from the FINAL point ('D')
       coming from the interface.

    Returns:
        Average of the FINAL values (SUM of the 4 satellites / 4)
    """
    try:
        from gladysUserInterface import x2, y2

        altitude = satellite.gpsFinalValue(x2, y2, 'altitude')

        # altitud = satValue

        latitude = satellite.gpsFinalValue(x2, y2, 'latitude')
        # latitude = satValue

        longitude = satellite.gpsFinalValue(x2, y2, 'longitude')
        # longitude = satValue

        time = satellite.gpsFinalValue(x2, y2, 'time')
        # time = satValue

        sumFinalSat = (altitude + latitude + longitude + time)

        average = sumFinalSat / 4

        return average

    except ImportError:

        print(line)
        print("You need to enter a FINAL destination coordenates in order to calculate the distance.")
        print("Please try again. ")
        print(line)

        from gladysUserInterface import userName
        gladysUserInterface.runApp(userName)


def distance():
    """Function that determines the distance between
    inicial and final coordenates.

    Args:
        gpsInitialAverage: Initial avereged of the SUM of
                           all satellites for Initial Point
        gpsFinalAverage: Final avereged of the SUM of
                         all satellites for Final Point

    Returns:
        Distance between Inicial and Final Average .
        (Squre root of the SUM of the 2 the Avereges^2)
    """

    initialAverage = gpsInitialAverage()
    initialPower = initialAverage**2
    finalAverage = gpsFinalAverage()
    finalPower = finalAverage**2

    distance = math.sqrt(initialPower+finalPower)

    return distance
