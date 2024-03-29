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


def gps_initial_average(x1, y1):
    """Function that determines the averege gps data from 
    the INITIAL point ('C') coming from the interface.

    Returns:
        Average of the INICIAL values (SUM of the 4 satellites / 4)
    """

    try:
        x1 = gladysUserInterface.coordinate_validator(x1)
        y1 = gladysUserInterface.coordinate_validator(y1)

        altitude = satellite.gps_initial_value(x1, y1, 'altitude')

        latitude = satellite.gps_initial_value(x1, y1, 'latitude')

        longitude = satellite.gps_initial_value(x1, y1, 'longitude')

        time = satellite.gps_initial_value(x1, y1, 'time')

        sum_initial_sat = (altitude + latitude + longitude + time)

        average = sum_initial_sat / 4

        return average

    except ImportError:
        line = f"\n---------------------------------------------------------------------------"
        print(line)
        print("\nYou need to enter a CURRENT coordenates in order to calculate the distance. \nPlease try again. ")
        print(line)
        from gladysUserInterface import userName
        gladysUserInterface.run_app(userName)


def gps_final_average(x2, y2):
    """Function that determines the averege gps data from the FINAL point ('D')
       coming from the interface.

    Returns:
        Average of the FINAL values (SUM of the 4 satellites / 4)
    """
    try:
        x2 = gladysUserInterface.coordinate_validator(x2)
        y2 = gladysUserInterface.coordinate_validator(y2)

        altitude = satellite.gps_final_value(x2, y2, 'altitude')

        # altitud = satValue

        latitude = satellite.gps_final_value(x2, y2, 'latitude')
        # latitude = satValue

        longitude = satellite.gps_final_value(x2, y2, 'longitude')
        # longitude = satValue

        time = satellite.gps_final_value(x2, y2, 'time')
        # time = satValue

        sum_final_sat = (altitude + latitude + longitude + time)

        average = sum_final_sat / 4

        return average

    except ImportError:
        line = f"\n---------------------------------------------------------------------------"
        print(line)
        print("You need to enter a FINAL destination coordenates in order to calculate the distance.")
        print("Please try again. ")
        print(line)

        from gladysUserInterface import userName
        gladysUserInterface.run_app(userName)


def distance(x1, y1, x2, y2):
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
    x1 = gladysUserInterface.coordinate_validator(x1)
    y1 = gladysUserInterface.coordinate_validator(y1)
    x1 = gladysUserInterface.coordinate_validator(x2)
    y1 = gladysUserInterface.coordinate_validator(y2)

    initial_average = gps_initial_average(x1, y1)
    initial_power = initial_average**2
    final_average = gps_final_average(x2, y2)
    final_power = final_average**2

    distance = math.sqrt(initial_power+final_power)

    return distance
