import json
import gladysUserInterface
"""
	Student: Edgar Nunez
	Module: gladysSatellite

Description: This module does Opens and reads any of the four data files from disk based on the
satellite name given to readSat function. Reads latitude, longitude, altitude, and time
information into data structures. Returns the data that was read to the gladysUserInterface module
"""


def read_sat(sat, pathToJSONDataFiles):
    """Function that read the JSON files.

    Args:
        sat: Name of JSON file satellite.
        pathToJSONDataFiles: Location of JSON file.

    Raises:
        IOError: "It is an error raised when an input/output operation fails, such as the print
        statement or the open() function when trying to open a file that does not exist."

    Returns:
        data = The content of the JSON files.
    """

    file_name = sat + "-satellite.json"
    file_path = pathToJSONDataFiles + "/" + file_name

   # open the file
    try:
        file_handle = open(file_path)
    except IOError:
        print("ERROR: Unable to open the file " + file_path)
        raise IOError

    # read the file
    data = json.load(file_handle)

    return data


def gps_initial_value(x1, y1, sat):
    """Function that returns the values matching in the 4 satelites
    [altitude,latitud, longitud, time ] for the initial coordenates ('C')

    Args:
        x: _Coordenade in x axis for the INITIAL point_
        y: _Coordenate in y axis for the INITIAL point
        sat: _Name of satelite

    Returns:
        The 4 matching satellites values with the input for the current location 
    """

    pathToJSONDataFiles = "/Users/Edgar/Documents/GitHub/West_py/src"

    # read the satellite data
    data = read_sat(sat, pathToJSONDataFiles)

    value_dictionary = {}

    for elem in data:
        x = elem['x']
        y = elem['y']
        value = elem['value']
        value_dictionary[x, y] = value

    gladysUserInterface.coordinate_validator(x1)
    gladysUserInterface.coordinate_validator(y1)

    for (i) in value_dictionary:
        if i == (x1, y1):
            return (value_dictionary[i])


def gps_final_value(x2, y2, sat):
    """Function that returns the values matching in the 4 satelites
    [altitude,latitud, longitud, time ] for the FINAL coordenates ('D')

    Args:
        x: _Coordenade in x axis for the FINAL point_
        y: _Coordenate in y axis for the FINAL point
        sat: _Name of satelite

    Returns:
        The 4 matching satellites values with the input for the destination location 
    """
    pathToJSONDataFiles = "/Users/Edgar/Documents/GitHub/West_py/src"

    # read the satellite data
    data = read_sat(sat, pathToJSONDataFiles)

    value_dictionary = {}

    for elem in data:
        x = elem['x']
        y = elem['y']
        value = elem['value']
        value_dictionary[x, y] = value

    gladysUserInterface.coordinate_validator(x2)
    gladysUserInterface.coordinate_validator(y2)

    for (i) in value_dictionary:
        if i == (x2, y2):
            return (value_dictionary[i])
