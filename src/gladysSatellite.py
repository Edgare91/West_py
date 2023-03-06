import io
import json
import gladysUserInterface as userInterface
"""
	Student: Edgar Nunez
	Module: gladysSatellite

Description: This module does Opens and reads any of the four data files from disk based on the
satellite name given to readSat function. Reads latitude, longitude, altitude, and time
information into data structures. Returns the data that was read to the gladysUserInterface module
"""


def readSat(sat, pathToJSONDataFiles):
    """
            reads satellite data from a json file
            Students do NOT need to change the readSat function.
    """

    # data file path
    fileName = sat + "-satellite.json"

    # print("filePath = ", filePath)
    filePath = pathToJSONDataFiles + "/" + fileName

    # open the file
    try:
        fileHandle = open(filePath)
    except IOError:
        print("ERROR: Unable to open the file " + filePath)
        raise IOError

    # read the file
    data = json.load(fileHandle)

    return data


def gpsInitialValue(x, y, sat):
    """_summary_ Function that returns the values matching in the 4 satelites
        [altitude,latitud, longitud, time ]

        Args:
            x: _Coordenade in x axis for initial and final point_
            y: _Coordenate in y axis for initial and final point
            sat: _Name of satelite

        Returns:
            SUM of the 4 values previously matching from 4 Jsons file
        """

    pathToJSONDataFiles = "/Users/Edgar/Documents/GitHub/West_py/src"

    # read the satellite data
    data = readSat(sat, pathToJSONDataFiles)

    """



	"""

    valueDictionary = {}

    for elem in data:
        x = elem['x']
        y = elem['y']
        value = elem['value']
        valueDictionary[x, y] = value

    from gladysUserInterface import x1, y1

    for (i) in valueDictionary:
        if i == (x1, y1):
            return (valueDictionary[i])


def gpsFinalValue(x, y, sat):
    pathToJSONDataFiles = "/Users/Edgar/Documents/GitHub/West_py/src"

    # read the satellite data
    data = readSat(sat, pathToJSONDataFiles)

    """



	"""

    valueDictionary = {}

    for elem in data:
        x = elem['x']
        y = elem['y']
        value = elem['value']
        valueDictionary[x, y] = value

    from gladysUserInterface import x2, y2

    for (i) in valueDictionary:
        if i == (x2, y2):
            return (valueDictionary[i])
